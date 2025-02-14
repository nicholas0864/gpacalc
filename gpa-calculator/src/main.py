import tkinter as tk

def setup_root_window():
    root = tk.Tk()
    root.title("GPA Calculator")
    root.configure(background="#2c3e50")

    root_width, root_height = 800, 600
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight() 
    x, y = int((screen_width/2) - (root_width/2)), int((screen_height/2) - (root_height/2))
    root.geometry(f"{root_width}x{root_height}+{x}+{y}")

    return root

def create_title_labels(root):
    title_label = tk.Label(root, text="GPA Calculator", font=("Helvetica", 24, "bold"), fg="#ecf0f1", bg="#2c3e50")
    title_label.place(relx=0.5, rely=0.2, anchor="center")

    instruction_label = tk.Label(root, text="Enter the number of classes below:", font=("Helvetica", 12), fg="#ecf0f1", bg="#2c3e50")
    instruction_label.place(relx=0.5, rely=0.3, anchor="center")

def create_class_amount_entry(root):
    class_amount_entry = tk.Entry(root, font=("Helvetica", 16), fg="#2c3e50", bg="#ecf0f1", width=10, relief="solid", borderwidth=1)
    class_amount_entry.place(relx=0.5, rely=0.4, anchor="center")
    return class_amount_entry

def gpa_return(letter_grade_entries, honors_options, screen):
    letter_grades = [entry.get() for entry in letter_grade_entries]
    letter_to_number = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'NC': 0, 'a': 4, 'b': 3, 'c': 2, 'd': 1, 'nc': 0, 'Nc': 0}
    
    number_grades = sum(letter_to_number.get(grade, 0) for grade in letter_grades)
    number_grades += honors_options.count(True)
    number_grades /= len(letter_grades)
    
    gpa_label = tk.Label(screen, text=f'Your GPA is {number_grades:.2f}.', font=("Helvetica", 24, "bold"), fg="#ecf0f1", bg="#2c3e50")
    gpa_label.place(relx=0.5, rely=0.85, anchor="center")

def mark_class(class_idx, button):
    honors_entries[class_idx] = not honors_entries[class_idx]
    button.config(fg='#3498db' if honors_entries[class_idx] else '#2c3e50')

def stage_2(n_classes):
    grades = tk.Tk()
    grades.title("Enter Grades")
    grades.configure(background="#2c3e50")
    
    grades_width, grades_height = 800, 600
    screen_width, screen_height = grades.winfo_screenwidth(), grades.winfo_screenheight() 
    x, y = int((screen_width/2) - (grades_width/2)), int((screen_height/2) - (grades_height/2))
    grades.geometry(f"{grades_width}x{grades_height}+{x}+{y}")

    create_stage_2_labels(grades)
    grade_entries, honors_entries = create_grade_entries(grades, n_classes)
    
    submit_button = tk.Button(grades, command=lambda: gpa_return(grade_entries, honors_entries, grades), text="Enter", font=("Helvetica", 16, "bold"), fg="#2c3e50", bg="#ecf0f1", width=10, height=1, relief="solid", borderwidth=1)
    submit_button.place(relx=0.5, rely=0.90, anchor="center")

def create_stage_2_labels(grades):
    input_label = tk.Label(grades, text="Enter your grades", font=("Helvetica", 20, "bold"), fg="#ecf0f1", bg="#2c3e50")
    input_label.place(relx=0.6, rely=0.15, anchor="center")

    class_label = tk.Label(grades, text="Enter your classes", font=("Helvetica", 24, "bold"), fg="#ecf0f1", bg="#2c3e50")
    class_label.place(relx=0.2, rely=0.15, anchor="center")

    honors_label = tk.Label(grades, text="Honors?", font=("Helvetica", 24, "bold"), fg="#ecf0f1", bg="#2c3e50")
    honors_label.place(relx=0.8, rely=0.15, anchor="center")

def create_grade_entries(grades, n_classes):
    grade_entries = []
    global honors_entries
    honors_entries = [False for _ in range(n_classes)]
    
    for i in range(n_classes):
        class_entry = tk.Entry(grades, font=("Helvetica", 16), fg="#2c3e50", bg="#ecf0f1", width=30, relief="solid", borderwidth=1)
        class_entry.place(relx=0.2, rely=0.05*(i+1)+0.15, anchor="center")

        grade_entry = tk.Entry(grades, font=("Helvetica", 16), fg="#2c3e50", bg="#ecf0f1", width=5, relief="solid", borderwidth=1)
        grade_entry.place(relx=0.6, rely=0.05*(i+1)+0.15, anchor="center")
        grade_entries.append(grade_entry)

        honors_button = tk.Button(grades, text="Honors", font=("Helvetica", 13), fg="#2c3e50", bg="#ecf0f1", width=6, relief="solid", borderwidth=1)
        honors_button.config(command=lambda idx=i, button=honors_button: mark_class(idx, button))
        honors_button.place(relx=0.8, rely=0.05*(i+1)+0.15, anchor="center")

    return grade_entries, honors_entries

def accept_user_input(class_amount_entry):
    global class_amount
    class_amount = class_amount_entry.get()
    try:
        class_amount = int(class_amount)
        stage_2(class_amount)
    except ValueError:
        class_error_label = tk.Label(root, text="Error: Number of classes must be a number.", font=("Helvetica", 24, "bold"), fg="#e74c3c", bg="#2c3e50")
        class_error_label.place(relx=0.5, rely=0.5, anchor="center")
        class_amount_entry.delete(0, 'end')

if __name__ == "__main__":
    root = setup_root_window()
    create_title_labels(root)
    class_amount_entry = create_class_amount_entry(root)

    submit_button = tk.Button(root, command=lambda: accept_user_input(class_amount_entry), text="Enter", font=("Helvetica", 16, "bold"), fg="#2c3e50", bg="#ecf0f1", width=10, height=1, relief="solid", borderwidth=1)
    submit_button.place(relx=0.5, rely=0.48, anchor="center")

    root.mainloop()