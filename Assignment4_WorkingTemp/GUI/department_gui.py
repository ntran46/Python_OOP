import tkinter as tk
from tkinter import ttk, SE, messagebox

import requests
from GUI.add_patient_popup import AddPatientPopup
from GUI.add_doctor_popup import AddDoctorPopup
from GUI.remove_person_popup import RemovePersonPopup
from GUI.cal_stats_popup import CalStatsPopup
from GUI.update_info_popup import UpdateInfoPopup


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)
        parent.title("Department Administration Tool")
        parent.geometry('640x250')

        menuBar = tk.Menu(parent)

        # create a pull down File menu
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Add a Patient", command=self._add_patient)
        fileMenu.add_command(label="Add a Doctor", command=self._add_doctor)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=parent.quit)
        menuBar.add_cascade(label="File", menu=fileMenu)

        # create a pull down Edit menu
        editMenu = tk.Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Update person Info", command=self._update_info)
        editMenu.add_command(label="Remove a person", command=self._remove_popup)
        fileMenu.add_separator()
        editMenu.add_command(label="Get Statistics", command=self._stats_popup)
        menuBar.add_cascade(label="Edit", menu=editMenu)

        # create a pull down Help menu
        helpMenu = tk.Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About", command=self._about_popup)
        menuBar.add_cascade(label="Help", menu=helpMenu)

        # display the menu
        parent.config(menu=menuBar)

        # Left frame, column 1
        left_frame = tk.Frame(master=self)
        left_frame.grid(row=1, column=1)

        # Right frame (info text, column 2)
        right_frame = tk.Frame(master=self)
        right_frame.grid(row=1, column=2)

        # Listbox for people
        tk.Label(left_frame, text="People list:").grid(row=1, column=1, columnspan=3)
        self._people_list = tk.Listbox(left_frame, width=25, relief="solid")
        self._people_list.grid(row=2, column=1, columnspan=3)

        # Call this on select
        self._people_list.bind("<<ListboxSelect>>", self._update_textbox)

        # Right frame widgets
        tk.Label(right_frame, text="Person Info:").grid(row=1, column=1, columnspan=4)
        self._info_text = tk.Text(master=right_frame, height=10, relief="solid",  width=60, font=("TkTextFont", 10))
        self._info_text.grid(row=2, column=1, columnspan=4, padx=15, rowspan=2)
        self._info_text.tag_configure("bold", font=("TkTextFont", 10, "bold"))

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
        person_id = self._people_list.get(selected_index)

        # Make a GET request
        r = requests.get("http://localhost:5000/department/person/" + person_id)

        # Clear the text box
        self._info_text.delete(1.0, tk.END)
        
        # Check the request status code
        if r.status_code != 200:
            self._info_text.insert(tk.END, "Error running the request!")
        
        # For every item (key, value) in the JSON response, display them:
        for k, v in r.json().items():
            self._info_text.insert(tk.END, f"{k.capitalize()}\t\t", "bold")
            self._info_text.insert(tk.END, f"{v}\n")

    def _about_popup(self):
        """ Show about popup"""
        self._popup_win = tk.Toplevel()
        self._popup_win.title("About")
        self._popup_win.geometry('400x150')
        aboutText = "British Columbia Institute of Technology - Winter 2020\n\n" \
                    "Class ACIT2515 - Assignment 4  \n\n" \
                    "Group 13 - Set 2C\n\n" \
                    "Ngoc Kha Uy Tran - A01073093 \nMahsa Taer - A01081561"
        ttk.Label(self._popup_win, text=aboutText).grid(row=1, column=1, padx=10)

    def _update_info(self):
        """ Modify person information """
        selected_values = self._people_list.curselection()
        selected_index = selected_values[0]
        person_id = self._people_list.get(selected_index)
        self._update_info_cb(person_id)
        self._update_people_list()

    def _update_info_cb(self, person_id):
        """ Update information Popup """
        self._popup_win = tk.Toplevel()
        self._popup = UpdateInfoPopup(self._popup_win, self._close_update_info_cb, person_id)

    def _close_update_info_cb(self):
        """ Close Update information Popup """
        self._popup_win.destroy()
        self._update_people_list()

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

    def _add_patient(self):
        """ Add Patient Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddPatientPopup(self._popup_win, self._close_patient_cb)

    def _close_patient_cb(self):
        """ Close Add Patient Popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _add_doctor(self):
        """ Add Doctor Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddDoctorPopup(self._popup_win, self._close_doctor_cb)

    def _close_doctor_cb(self):
        """ Close Add Doctor Popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _quit_callback(self):
        """ Quit """
        self.quit()

    def _update_people_list(self):
        """ Update the List of People """
        r = requests.get("http://localhost:5000/department/person/all")
        self._people_list.delete(0, tk.END)

        for s in r.json()["Doctor"]:
            self._people_list.insert(tk.END, s['id'])
            self._people_list.itemconfig(tk.END, {'fg': 'blue'})
        for s in r.json()["Patient"]:
            self._people_list.insert(tk.END, s['id'])
            self._people_list.itemconfig(tk.END, {'fg': 'red'})
            if s['is_released'] == 'True':
                self._people_list.itemconfig(tk.END, {'bg': 'yellow'})


if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack()
    root.mainloop()
