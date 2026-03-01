"""Task model with enhanced features."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid


@dataclass
class Task:
    description: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    
    def toggle_completion(self) -> None:
        self.completed = not self.completed
        self.updated_at = datetime.now()
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        task = cls(
            description=data["description"],
            id=data["id"],
            completed=data["completed"],
            created_at=datetime.fromisoformat(data["created_at"])
        )
        if data.get("updated_at"):
            task.updated_at = datetime.fromisoformat(data["updated_at"])
        return task
