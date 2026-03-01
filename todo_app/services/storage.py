"""Storage service for task persistence."""
import json
from pathlib import Path
from typing import List
from models.task import Task


class StorageService:
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
    
    def save_tasks(self, tasks: List[Task]) -> None:
        try:
            data = [task.to_dict() for task in tasks]
            with open(self.filepath, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            raise IOError(f"Failed to save tasks: {e}")
    
    def load_tasks(self) -> List[Task]:
        if not self.filepath.exists():
            return []
        
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
            return [Task.from_dict(item) for item in data]
        except Exception as e:
            raise IOError(f"Failed to load tasks: {e}")
