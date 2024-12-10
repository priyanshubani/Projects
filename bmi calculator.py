import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time


def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI) based on weight and height.
    Returns the calculated BMI value.
    """
    return weight / (height ** 2)


def get_bmi_category(bmi):
    """
    Determines the BMI category based on the BMI value.
    Returns the BMI category as a string.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_weight_range(height):
    """
    Provides a suggested weight range based on height.
    Returns a tuple containing the lower and upper weight limits.
    """
    lower_limit = 18.5 * (height ** 2)
    upper_limit = 24.9 * (height ** 2)
    return lower_limit, upper_limit


def get_height_range(weight):
    """
    Provides a suggested height range based on weight.
    Returns a tuple containing the lower and upper height limits.
    """
    lower_limit = (weight / 24.9) ** 0.5
    upper_limit = (weight / 18.5) ** 0.5
    return lower_limit, upper_limit


def animate_widget(widget, animation, duration=0.1, repeat=5):
    """
    Animates a tkinter widget by repeatedly applying a sequence of styles.
    """
    for _ in range(repeat):
        for style, value in animation:
            widget.configure(**{style: value})
            root.update()
            time.sleep(duration)


def calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight_unit_var.get() == "lbs":
            weight = weight * 0.453592

        if height_unit_var.get() == "feet":
            height = height * 0.3048

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        bmi_category = get_bmi_category(bmi)

        bmi_label.config(text=f"BMI: {bmi:.2f}")
        category_label.config(text=f"Category: {bmi_category}")

        weight_range = get_weight_range(height)
        height_range = get_height_range(weight)

        weight_range_label.config(
            text=f"Suggested Weight Range: {weight_range[0]:.2f} - {weight_range[1]:.2f} kg"
        )
        height_range_label.config(
            text=f"Suggested Height Range: {height_range[0]:.2f} - {height_range[1]:.2f} meters"
        )

        animate_widget(calculate_button, [("background", "green"), ("background", "#4CAF50")])

    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")


def exit_app():
    root.quit()


# Main application window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# Apply modern ttk theme
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=6)
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))

# Main frame
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True, fill="both")

# Input fields
ttk.Label(main_frame, text="Weight:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
weight_entry = ttk.Entry(main_frame)
weight_entry.grid(row=0, column=1, padx=5)

weight_unit_var = tk.StringVar(value="kgs")
weight_unit_combo = ttk.Combobox(main_frame, textvariable=weight_unit_var, values=("kgs", "lbs"), state="readonly", width=5)
weight_unit_combo.grid(row=0, column=2, padx=5)

ttk.Label(main_frame, text="Height:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
height_entry = ttk.Entry(main_frame)
height_entry.grid(row=1, column=1, padx=5)

height_unit_var = tk.StringVar(value="meters")
height_unit_combo = ttk.Combobox(main_frame, textvariable=height_unit_var, values=("meters", "feet"), state="readonly", width=5)
height_unit_combo.grid(row=1, column=2, padx=5)

# Buttons
calculate_button = ttk.Button(main_frame, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=3, pady=10)

exit_button = ttk.Button(main_frame, text="Exit", command=exit_app)
exit_button.grid(row=3, column=0, columnspan=3, pady=10)

# Output labels
bmi_label = ttk.Label(main_frame, text="BMI: ")
bmi_label.grid(row=4, column=0, columnspan=3, sticky="w", padx=5, pady=5)

category_label = ttk.Label(main_frame, text="Category: ")
category_label.grid(row=5, column=0, columnspan=3, sticky="w", padx=5, pady=5)

weight_range_label = ttk.Label(main_frame, text="Suggested Weight Range: ")
weight_range_label.grid(row=6, column=0, columnspan=3, sticky="w", padx=5, pady=5)

height_range_label = ttk.Label(main_frame, text="Suggested Height Range: ")
height_range_label.grid(row=7, column=0, columnspan=3, sticky="w", padx=5, pady=5)

root.mainloop()
