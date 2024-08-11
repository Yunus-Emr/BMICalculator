import tkinter as tk


def bmi_calculate():
    height = entry_height.get()
    weight = entry_weight.get()

    try:
        _height = float(height)
        _weight = float(weight)
        _height = _height / 100

        calculate = _weight / (_height ** 2)

        if calculate < 18.5:
            label_bmi.config(text=f"Your bmi is {calculate:.2f}. You are Underweight ")
            label_bmi.place(x=50, y=220)
        elif 18.5 <= calculate <= 24.9:
            label_bmi.config(text=f"Your bmi is {calculate:.2f}. You are Normal")
            label_bmi.place(x=50, y=220)
        elif 25 <= calculate <= 29.9:
            label_bmi.config(text=f"Your bmi is {calculate:.2f}. You are Overweight")
            label_bmi.place(x=50, y=220)
        elif 30 <= calculate <= 34.9:
            label_bmi.config(text=f"Your bmi is {calculate:.2f}. You are Obese")
            label_bmi.place(x=50, y=220)
        elif 35 <= calculate <= 39.9:
            label_bmi.config(text=f"Your bmi is {calculate:.2f}. You are Severely Obese")
            label_bmi.place(x=50, y=220)
        else:
            label_bmi.config(text=f"Your bmi is {calculate:.2f}.You are Morbidly Obese")
            label_bmi.place(x=50, y=220)

    except ValueError:
        label_bmi.config(text="Please enter valid numbers")
        label_bmi.place(x=50, y=220)


def hide_label():
    label_bmi.place_forget()


window = tk.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)


label_weight = tk.Label()
label_weight.config(text="Enter Your Weight (kg)")
label_weight.place(x=86.5, y=30)

entry_weight = tk.Entry(width=18)
entry_weight.place(x=89, y=65)

label_height = tk.Label()
label_height.config(text="Enter Your Height (cm)")
label_height.place(x=86.5, y=110)

entry_height = tk.Entry(width=18)
entry_height.place(x=89, y=145)

label_bmi = tk.Label()
hide_label()

button_calculate = tk.Button(width=12, text="Calculate", command=bmi_calculate)
button_calculate.place(x=95, y=180)


window.mainloop()
