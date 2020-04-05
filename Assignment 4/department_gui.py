import tkinter as tk
import tkinter.font
from tkinter import ttk, messagebox, CENTER, BOTTOM, SE, S, RIGHT

import requests
from add_patient_popup import AddPatientPopup
from add_doctor_popup import AddDoctorPopup
from remove_person_popup import RemovePersonPopup
from cal_stats_popup import CalStatsPopup


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)
        parent.title("School Administration Tool")
        # Left frame, column 1
        left_frame = tk.Frame(master=self)
        scrollbar = tk.Scrollbar(left_frame)
        left_frame.grid(row=1, column=1)
        scrollbar.pack(side=RIGHT, fill=tk.Y)
        # Right frame (info text, column 2)
        right_frame = tk.Frame(master=self)
        right_frame.grid(row=1, column=2)

        # Listbox for people
        tk.Label(left_frame, text="People list:").grid(row=1, column=1, columnspan=3)
        self._people_list = tk.Listbox(left_frame, width=25, relief="solid")
        self._people_list.grid(row=2, column=1, columnspan=3)

        # Call this on select
        self._people_list.bind("<<ListboxSelect>>", self._update_textbox)

        # Left frame widgets - using TTK
        ttk.Button(left_frame, text="Add Student", command=self._add_student).grid(row=3, column=1)
        ttk.Button(left_frame, text="Add Teacher", command=self._add_teacher).grid(row=3, column=3, pady=5)
        ttk.Button(left_frame, text="Remove Person", command=self._remove_popup)\
            .grid(row=4, column=1, pady=5, padx=5, columnspan=4)

        # Right frame widgets
        tk.Label(right_frame, text="Person Info:").grid(row=1, column=1, columnspan=4)
        self._info_text = tk.Text(master=right_frame, height=10, relief="solid",  width=40, font=("TkTextFont", 10))
        self._info_text.grid(row=2, column=1, columnspan=4, padx=15)
        self._info_text.tag_configure("bold", font=("TkTextFont", 10, "bold"))
        ttk.Button(right_frame, text="Quarantine", command=self._quarantine_cb).grid(row=3, column=2, pady=5)
        ttk.Button(right_frame, text="Release", command=self._release_cb).grid(row=3, column=3)
        ttk.Button(right_frame, text="Statistics", command=self._stats_popup)\
            .grid(row=4, column=2, pady=5, columnspan=2)

        # Bottom frame widgets
        ttk.Button(parent, text="Quit", command=self._quit_callback)\
            .place(relx=0.97, rely=0.97, anchor=SE)

        # # Now update the list
        self._update_people_list()

    def _update_textbox(self, evt):
        """ Updates the info text box on the right, based on the current ID selected """

        # This is a list, so we take just the first item (could be multi select...)
        selected_values = self._people_list.curselection()
        selected_index = selected_values[0]
        student_id = self._people_list.get(selected_index)

        # Make a GET request
        r = requests.get("http://localhost:5000/school/person/" + student_id)
        
        # Clear the text box
        self._info_text.delete(1.0, tk.END)
        
        # Check the request status code
        if r.status_code != 200:
            self._info_text.insert(tk.END, "Error running the request!")
        
        # For every item (key, value) in the JSON response, display them:
        for k, v in r.json().items():
            self._info_text.insert(tk.END, f"{k.capitalize()}\t\t", "bold")
            self._info_text.insert(tk.END, f"{v}\n")

    def _quarantine_cb(self):
        """ Set the quarantine status """
        selected_values = self._people_list.curselection()
        selected_index = selected_values[0]
        student_id = self._people_list.get(selected_index)
        response = requests.put("http://localhost:5000/school/person/" + student_id + "/quarantine")

        if response.status_code == 200:
            self._update_people_list()
        else:
            messagebox.showerror(title="API Call Error", message=response.content, icon="error")

    def _release_cb(self):
        """ Release the quarantine status of a person """
        selected_values = self._people_list.curselection()
        selected_index = selected_values[0]
        student_id = self._people_list.get(selected_index)
        response = requests.put("http://localhost:5000/school/person/" + student_id + "/release")

        if response.status_code == 200:
            self._update_people_list()
        else:
            messagebox.showerror(title="API Call Error", message=response.content, icon="error")

    def _remove_popup(self):
        """ New window for delete a person in school"""
        self._popup_win = tk.Toplevel()
        self._popup = RemovePersonPopup(self._popup_win, self._close_remove_cb)

    def _close_remove_cb(self):
        """ Close Remove Popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _stats_popup(self):
        """ New window for calculate statistics of the school """
        self._popup_win = tk.Toplevel()
        self._popup = CalStatsPopup(self._popup_win, self._close_stats_cb)

    def _close_stats_cb(self):
        """ Close Statistics Popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _add_student(self):
        """ Add Student Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddPatientPopup(self._popup_win, self._close_student_cb)

    def _close_student_cb(self):
        """ Close Add Student Popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _add_teacher(self):
        """ Add Teacher Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddDoctorPopup(self._popup_win, self._close_teacher_cb)

    def _close_teacher_cb(self):
        """ Close Add Teacher Popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _quit_callback(self):
        """ Quit """
        self.quit()

    def _update_people_list(self):
        """ Update the List of People """
        r = requests.get("http://localhost:5000/school")
        self._people_list.delete(0, tk.END)
        for s in r.json()["people"]:
            self._people_list.insert(tk.END, s['student_id'])
            if s['type'] == "teacher":
                self._people_list.itemconfig(tk.END, {'fg': 'blue'})
            if s['quarantine']:
                self._people_list.itemconfig(tk.END, {'bg': 'red'})


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")
    MainAppController(root).pack()
    root.mainloop()

