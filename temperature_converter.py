import customtkinter as ctk

def convert_temperature():
    choice = selected_value.get()
    if choice == "C":
        convert_to_celsius()
    else:
        convert_to_fahrenheit()

def convert_to_celsius():
    fahrenheit  = float(temp_entry.get())
    celcius = (fahrenheit - 32) * 5.0/9.0
    celcius_text = f"{celcius:.2f} °C"
    result_label.configure(text=celcius_text, text_color="green", font = ctk.CTkFont(size=20, weight="bold"))

def convert_to_fahrenheit():
    celcius = float(temp_entry.get())
    fahrenheit = (celcius * 9.0/5.0) + 32
    fahrenheit_text = f"{fahrenheit:.2f} °F"
    result_label.configure(text=fahrenheit_text, text_color="blue", font = ctk.CTkFont(size=20, weight="bold"))


window = ctk.CTk()
ctk.set_appearance_mode("dark")
window.geometry("600x400")

window.title("Temperature Converter")

title_label = ctk.CTkLabel(window, text="Temperature Converter", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(30,20))

radio_Frame = ctk.CTkFrame(window)
radio_Frame.pack(fill="x", padx=50)

selected_value = ctk.StringVar(value="C")

radio_FtoC = ctk.CTkRadioButton(radio_Frame, text="Fahrenheit to Celsius", variable = selected_value, value="C")
radio_FtoC.pack(side="left", padx=(80,10), pady=10)


radio_CtoF = ctk.CTkRadioButton(radio_Frame, text="Celsius to Fahrenheit", variable = selected_value, value="F")
radio_CtoF.pack(side="left", padx=10, pady=10)

input_Frame = ctk.CTkFrame(window)
input_Frame.pack(fill="x", padx=50, pady=(20,10))

temp_entry = ctk.CTkEntry(input_Frame, placeholder_text="Enter Temperature")
temp_entry.pack(side="left", padx=(80,10), pady=20)

convert_button = ctk.CTkButton(input_Frame, text="Convert", command=convert_temperature)
convert_button.pack(side="left", padx=10, pady=20)


result_Frame  = ctk.CTkFrame(window)
result_Frame.pack(fill="x", padx=50)

result_label = ctk.CTkLabel(result_Frame, text="", font=ctk.CTkFont(size=20))
result_label.pack(padx=10, pady=20)


window.mainloop()