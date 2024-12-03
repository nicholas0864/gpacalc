import tkinter as tk
import time

root = tk.Tk()
root.title("GPA Calculator")
root.configure(background="black")

root_width, root_height = 800, 600
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight() 

x, y = int((screen_width/2) - (root_width/2)), int((screen_height/2) - (root_height/2))
root.geometry(f"{root_width}x{root_height}+{x}+{y}")

title_label = tk.Label(root, text="GPA Calculator", font=("Arial", 24, "bold"), fg="white", bg="black")
title_label.place(relx=0.5, rely=0.2, anchor="center")

title_label = tk.Label(root, text="Put # of classes here --------------------------------------------------->", font=("Arial", 10, "bold"), fg="white", bg="black")
title_label.place(relx=0.2, rely=0.33, anchor="center")




class_amount_entry = tk.Entry(root, font=("Arial", 16), fg="black", bg="white", width=20)
class_amount_entry.place(relx=0.5, rely=0.33, anchor="center")

def gpa_return(letter_grade_entries, honors_options, screen):
    letter_grades = [letter_grade_entry.get() for letter_grade_entry in letter_grade_entries]

    letter_to_number = { 'A':4, 'B':3,'C':2,'D':1,'NC':0,'a':4,'b':3,'c':2,'d':1,'nc':0,'Nc':0}
    number_grades = 0
    for i in letter_grades:
        number_grades += letter_to_number[i]
    number_grades += honors_options.count(True)
    number_grades /= len(letter_grades)
    
    gpa_label = tk.Label(screen, text= f'Your GPA is {number_grades:.2f}.', font=("Arial", 24, "bold"), fg="white", bg="black")
    gpa_label.place(relx=.5, rely=0.85, anchor="center")



 



def mark_class(class_idx, button):
    honors_entries[class_idx] = not honors_entries[class_idx]

    if honors_entries[class_idx] == True:
        button.config(fg = 'blue')

    if honors_entries[class_idx] == False:
        button.config(fg = 'black')

def stage_2(n_classes):
   

    grades = tk.Tk()
    grades.title("Enter Grades")
    grades.configure(background="black")
    grades_width, grades_height = 800, 600
    screen_width, screen_height = grades.winfo_screenwidth(), grades.winfo_screenheight() 
    x, y = int((screen_width/2) - (grades_width/2)), int((screen_height/2) - (grades_height/2))
    grades.geometry(f"{grades_width}x{grades_height}+{x}+{y}")

    input_label = tk.Label(grades, text="Enter your grades", font=("Arial", 20, "bold"), fg="white", bg="black")
    input_label.place(relx=0.6, rely=0.15, anchor="center")

    class_label = tk.Label(grades, text="Enter your classes", font=("Arial", 24, "bold"), fg="white", bg="black")
    class_label.place(relx=0.2, rely=0.15, anchor="center")

    honors_label = tk.Label(grades, text="Honors?", font=("Arial", 24, "bold"), fg="white", bg="black")
    honors_label.place(relx=0.8, rely=0.15, anchor="center")

    global honors_entries

    grade_entries = []
    honors_entries = [False for _ in range(n_classes)]
    
    for i in range(n_classes):
        class_entry = tk.Entry(grades, font=("Arial", 16), fg="black", bg="white", width=30)
        class_entry.place(relx=0.2, rely=0.05*(i+1)+0.15, anchor="center")

        grade_entry = tk.Entry(grades, font=("Arial", 16), fg="black", bg="white", width=5)
        grade_entry.place(relx=0.6, rely=0.05*(i+1)+0.15, anchor="center")

        grade_entries.append(grade_entry)

        honors_button = tk.Button(grades, text="Honors", font=("Arial", 13), fg="black", bg="black", width=2)
        honors_button.config(command = lambda idx=i, button = honors_button: mark_class(idx,button))
        honors_button.place(relx=0.8, rely=0.05*(i+1)+0.15, anchor="center")

        

        
    
    submit_button = tk.Button(grades, command = lambda: gpa_return(grade_entries, honors_entries, grades), text="Enter", font=("Arial", 24, "bold"), fg="green", bg="white", width=6, height=1, borderwidth=0)
    submit_button.place(relx=0.5, rely=0.90, anchor="center")




def accept_user_input() -> None:
    global class_amount

    class_amount = class_amount_entry.get()
    try:
        class_amount = int(class_amount)
        stage_2(class_amount)
        
    except:
        class_error_label = tk.Label(root, text="Error: Number of classes must be a number.", font=("Arial", 24, "bold"), fg="red", bg="black")
        class_error_label.place(relx=0.5, rely=0.5, anchor="center")
        class_amount_entry.delete(0, 'end')   
    

    

    
submit_button = tk.Button(root, command=accept_user_input, text="Enter", font=("Arial", 24, "bold"), fg="green", bg="white", width=6, height=1, borderwidth=0)
submit_button.place(relx=0.5, rely=0.48, anchor="center")


root.mainloop()
"""SYNTAX"""
"""
label = tk.Label(root, text="TEXT", font=("Arial", 24, "bold"), fg="green", bg="black")
label.place(relx=0.31, rely=0.45, anchor="center")

email_entry = tk.Entry(root, font=("Arial", 16), fg="black", bg="white", width=46)
email_entry.place(relx=0.475, rely=0.33, anchor="center")

def accept_user_input() -> None:
    global user_input
    email = email_entry.get()
    old_password = password_entry.get()

submit_button = tk.Button(root, command=accept_user_input, text="Securify", font=("Arial", 24, "bold"), fg="green", bg="white", width=6, height=1, borderwidth=0)
submit_button.place(relx=0.5, rely=0.68, anchor="center")
"""


