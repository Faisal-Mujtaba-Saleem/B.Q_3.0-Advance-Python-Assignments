# This code is taken from chatGPT to print the the text at the center of terminal. It is not relted to the assignment
import os
import shutil


def get_terminal_width():
    try:
        # Try to get terminal size (works on most Unix-like systems)
        size = shutil.get_terminal_size()
        return size.columns
    except Exception as e:
        print(f"Error: {e}")
        # Fallback width if terminal size cannot be determined
        return 80


def print_centered_text(text):
    terminal_width = get_terminal_width()
    # Center the text using the center method
    centered_text = text.center(terminal_width)
    print(centered_text)
