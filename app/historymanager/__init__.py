"""
History manager: manages history of calculations and undo operations.
"""
from typing import Union
import os
import pandas as pd
from dotenv import load_dotenv

"""Load environment variables."""
load_dotenv()
HISTORY_FILE = os.getenv("HISTORY_FILE")

class historymanager:
    """Class to manage history of calculations."""
    def __init__(self):
        """Initialize the history manager with an empty history."""
        self.history = pd.DataFrame(columns=["entry"])

    def add_to_history(self, entry: str):
        """Add a calculation to the history."""
        new_record = {"entry": entry}
        self.history = pd.concat([self.history, pd.DataFrame([new_record])], ignore_index=True)

    def get_history(self) -> list:
        """Return the history of calculations."""
        return self.history["entry"].tolist()

    def undo_last(self) -> Union[str, None]:
        """Undo the last calculation."""
        if not self.history.empty:
            last_entry = self.history.iloc[-1]["entry"]
            self.history = self.history.iloc[:-1]  # Remove the last entry
            return last_entry
        return None
    
    def save_history(self):
        """Save the history to a file."""
        self.history.to_csv(HISTORY_FILE, index=False)

    def load_history(self):
        """Load the history from a file."""
        if os.path.exists(HISTORY_FILE):
            self.history = pd.read_csv(HISTORY_FILE)
        else:
            self.history = pd.DataFrame(columns=["entry"])

    def clear_history(self):
        """Clear the history."""
        self.history = pd.DataFrame(columns=["entry"])
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)