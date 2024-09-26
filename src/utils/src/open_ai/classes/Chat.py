import os
from typing import List, Dict, Any, Literal
from collections.abc import Mapping, Sequence, Callable
from dotenv import load_dotenv
from inspect import isfunction
from pydantic import BaseModel, Field, model_validator
from dotenv import load_dotenv
from typing import Dict, Literal
from pydantic import BaseModel, Field
from openai import OpenAI, ChatCompletion
import openai

from classes import History as OAIH, Message as OAIM
from utils.execute_python import python
from utils.schema import schema
from utils.call_func import call_func

History = OAIH.OAIHistory
Message = OAIH.OAIMessage

load_dotenv()    

config = {
    "system_prompt": Message(role='system', content="You are an intelligent assistant that enjoys Australian Aphorisms."),
    "tools": [schema(python)],
    "model": "gpt-4-1106-preview",
    "max_tokens": 15500,
    "temperature": 0.83,
    "encoding_model_messages": "gpt-3.5-turbo-0613",
    "encoding_model_strings": "cl100k_base",
    "function_call_limit": 3,
}

class Open_AI_Chat(BaseModel):
    """
    class for handling Open Chat chat completions.
    """
    model: str = Field(config['model'], description="The model to be used for completions.")
    system: Message = Field(config['system_prompt'], description="The system prompt.")
    max_tokens: int = Field(config['max_tokens'], description="The maximum number of tokens for the completion.")
    temperature: float = Field(config['temperature'], description="The temperature for the completion.")
    history: History = Field(default_factory=History, description="The conversation history.")
    tools: List[dict] = Field([], description="The tools which can be utilized by the completion.")
    
    @property
    def client(self) -> OpenAI:
        if not hasattr(self, '_client'):
            self._client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),
                                  organization=os.getenv("OPENAI_ORGANIZATION"))
        return self._client

    # @model_validator(mode="before")
    # @classmethod
    # def validate_and_transform_fields(self, values):
    #     system = values.get('system', config['system_prompt'])
    #     if isinstance(system, str):
    #         system = Message.create(role='system', content=system)
    #     values['history'] = [system]  
    #     values['tools'] = self.append_tools([python] + values.get('tools', []))
        
    #     return values
    
    class Config:
        arbitrary_types_allowed = True
        validate_assignment = True


    def __str__(self) -> str:
        return f"Model: {self.model}\nMax Tokens: {self.max_tokens}\nSystem Prompt: {self.system}\nMessages: {self.history}"

    @classmethod
    def give_tools(tools: Sequence[Callable]) -> None:
        """Appends tools to the list of tools."""
        
        tls = []
        for tool in tools:
            print(schema(tool))
            if isfunction(tool):
                tls.push(schema(tool))
        return tls

    def completion(self, prompt: str, **kwargs: Any) -> None:                        
        self.history.add_message(role='user', content=prompt)
                     
        print(f"\n Calling the Open AI Api...\n")

        try:
            request_data = {
                "messages": self.history.get_messages(),
                "model": self.model,
                "max_tokens": self.max_tokens,
                "temperature": self.temperature
            }
            if self.tools:
                request_data["tools"] = self.tools
                
            completion = self.client.chat.completions.create(**request_data)
            response = Message.response(completion)
            if with_tools:
                response = call_func(response, self.tools)
            self.history.add_message(response)
            
        except Exception as e:
            Open_AI_Chat.handle_completion_error(e)
            return None

    @staticmethod
    def handle_completion_error(e: Exception) -> None:
        """Handles an error from the OpenAI API."""
        match e:
            case openai.APIConnectionError():
                print("The server could not be reached")
                print(e.__cause__)  # an underlying Exception, likely raised within httpx.
            case openai.RateLimitError():
                retry_after = int(e.headers.get("retry-after", 60))
                print(f"Rate limit exceeded, waiting for {retry_after} seconds...")
                time.sleep(retry_after)
                self.completion(prompt, kwargs)            
            case openai.BadRequestError():
                print(f"A 400 status code was received; bad request.\n{str(e)}")
            case openai.AuthenticationError():
                print(f"A 401 status code was received; authentication failed:\n{e.response}")
            case openai.PermissionDeniedError():
                print(f"A 403 status code was received; permission denied:\n{e.response}")
            case openai.NotFoundError():
                print(f"A 404 status code was received; resource not found:\n{e.response}")
            case openai.UnprocessableEntityError():
                print(f"A 422 status code was received; unprocessable entity:\n{e.response}")
        