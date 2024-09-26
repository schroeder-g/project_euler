from classes.Message import OAIMessage
from typing_extensions import Literal, TypedDict
from typing import Dict, Any, List
from pydantic import BaseModel, Field


class OAIHistory(BaseModel):
    messages: List[OAIMessage] = Field(
        [], description="The messages in the conversation history."
    )

    def add_message(self, role: str, content: str) -> None:
        """Adds a message to the conversation history."""
        self.messages.append(OAIMessage(role=role, content=content))

    def get_messages(self) -> List[OAIMessage]:
        """Returns the current conversation history."""
        return self.messages

    def remove_message(self, index: int) -> None:
        """Removes a message from the completion."""
        self.messages.pop(index)

    def clear_messages(self) -> None:
        """Clears the messages for the completion."""
        self.messages = []

    def update_message(self, index: int, message: OAIMessage) -> None:
        """Updates a message for the completion."""
        self.messages[index] = message

    def last(self) -> OAIMessage:
        """Returns the last message in the history."""
        return self.messages[-1]

    def __str__(self) -> str:
        return "\n".join([str(message) for message in self.messages])
