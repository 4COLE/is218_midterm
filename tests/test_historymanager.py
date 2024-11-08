"""
Unit tests for the HistoryManager class in the app.historymanager module.

This module contains tests for adding to history, getting history, 
undoing the last entry in the history, and saving/loading history.
"""

from app.historymanager import historymanager

def test_add_to_history():
    """Test that adding an entry to history correctly stores it."""
    history_manager = historymanager(history_file="test_history.csv")
    history_manager.add_to_history("1 + 1 = 2")
    assert history_manager.get_history() == ["1 + 1 = 2"]

def test_get_history_empty():
    """Test that getting history returns an empty list when no entries exist."""
    history_manager = historymanager(history_file="test_history.csv")
    assert not history_manager.get_history()

def test_undo_last():
    """Test that undo removes the last entry from the history."""
    history_manager = historymanager(history_file="test_history.csv")
    history_manager.add_to_history("5 - 3 = 2")
    history_manager.add_to_history("10 / 2 = 5")
    undo = history_manager.undo_last()
    assert undo == "10 / 2 = 5"
    assert history_manager.get_history() == ["5 - 3 = 2"]

def test_undo_last_empty():
    """Test that undo returns None when history is empty."""
    history_manager = historymanager(history_file="test_history.csv")
    assert history_manager.undo_last() is None

def test_save_history():
    """Test saving history to a CSV file."""
    history_manager = historymanager(history_file="test_history.csv")
    history_manager.add_to_history("5 * 5 = 25")
    history_manager.save_history()
    # Reload history to verify that it was saved
    history_manager.load_history()
    assert history_manager.get_history() == ["5 * 5 = 25"]

def test_load_history():
    """Test loading history from a CSV file."""
    history_manager = historymanager(history_file="test_history.csv")
    history_manager.add_to_history("3 + 3 = 6")
    history_manager.save_history()
    new_manager = historymanager(history_file="test_history.csv")
    new_manager.load_history()
    assert new_manager.get_history() == ["3 + 3 = 6"]

def test_clear_history():
    """Test clearing history."""
    history_manager = historymanager(history_file="test_history.csv")
    history_manager.add_to_history("9 - 4 = 5")
    history_manager.clear_history()
    assert history_manager.get_history() == []
