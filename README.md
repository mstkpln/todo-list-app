# To-Do List Application

A professional, enterprise-grade to-do list application built with Python and Tkinter, following SOLID principles and clean architecture patterns.

## Features

- ✅ Add, complete, and delete tasks
- 💾 Automatic data persistence (JSON storage)
- 🎨 Clean, modern UI
- 🏗️ Enterprise-level architecture
- 🧪 Comprehensive unit tests
- 📝 Task metadata (UUID, timestamps)

## Architecture

This application follows a layered architecture with clear separation of concerns:

```
todo_app/
├── main.py                 # Application controller & entry point
├── config.py               # Configuration and constants
├── models/
│   └── task.py            # Task data model
├── services/
│   ├── task_manager.py    # Business logic layer
│   └── storage.py         # Data persistence layer
├── views/
│   └── todo_view.py       # UI presentation layer
└── tests/
    ├── test_task.py       # Task model tests
    ├── test_task_manager.py  # Business logic tests
    └── test_storage.py    # Storage tests
```

## Requirements

- Python 3.7+
- tkinter (usually included with Python)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd todo_app
```

2. No additional dependencies required (uses Python standard library)

## Usage

Run the application:
```bash
python main.py
```

### Controls
- **Add Task**: Type in the text field and press Enter or click "Add"
- **Complete Task**: Select a task and click "Complete" to toggle completion status
- **Delete Task**: Select a task and click "Delete" to remove it

## Running Tests

Run all tests:
```bash
python -m unittest discover tests
```

Run specific test file:
```bash
python -m unittest tests.test_task
python -m unittest tests.test_task_manager
python -m unittest tests.test_storage
```

## Design Patterns & Principles

### SOLID Principles
- **Single Responsibility**: Each class has one clear purpose
- **Open/Closed**: Easy to extend without modifying existing code
- **Dependency Inversion**: High-level modules depend on abstractions

### Architecture Patterns
- **MVC Pattern**: Separation of Model, View, and Controller
- **Repository Pattern**: StorageService abstracts data access
- **Service Layer**: TaskManager encapsulates business logic

### Best Practices
- Type hints for better code clarity
- Dataclasses for clean data models
- Dependency injection for testability
- Configuration management
- Comprehensive error handling

## Data Persistence

Tasks are automatically saved to `tasks.json` in the application directory. Each task includes:
- Unique ID (UUID)
- Description
- Completion status
- Created timestamp
- Updated timestamp

## Future Enhancements

- Task priorities and categories
- Due dates and reminders
- Search and filter functionality
- Task sorting options
- Export/import functionality
- Dark mode theme
