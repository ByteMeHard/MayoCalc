import tkinter as tk
from tkinter import messagebox

def mayyar_lateness_calculator():
    def calculate_lateness():
        try:
            initial_minutes = int(entry_initial_minutes.get()) 
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for minutes.")
            return

        # Adjustment factors
        influence_factor = 1.5  # 50% longer if Mayyar is under influence
        poop_factor = 1.2       # 20% longer if Mayyar hasn't pooped yet
        father_visiting_factor = 1.3  # 30% longer if Mayyar's father is visiting

        # Get values from checkboxes
        is_influenced = var_influenced.get()
        has_poop_today = var_poop.get()
        father_visiting = var_father_visiting.get()

        # Adjust the estimated time based on answers
        adjusted_minutes = initial_minutes * 1.1

        if is_influenced:
            adjusted_minutes *= influence_factor
        if not has_poop_today:
            adjusted_minutes *= poop_factor
        if father_visiting:
            adjusted_minutes *= father_visiting_factor

        adjusted_minutes = round(adjusted_minutes)
        messagebox.showinfo("Mayyar Lateness Estimate", f"Mayyar said he will take {initial_minutes} minutes, but considering all the factors...\nWe estimate that Mayyar will actually take around {adjusted_minutes} minutes.")

    # Create main window
    root = tk.Tk()
    root.title("Mayyar Lateness Calculator")

    # Input for initial minutes
    tk.Label(root, text="How many minutes did Mayyar say he will take?").grid(row=0, column=0, padx=10, pady=5)
    entry_initial_minutes = tk.Entry(root)
    entry_initial_minutes.grid(row=0, column=1, padx=10, pady=5)

    # Checkboxes for factors
    var_influenced = tk.BooleanVar()
    var_poop = tk.BooleanVar()
    var_father_visiting = tk.BooleanVar()

    tk.Checkbutton(root, text="Is Mayyar under influence?", variable=var_influenced).grid(row=1, column=0, columnspan=2, sticky='w', padx=10, pady=5)
    tk.Checkbutton(root, text="Has Mayyar pooped yet today?", variable=var_poop).grid(row=2, column=0, columnspan=2, sticky='w', padx=10, pady=5)
    tk.Checkbutton(root, text="Is Mayyar's father currently visiting him?", variable=var_father_visiting).grid(row=3, column=0, columnspan=2, sticky='w', padx=10, pady=5)

    # Calculate button
    tk.Button(root, text="Calculate Lateness", command=calculate_lateness).grid(row=4, column=0, columnspan=2, pady=10)

    # Run the application
    root.mainloop()

# Run the calculator
mayyar_lateness_calculator()
