from datetime import datetime, time

import requests
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import re


class AddPatientPopup(tk.Frame):
    """ Popup Frame to Add a Student """

    def __init__(self, parent, close_callback):
        """ Constructor """
        self.is_released = False
        tk.Frame.__init__(self, parent)
        self.date_of_birth = ''

        parent.title("Add a Patient")
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2, padx=30, pady=30)

        ttk.Label(self, text="ID:").grid(row=1, column=1)
        self.id = ttk.Entry(self)
        self.id.grid(row=1, column=2)
        ttk.Label(self, text="First Name:").grid(row=2, column=1)
        self.first_name = ttk.Entry(self)
        self.first_name.grid(row=2, column=2)
        ttk.Label(self, text="Last Name:").grid(row=3, column=1)
        self.last_name = ttk.Entry(self)
        self.last_name.grid(row=3, column=2)
        ttk.Label(self, text="Date of Birth:").grid(row=4, column=1)
        ttk.Button(self, text="Calendar", command=self._date_of_birth).grid(row=4, column=2)

        ttk.Label(self, text="Address:").grid(row=5, column=1)
        self.address = ttk.Entry(self)
        self.address.grid(row=5, column=2)

        ttk.Label(self, text="Room Number:").grid(row=7, column=1)
        self.room_num = ttk.Entry(self)
        self.room_num.grid(row=7, column=2)
        ttk.Label(self, text="Bill Payment*:").grid(row=8, column=1)
        self.bill = ttk.Entry(self)
        self.bill.grid(row=8, column=2)

        ttk.Button(self, text="Submit", command=self._submit_cb).grid(row=9, column=1, pady=20)
        ttk.Button(self, text="Close", command=self._close_cb).grid(row=9, column=2)
        ttk.Label(self, text="(*) Not mandatory").grid(row=11, column=1)

    def _date_of_birth(self):
        """ Calendar popup """
        new_wins = tk.Toplevel()
        cal = DateEntry(new_wins, width=15, background="blue", foreground="red",
                        borderwidth=3, date_pattern='y-mm-dd')
        cal.pack(padx=10, pady=10)
        self.date_of_birth = cal.get_date()

    def _submit_cb(self):
        """ Submit the Add Patient button """
        data = {}
        data["first_name"] = self.first_name.get()
        data["last_name"] = self.last_name.get()
        data["date_of_birth"] = self.date_of_birth.strftime("%d-%b-%Y")
        data["address"] = self.address.get()
        data["id"] = self.id.get()
        try:
            data["room_num"] = int(self.room_num.get())
            if self.bill.get() != '':
                data["bill"] = int(self.bill.get())
                self.is_released = True
            else:
                data["bill"] = 0
                self.is_released = False
        except TypeError:
            messagebox.showerror("Error", "Room number or Bill amount must be greater than or equal 0, "
                                          "and they are an integer", icon="error")
        data["is_released"] = self.is_released

        # regex = re.compile('^[0-9]', re.I)
        # match = regex.match(str(data['id']))

        regex_1 = re.compile('[a-zA-Z]', re.I)
        match_1 = regex_1.match(str(data['first_name']))

        regex_2 = re.compile('[a-zA-Z]', re.I)
        match_2 = regex_2.match(str(data['last_name']))

        try:
        # if bool(match) and bool(match_1) and bool(match_2):
            response = requests.post("http://127.0.0.1:5000/department/Patient", json=data)

            if response.status_code == 200:
                print(response.text)
            else:
                messagebox.showerror("Error", response.text)
        except ValueError as err:
            messagebox.showerror(title="Invalid Value", message=err, icon="error")