import requests
import tkinter as tk
from tkinter import ttk, messagebox
import re
from tkcalendar import DateEntry


class UpdateInfoPopup(tk.Frame):
    """ Popup Frame to Add a Doctor """

    def __init__(self, parent, close_callback, person_id):
        """ Constructor """
        self.person_id = person_id
        tk.Frame.__init__(self, parent)
        parent.title("Update information")
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2, padx=30, pady=30)

        ttk.Label(self, text="ID:").grid(row=1, column=1)
        ttk.Label(self, text=person_id).grid(row=1, column=2)

        response = requests.get("http://localhost:5000/department/person/" + person_id)
        if response.status_code == 200:
            data = response.json()
        else:
            messagebox.showerror(title="API Call Error", message=response.content, icon="error")

        ttk.Label(self, text="First Name:").grid(row=2, column=1)
        self.first_name = ttk.Entry(self, width=35)
        self.first_name.grid(row=2, column=2)
        self.first_name.insert(0, data['first_name'])

        ttk.Label(self, text="Last Name:").grid(row=3, column=1)
        self.last_name = ttk.Entry(self, width=35)
        self.last_name.grid(row=3, column=2)
        self.last_name.insert(0, data['last_name'])

        ttk.Label(self, text="Address:").grid(row=5, column=1)
        self.address = ttk.Entry(self, width=35)
        self.address.grid(row=5, column=2)
        self.address.insert(0, data['address'])

        if self.person_id[0:1] == 'P':
            ttk.Label(self, text="Room Number:").grid(row=7, column=1)
            self.office_room_num = ttk.Entry(self, width=35)
            self.office_room_num.grid(row=7, column=2)
            self.office_room_num.insert(0, data['room_num'])

            ttk.Label(self, text="Bill Payment:").grid(row=8, column=1)
            self.bill_income = ttk.Entry(self, width=35)
            self.bill_income.grid(row=8, column=2)
            self.bill_income.insert(0, data['bill'])
        else:
            ttk.Label(self, text="Office Number:").grid(row=7, column=1)
            self.office_room_num = ttk.Entry(self, width=35)
            self.office_room_num.grid(row=7, column=2)
            self.office_room_num.insert(0, data['office_num'])

            ttk.Label(self, text="Income:").grid(row=8, column=1)
            self.bill_income = ttk.Entry(self, width=35)
            self.bill_income.grid(row=8, column=2)
            self.bill_income.insert(0, data['income'])

        ttk.Button(self, text="Submit", command=self._submit_cb).grid(row=9, column=1, pady=20)
        ttk.Button(self, text="Close", command=self._close_cb).grid(row=9, column=2)

    def _submit_cb(self):
        """ Submit the Add Doctor button """
        if self.person_id[0:1] == 'P':
            person_type = "Patient"
        else:
            person_type = "Doctor"

        data = {}
        data["first_name"] = self.first_name.get()
        data["last_name"] = self.last_name.get()
        data["address"] = self.address.get()
        try:
            data["office_room_num"] = int(self.office_room_num.get())
            data["bill_income"] = int(self.bill_income.get())
        except TypeError:
            messagebox.showerror("Warning", "Office number or Money amount must be greater than or equal 0,"
                                            " and they are an integer", icon="warning")

        try:
            response = requests.put("http://127.0.0.1:5000/department/person/"
                                    + person_type + "/" + self.person_id, json=data)

            if response.status_code == 200:
                messagebox.showinfo("Confirmation", response.text, icon="info")
            else:
                messagebox.showerror("Error", response.text, icon="error")
        except ValueError as err:
            messagebox.showerror(title="Invalid Value", message=err, icon="error")
