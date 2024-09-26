from typing_extensions import Literal, TypedDict
from typing import Dict, Any
from pydantic import Field
from fastcore.utils import nested_idx


class OAIMessage(TypedDict):
    """This class represents a message in a conversation."""

    role: Literal["user", "assistant", "system"] = Field(
        ..., description="The role of the message (user, assistant, or system)"
    )
    content: str = Field(..., description="The content of the message")

    class Config:
        validate_assignment = True

    def __str__(self) -> str:
        return f"{self.role}: {self.message}"

    def get(self) -> Dict[str, str]:
        """Returns a dict of the message's contents."""
        return {"role": self.role, "content": self.message}

    @staticmethod
    def response(completion: Dict[str, Any], with_tools=False) -> str:
        """Returns the response from OpenAI's ChatGPT API."""
        response = nested_idx(completion, "choices", 0, "message", "content")
        print(f"\nAssistant: {response}\n")
        return OAIMessage(role="assistant", content=response)
