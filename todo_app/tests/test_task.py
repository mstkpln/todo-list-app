"""Unit tests for Task model."""
import unittest
from datetime import datetime
from models.task import Task


class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task(description="Test task")
        self.assertEqual(task.description, "Test task")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.id)
        self.assertIsInstance(task.created_at, datetime)
    
    def test_toggle_completion(self):
        task = Task(description="Test task")
        self.assertFalse(task.completed)
        
        task.toggle_completion()
        self.assertTrue(task.completed)
        self.assertIsNotNone(task.updated_at)
        
        task.toggle_completion()
        self.assertFalse(task.completed)
    
    def test_to_dict(self):
        task = Task(description="Test task")
        data = task.to_dict()
        
        self.assertEqual(data["description"], "Test task")
        self.assertEqual(data["id"], task.id)
        self.assertFalse(data["completed"])
        self.assertIsNotNone(data["created_at"])
    
    def test_from_dict(self):
        original = Task(description="Test task")
        data = original.to_dict()
        restored = Task.from_dict(data)
        
        self.assertEqual(restored.description, original.description)
        self.assertEqual(restored.id, original.id)
        self.assertEqual(restored.completed, original.completed)


if __name__ == "__main__":
    unittest.main()
