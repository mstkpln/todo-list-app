"""View layer for the to-do list application."""
import tkinter as tk
from tkinter import messagebox
from typing import Callable
from config import Config


class TodoView:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(Config.WINDOW_TITLE)
        self.root.geometry(f"{Config.WINDOW_WIDTH}x{Config.WINDOW_HEIGHT}")
        
        self.on_add_task: Callable[[str], None] = lambda x: None
        self.on_toggle_task: Callable[[int], None] = lambda x: None
        self.on_delete_task: Callable[[int], None] = lambda x: None
        
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        title = tk.Label(self.root, text="My To-Do List", font=Config.FONT_TITLE)
        title.pack(pady=10)
        
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(input_frame, width=Config.ENTRY_WIDTH, font=Config.FONT_NORMAL)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind("<Return>", lambda e: self._handle_add())
        
        add_btn = tk.Button(
            input_frame, 
            text="Add", 
            command=self._handle_add,
            bg=Config.COLOR_PRIMARY,
            fg=Config.COLOR_WHITE
        )
        add_btn.pack(side=tk.LEFT)
        
        self.task_listbox = tk.Listbox(
            self.root,
            width=Config.LISTBOX_WIDTH,
            height=Config.LISTBOX_HEIGHT,
            font=Config.FONT_LIST,
            selectmode=tk.SINGLE
        )
        self.task_listbox.pack(pady=10)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        tk.Button(
            button_frame,
            text="Complete",
            command=self._handle_toggle,
            bg=Config.COLOR_SECONDARY,
            fg=Config.COLOR_WHITE,
            width=Config.BUTTON_WIDTH
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="Delete",
            command=self._handle_delete,
            bg=Config.COLOR_DANGER,
            fg=Config.COLOR_WHITE,
            width=Config.BUTTON_WIDTH
        ).pack(side=tk.LEFT, padx=5)
    
    def _handle_add(self) -> None:
        description = self.task_entry.get().strip()
        if not description:
            messagebox.showwarning("Warning", "Please enter a task.")
            return
        self.on_add_task(description)
        self.task_entry.delete(0, tk.END)
    
    def _handle_toggle(self) -> None:
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task.")
            return
        self.on_toggle_task(selected[0])
    
    def _handle_delete(self) -> None:
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task.")
            return
        self.on_delete_task(selected[0])
    
    def update_task_list(self, tasks: list) -> None:
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            status = "✓" if task.completed else "○"
            display = f"{status} {task.description}"
            self.task_listbox.insert(tk.END, display)
