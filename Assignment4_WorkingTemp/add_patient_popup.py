import requests
import tkinter as tk
from tkinter import ttk, messagebox
import re


class AddPatientPopup(tk.Frame):
    """ Popup Frame to Add a Student """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
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
        self.date_of_birth = ttk.Entry(self)
        self.date_of_birth.grid(row=4, column=2)
        ttk.Label(self, text="Address:").grid(row=5, column=1)
        self.address = ttk.Entry(self)
        self.address.grid(row=5, column=2)
        ttk.Label(self, text="Is released:").grid(row=6, column=1)
        self.is_released = ttk.Entry(self)
        self.is_released.grid(row=6, column=2)
        ttk.Label(self, text="Room Number:").grid(row=7, column=1)
        self.room_num = ttk.Entry(self)
        self.room_num.grid(row=7, column=2)
        ttk.Label(self, text="Bill Payment:").grid(row=8, column=1)
        self.bill = ttk.Entry(self)
        self.bill.grid(row=8, column=2)

        ttk.Button(self, text="Submit", command=self._submit_cb).grid(row=9, column=1, pady=20)
        ttk.Button(self, text="Close", command=self._close_cb).grid(row=9, column=2)

    def _submit_cb(self):
        """ Submit the Add Patient button """
        data = {}
        data["first_name"] = self.first_name.get()
        data["last_name"] = self.last_name.get()
        data["date_of_birth"] = self.date_of_birth.get()
        data["address"] = self.address.get()
        # data["id"] = self.id.get()
        data["is_released"] = self.is_released.get()
        data["room_num"] = self.room_num.get()
        data["bill_payment"] = self.bill.get()

        # regex = re.compile('^[0-9]', re.I)
        # match = regex.match(str(data['id']))

        regex_1 = re.compile('[a-zA-Z]', re.I)
        match_1 = regex_1.match(str(data['first_name']))

        regex_2 = re.compile('[a-zA-Z]', re.I)
        match_2 = regex_2.match(str(data['last_name']))

        try:
        # if bool(match) and bool(match_1) and bool(match_2):
            response = requests.post("http://127.0.0.1:5000/department/Patient", json=data)
            print(response.status_code)
            print(response.text)  #test

            if response.status_code == 200:
                print(response.text)
            else:
                messagebox.showerror("Error", response.text)
        except ValueError as err:
        # else:
            """Either of them in below is all good"""
            messagebox.showerror(title="Invalid Value", message=err, icon="error")
            messagebox.showerror("Error", "Wrong Entry. Please try again!")