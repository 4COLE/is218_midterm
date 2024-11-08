"""
Unit tests for the historymanager class in the app.historymanager module.

This module contains tests for adding to history, retrieving history, saving and loading history,
clearing history, and undoing the last entry in the history.
"""

import os
from app.historymanager import historymanager


def test_history_manager_initialization_without_file():
    """Test that historymanager initializes with an empty DataFrame when no history file is present."""
    history_manager = historymanager()
    assert history_manager.get_history() == []

def test_add_to_history():
    """Test that adding an entry to history correctly stores it."""
    history_manager = historymanager()
    history_manager.add_to_history("1 + 1 = 2")
    assert history_manager.get_history() == ["1 + 1 = 2"]

def test_get_history_empty():
    """Test that getting history returns an empty list when no entries exist."""
    history_manager = historymanager()
    assert history_manager.get_history() == []

def test_undo_last():
    """Test that undo removes the last entry from the history."""
    history_manager = historymanager()
    history_manager.add_to_history("1 + 1 = 2")
    history_manager.undo_last()
    assert history_manager.get_history() == []

def test_undo_last_empty():
    """Test that undo returns None when history is empty."""
    history_manager = historymanager()
    assert history_manager.undo_last() is None

    #Unit tests for the historymanager class in the app.historymanager module.

def test_save_history():
    """Test saving history to a CSV file."""
    history_manager = historymanager()
    history_manager.add_to_history("1 + 1 = 2")
    history_manager.save_history()
    assert os.path.exists("history.csv")

def test_load_history():
    """Test loading history from a CSV file."""
    history_manager = historymanager()
    history_manager.add_to_history("1 + 1 = 2")
    history_manager.save_history()
    history_manager.load_history()
    assert history_manager.get_history() == ["1 + 1 = 2"]

def test_clear_history():
    """Test clearing the history."""
    history_manager = historymanager()
    history_manager.add_to_history("1 + 1 = 2")
    history_manager.clear_history()
    assert history_manager.get_history() == []
