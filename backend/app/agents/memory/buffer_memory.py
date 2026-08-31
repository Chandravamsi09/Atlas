from typing import List, Dict, Any


class ConversationBufferMemory:
    """Sliding-window in-memory conversation buffer maintaining recent dialogue turns."""
    def __init__(self, max_messages: int = 10):
        self.max_messages = max_messages
        self.messages: List[Dict[str, str]] = []

    def add_turn(self, role: str, content: str) -> None:
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def get_history(self) -> List[Dict[str, str]]:
        return list(self.messages)

    def clear(self) -> None:
        self.messages.clear()
