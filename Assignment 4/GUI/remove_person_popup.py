import requests
import tkinter as tk
from tkinter import ttk, messagebox
import re


class RemovePersonPopup(tk.Frame):
    """ Popup Frame to remove a person """

    ID_REGEXP = r"(^D|^P)\d+$"

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        parent.title("Remove a Person")
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2, padx=30, pady=30)

        ttk.Label(self, text="Enter Person ID: ").grid(row=1, column=1)
        self._person_id = ttk.Entry(self)
        self._person_id.grid(row=1, column=2)
        ttk.Button(self, text="Remove", command=self._confirm_popup).grid(row=4, column=1, pady=20)

        ttk.Button(self, text="Close", command=self._close_cb).grid(row=4, column=2)

    def _remove_person(self):
        """ Remove selected person"""
        response = requests.delete("http://localhost:5000/department/person/" + self._person_id.get())
        if response.status_code == 200:
            messagebox.showinfo("Accomplished", "Removed action completed")
            self._close_cb()
        else:
            messagebox.showerror(title="API Call Error", message=response.content, icon="error")

    def _confirm_popup(self):
        """ Show confirmation message """
        if not re.match(self.ID_REGEXP, self._person_id.get()):
            messagebox.showinfo(title="Invalid Value", message="Invalid Person ID: " + self._person_id.get())
        else:
            data = self._get_id()
            if self._person_id.get()[0:1] == 'P':
                _type = "Patient"
            else:
                _type = "Doctor"
            message = f"Do you want to remove this {_type}? \n\n" \
                      f" Name: {data['first_name']} {data['last_name']} \n" \
                      f" Person ID: {data['id']}\n" \
                      f" Date of Birth: {data['date_of_birth']}\n" \
                      f" Address: {data['address']}" \
                      f"\n\n Caution: This action could not be undone "
            MsgBox = tk.messagebox.askquestion('Confirm Action', message,
                                               icon='warning')
            if MsgBox == 'yes':
                self._remove_person()
                messagebox.showinfo("Confirmation", f"Person record (ID: {data['id']})"
                                                    f" has been removed successfully.", icon="info")

    def _get_id(self):
        """ Get information of selected person"""
        data = {}
        response = requests.get("http://localhost:5000/department/person/" + self._person_id.get())
        if response.status_code != 200:
            messagebox.showerror(title="API Call Error", message=response.content, icon="error")
        else:
            for key, value in response.json().items():
                data[key] = value
        return data
