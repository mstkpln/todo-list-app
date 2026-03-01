"""Application configuration and constants."""

class Config:
    # Window settings
    WINDOW_TITLE = "To-Do List"
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 500
    
    # Colors
    COLOR_PRIMARY = "#4CAF50"
    COLOR_SECONDARY = "#2196F3"
    COLOR_DANGER = "#f44336"
    COLOR_WHITE = "white"
    
    # Fonts
    FONT_TITLE = ("Arial", 18, "bold")
    FONT_NORMAL = ("Arial", 12)
    FONT_LIST = ("Arial", 11)
    
    # UI dimensions
    ENTRY_WIDTH = 30
    LISTBOX_WIDTH = 50
    LISTBOX_HEIGHT = 15
    BUTTON_WIDTH = 10
    
    # Storage
    STORAGE_FILE = "tasks.json"
