"""Unit tests for TaskManager service."""
import unittest
from unittest.mock import Mock
from services.task_manager import TaskManager
from models.task import Task


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.mock_storage = Mock()
        self.mock_storage.load_tasks.return_value = []
        self.manager = TaskManager(self.mock_storage)
    
    def test_add_task(self):
        task = self.manager.add_task("New task")
        
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(task.description, "New task")
        self.mock_storage.save_tasks.assert_called_once()
    
    def test_get_task(self):
        self.manager.add_task("Task 1")
        task = self.manager.get_task(0)
        
        self.assertIsNotNone(task)
        self.assertEqual(task.description, "Task 1")
    
    def test_get_task_invalid_index(self):
        task = self.manager.get_task(99)
        self.assertIsNone(task)
    
    def test_toggle_task(self):
        self.manager.add_task("Task 1")
        result = self.manager.toggle_task(0)
        
        self.assertTrue(result)
        self.assertTrue(self.manager.tasks[0].completed)
    
    def test_delete_task(self):
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        
        result = self.manager.delete_task(0)
        
        self.assertTrue(result)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].description, "Task 2")
    
    def test_get_all_tasks(self):
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        
        tasks = self.manager.get_all_tasks()
        
        self.assertEqual(len(tasks), 2)
        self.assertIsNot(tasks, self.manager.tasks)


if __name__ == "__main__":
    unittest.main()
