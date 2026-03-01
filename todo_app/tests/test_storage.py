"""Unit tests for StorageService."""
import unittest
import tempfile
import os
from pathlib import Path
from services.storage import StorageService
from models.task import Task


class TestStorageService(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.storage = StorageService(self.temp_file.name)
    
    def tearDown(self):
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_save_and_load_tasks(self):
        tasks = [
            Task(description="Task 1"),
            Task(description="Task 2")
        ]
        
        self.storage.save_tasks(tasks)
        loaded_tasks = self.storage.load_tasks()
        
        self.assertEqual(len(loaded_tasks), 2)
        self.assertEqual(loaded_tasks[0].description, "Task 1")
        self.assertEqual(loaded_tasks[1].description, "Task 2")
    
    def test_load_nonexistent_file(self):
        storage = StorageService("nonexistent.json")
        tasks = storage.load_tasks()
        self.assertEqual(tasks, [])
    
    def test_save_empty_list(self):
        self.storage.save_tasks([])
        loaded_tasks = self.storage.load_tasks()
        self.assertEqual(loaded_tasks, [])


if __name__ == "__main__":
    unittest.main()
