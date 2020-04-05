import requests
import tkinter as tk
from tkinter import ttk, messagebox, SE, W


class CalStatsPopup(tk.Frame):
    """ Popup Frame to show statistics for the school """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        parent.title("Statistics Information")
        parent.geometry('400x200')
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2, padx=30, pady=30)
        data = self._calculate_stats()
        _count = 1
        for key, value in data.items():
            ttk.Label(self, text=key+":", justify=tk.LEFT).grid(row=_count, column=1)
            ttk.Label(self, text=str(value)).grid(row=_count, column=2, padx=10)
            _count += 1

        ttk.Button(parent, text="Close", command=self._close_cb).place(relx=0.97, rely=0.97, anchor=SE)

    @classmethod
    def _calculate_stats(cls):
        """Get the people list information and return the according staff object"""
        _students = 0
        _teachers = 0
        _quarantine_students = 0
        _quarantine_teachers = 0
        _quarantine_total = 0

        response = requests.get("http://localhost:5000/school")
        _total_ppl = len(response.json()["people"])

        for person in response.json()["people"]:
            if person["type"] == 'student':
                _students += 1
            if person["quarantine"]:
                _quarantine_total += 1
            if person["quarantine"] and person["type"] == 'student':
                _quarantine_students += 1

        _teachers = _total_ppl - _students
        _quarantine_teachers = _quarantine_total - _quarantine_students

        return {"The total people in the school": _total_ppl,
                "The number of Teachers": _teachers,
                "The number of Students": _students,
                "The total quarantined people in the school": _quarantine_total,
                "The number of quarantined Teachers": _quarantine_teachers,
                "The number of quarantined Students": _quarantine_students}
