"""Task manager service for business logic."""
from typing import List, Optional
from models.task import Task
from services.storage import StorageService


class TaskManager:
    def __init__(self, storage: StorageService):
        self.storage = storage
        self.tasks: List[Task] = []
        self.load_tasks()
    
    def load_tasks(self) -> None:
        try:
            self.tasks = self.storage.load_tasks()
        except IOError as e:
            print(f"Warning: {e}")
            self.tasks = []
    
    def save_tasks(self) -> None:
        try:
            self.storage.save_tasks(self.tasks)
        except IOError as e:
            print(f"Error: {e}")
    
    def add_task(self, description: str) -> Task:
        task = Task(description=description)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def get_task(self, index: int) -> Optional[Task]:
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None
    
    def toggle_task(self, index: int) -> bool:
        task = self.get_task(index)
        if task:
            task.toggle_completion()
            self.save_tasks()
            return True
        return False
    
    def delete_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
            return True
        return False
    
    def get_all_tasks(self) -> List[Task]:
        return self.tasks.copy()
