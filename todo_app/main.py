"""Main application entry point."""
import tkinter as tk
from config import Config
from services.storage import StorageService
from services.task_manager import TaskManager
from views.todo_view import TodoView


class TodoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.storage = StorageService(Config.STORAGE_FILE)
        self.task_manager = TaskManager(self.storage)
        self.view = TodoView(self.root)
        
        self._bind_events()
        self._refresh_view()
    
    def _bind_events(self) -> None:
        self.view.on_add_task = self._handle_add_task
        self.view.on_toggle_task = self._handle_toggle_task
        self.view.on_delete_task = self._handle_delete_task
    
    def _handle_add_task(self, description: str) -> None:
        self.task_manager.add_task(description)
        self._refresh_view()
    
    def _handle_toggle_task(self, index: int) -> None:
        self.task_manager.toggle_task(index)
        self._refresh_view()
    
    def _handle_delete_task(self, index: int) -> None:
        self.task_manager.delete_task(index)
        self._refresh_view()
    
    def _refresh_view(self) -> None:
        tasks = self.task_manager.get_all_tasks()
        self.view.update_task_list(tasks)
    
    def run(self) -> None:
        self.root.mainloop()


def main():
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()
