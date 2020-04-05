import tkinter as tk
from tkinter import ttk, messagebox
import requests


class AddDoctorPopup(tk.Frame):
    """ Popup Frame to Add a Doctor """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        parent.title("Add a Doctor")
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2, padx=30, pady=30)

        ttk.Label(self, text="Doctor Name:").grid(row=1, column=1)
        self._name = ttk.Entry(self)
        self._name.grid(row=1, column=2)
        ttk.Label(self, text="Doctor ID:").grid(row=2, column=1)
        self._person_id = ttk.Entry(self)
        self._person_id.grid(row=2, column=2)
        ttk.Label(self, text="Room").grid(row=3, column=1)
        self._room = ttk.Entry(self)
        self._room.grid(row=3, column=2)
        ttk.Button(self, text="Submit", command=self._submit_cb).grid(row=4, column=1, pady=20)
        ttk.Button(self, text="Close", command=self._close_cb).grid(row=4, column=2)

    def _submit_cb(self):
        """ Submit the Add Doctor button """
        data = {}
        data['name'] = self._name.get()
        data['person_id'] = self._person_id.get()
        data['room'] = self._room.get()
        try:
            response = requests.post("http://localhost:5000/department/doctor", json=data)
            print(response.text)
            if response.status_code == 200:
                # print(response.json())
                self._close_cb()
            else:
                messagebox.showerror(title="API Call Error", message=response.content, icon="error")
        except ValueError as err:
            messagebox.showerror(title="Invalid Value", message=err, icon="error")



