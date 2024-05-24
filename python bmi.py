from tkinter import *
import customtkinter
from PIL import Image, ImageTK

customtkinter.set_appearance_mode("dar")
custometkinter.set_default_color_theme("dark-pink")

root = customtkinter.CTk()

root.title('Tkinter.com - BMI Calculator')
root.iconbitmap('c:/tkinter.com/codemy.ico')
root.geometry("500x650")

#Define Our  Image
meter = ImageTk.photoImage(Image.open("images/meter2.png"))
meter_img = Label(root, image=meter, bd=0)
meter_img.pack(pady=20)

def clear_screen():
    h_entry.delete(0, END)
    w_entry.delete(0, END)
    results.config(text="")

def get_bmi():
    #calculate bmi
    #(weight_pounds/height_inches^2) *705
    our_height = int(h_entry.get()) * int(h_entry.get())
    our_weight = int(w_entry.get())
    bmi = (out_weight/our_height)*783
    bmi_rounded = round(bmi, 1)

    results.config(text=f"{str(bmi_rounded)}")

    #Logic
    if bmi_rounded < 18.5:
        results.config(text=f"{str(bmi_rounded)}\nUnderweight", text_color="#54ble1")
    elif bmi_rounded >= 18.5 and bmi_rounded <= 24.9:
      results.config(text=f"{str(bmi_rounded)}\nNormal",  text_color="#b3d686")

    elif bmi_rounded >= 25.0 and bmi_rounded <= 29.9:
      results.config(text=f"{str(bmi_rounded)}\Overweight",  text_color="#fed6429")


    elif bmi_rounded >= 30.0 and bmi_rounded <= 34.9:
      results.config(text=f"{str(bmi_rounded)}\nObese",  text_color="#fbaf42")

    elif bmi_rounded >= 35:
      results.config(text=f"{str(bmi_rounded)}\nExtreme Obese",  text_color="#bf25356")

#Define Entry Boxes
h_entry = customtkinter.CTkEntry(master=root,
   placeholder_text="Height In Inches",
   width=200,
   height=30,
   border_width=1,
   corner_radius=10)
h_entry.pack(pady=20)

w_entry = customtkinter.CTkEntry(master=root,
   placeholder_text="Weight In pounds",
   width=200,
   height=30,
   border_width=1,
   corner_radius=10)
w_entry.pack(pady=20)

#Buttons
button_1 = customtkinter.CTkButton(master=root,
      text="Calculate BMI",
      width=190,
      height=40,
      compound="top"
      command=get_bmi)
button_1.pack(pady=20)

button_2 = customtkinter.CTButton(master=root,
    text="Clear screen",
    width=190,
    height=40,
    fg_color="#D35B58",
    hover_color="#C77C78"
    command=clear_screen)
button_2.pack(pady=20)

#result
results = customtkinter.CTkLabel(master=root, text="",
    text_font=("Helvetica", 28))                  
result.pack(pady=50)

root.mainloop()






