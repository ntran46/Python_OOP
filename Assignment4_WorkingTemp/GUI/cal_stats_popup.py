import requests
import tkinter as tk
from tkinter import ttk, messagebox, SE, W


class CalStatsPopup(tk.Frame):
    """ Popup Frame to show statistics for the department """

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
            ttk.Label(self, text=key, justify=tk.LEFT).grid(row=_count, column=1)
            ttk.Label(self, text=str(value)).grid(row=_count, column=2, padx=10)
            _count += 1

        # ttk.Button(self, text="Close", command=self._close_cb).grid(row=4, column=2)
        ttk.Button(parent, text="Close", command=self._close_cb).place(relx=0.97, rely=0.97, anchor=SE)

    def _calculate_stats(self):
        """Get the people list information and return the according stats object"""
        response1 = requests.get("http://127.0.0.1:5000/department/persons/stats")
        response2 = requests.get("http://localhost:5000/department/person/all")

        if response1.status_code and response2.status_code is 200:
            data1 = response1.json()
            doctor_num = len(response2.json()["Doctor"])
            patient_num = len(response2.json()["Patient"])
            data = {'Report for the department ': response2.json()['name'],
                    'Total of people: ': doctor_num + patient_num,
                    'Number of Doctors: ': doctor_num,
                    'Number of Patients: ': patient_num,
                    '   Number of Released Patients: ': data1["released_patient"],
                    '   Number of Un-released Patients: ': data1["not_released_patient"],
                    '   Total bill amount ($) : ': data1['total_bill']
                    }

            return data
        else:
            error_mess = response1.text + response2.text
            messagebox.showerror("Error", error_mess, icon='error')