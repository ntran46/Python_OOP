import requests
import tkinter as tk
from tkinter import ttk, messagebox
import re


class CalStatsPopup(tk.Frame):
    """ Popup Frame to show statistics for the school """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        parent.title("Statistics Information")
        parent.geometry('400x200')
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2, padx=30, pady=30)

        listbox = tk.Listbox(tk.Frame)
        listbox.pack(side=tk.TOP)

        ttk.Button(self, text="Close", command=self._close_cb).grid(row=4, column=2)

    def _stats_cb(self):
        """Get the people list information and return the according stats object"""
        response = requests.get("http://127.0.0.1:5000/school")
        print(response.status_code)

        if response.status_code == 200:
            print(response.text)

        self.listbox = response
        doctor_num = 0
        patient_num = 0
        released_num_patients = 0
        # quarantine_num_teacher = 0
        ppl_count = 0
        # quarantine_num = 0
        for item in self.listbox:
            if item != None:
                ppl_count += 1
            if ["type"] == "Doctor":
                doctor_num += 1
            if ["type"] == "Patient":
                patient_num += 1
            if ["quarantine"] and ["type"] == "Patient":
                released_num_patients += 1
            # if ["quarantine"] and ["type"] == "teacher":
            #     quarantine_num_teacher += 1
            # if ["quarantine"]:
            #     quarantine_num += 1

        data = {'Report for: ': self._name,
                'Number of Doctors: ': doctor_num,
                'Number of Patients: ': patient_num,
                'Number of Released Patients: ': released_num_patients,
                'Number of Un-released Patients: ': patient_num - released_num_patients,
                # 'Number of All Quarantined People: ': quarantine_num,
                'Total of people: ': ppl_count}

        for k, v in data.items():
            self.listbox.insert(tk.END, f"{k}\t\t\t", "bold")
            self.listbox.insert(tk.END, f"{v}\n")