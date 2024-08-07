import tkinter
from tkinter import ttk
from tkinter import messagebox

#ttk --> collection of themed widgets

def enter_data():

    accepted = accept_var.get()

    if accepted=="Accepted" :

        #User Info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        mailid = mail_id_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            #Courses info
            registration_status = reg_status_var.get()
            courses = courses_spinbox.get()
            semesters = semesters_spinbox.get()

            print("First name: ", firstname, "Last name: ", lastname, "MailID :",    mailid)
            print("Title : ", title, "Age:", age,"Nationality: ", nationality)
            print("# Courses:",courses, "#Semesters:",semesters)
           # print("Registration status",registration_status)
            print("--------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Error",message = "First name, last name & Email are required")

    else:
      tkinter.messagebox.showwarning(title ="Error" , message="Please accept the terms")


window = tkinter.Tk()
window.title("Registration form")

#Style
style=ttk.Style()
style.theme_use("clam")
window.configure(background="violet",padx=30, pady=30)


#frame is inside root window
frame = tkinter.Frame(window)
frame.pack()

#Saving user information
user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row=0,column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text = "First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text = "Last Name")
last_name_label.grid(row=0, column=1)
mail_id_label = tkinter.Label(user_info_frame, text = "Email")
mail_id_label.grid(row=0, column=3)


first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
mail_id_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)
mail_id_entry.grid(row =1, column=3)


title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr.","Ms.","Dr."])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=100)
age_label.grid(row=2, column = 0)
age_spinbox.grid(row=3, column = 0)

nationality_label = tkinter.Label(user_info_frame, text ="Nationality" )
nationality_combobox = ttk.Combobox(user_info_frame, values = ["Africa","Antartica","Asia","Europe","North America","South America",])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3, column=1)

#For cleaner padding at once
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Saving Course info
courses_frame =  tkinter.LabelFrame(frame)
courses_frame.grid(row = 1, column = 0, sticky = "news", padx=20, pady=10)
#news: expand with respect to padding

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text = "Currently Registered", variable = reg_status_var,onvalue="Registered", offvalue="Not registered")
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

courses_label = tkinter.Label(courses_frame, text="# Completed Courses")
courses_spinbox = tkinter.Spinbox(courses_frame, from_=0,to="infinity")
courses_label.grid(row=0,column=1)
courses_spinbox.grid(row=1, column=1)

semesters_label = tkinter.Label(courses_frame, text= "# Semesters")
semesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
semesters_label.grid(row=0, column=2)
semesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Terms and conditions
terms_frame = tkinter.LabelFrame(frame, text = "Terms & Conditions")
terms_frame.grid(row = 2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value = "Not Accepted")

#To not accept the form if not checked with terms & conditions
terms_check = tkinter.Checkbutton(terms_frame, text = "I accept the terms and conditions.",
                                variable=accept_var, onvalue="Accepted", offvalue = "Not Accepted")
terms_check.grid(row=0, column = 0)

#Submit button
#Command: When button is clicked, execute the data
button = tkinter.Button(frame, text = "Submit", command = enter_data)
button.grid(row=3, column = 0, sticky = "news", padx=20, pady=10)

window.mainloop()
