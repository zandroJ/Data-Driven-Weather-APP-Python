import requests
from tkinter import * #sus
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def weather():
    try:
        city = textfield.get()
        #API weather
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" #concatonating city for input
        data = requests.get(api).json()
        condition = data["weather"][0]["main"]
        tempt = int(data["main"]["temp"] - 273.15)
        feels_like = int(data["main"]["feels_like"] - 273.15) #subtracting to convert fahr to cels
        press = data["main"]["pressure"]
        humid = data["main"]["humidity"]
        wind_1 = int(data["wind"]["speed"] * 1.609) #converting miles to km
        temp_info.config(text=(tempt, "°C"))
        condition_info.config(text=(condition, "|", "FEELS", "LIKE", feels_like, "°C"))
        wind.config(text=(wind_1,"km/h"))
        humidity.config(text=(humid,"%"))
        pressure.config(text=(press,"mbar"))
    except Exception:
        messagebox.showerror("Weather App", "Invalid Input!")


api_key = '30d4741c779ba94c470ca1f63045390a'

gui = tk.Tk()
gui.geometry("500x600")
gui.title("Weather App")
gui.resizable(False, False) #makes it impossible to resize for both x  y

# Search bar
search_bar = PhotoImage(file="search.png")
search = Label(image=search_bar)
search.place(x=20, y=20)


textfield = tk.Entry(
    gui,
    width=21,
    justify="left",
    bg="#404040",
    fg="white",
    border=0,
    font=("Times New Roman", 24, "bold")
)
textfield.place(x=100,y=40)
textfield.focus()

# enter button function
btn_invis = Button(
    command=weather
)
gui.bind('<Return>',lambda event:weather())

# Logo
logo_img = Image.open("logo.png")
# Resize the image using resize() method
resize_image = logo_img.resize((250, 250))
logo_image_resized = ImageTk.PhotoImage(resize_image)
logo = Label(image=logo_image_resized)
logo.size
logo.place(x=40, y=150)

#labels
label_info_wind = Label(gui, text="WIND", font=("Georgia", 20, "bold"), fg="black")
label_info_wind.place(x=340, y=150)

label_info_humid = Label(gui, text="HUMIDITY", font=("Georgia", 20, "bold"), fg="black")
label_info_humid.place(x=305, y=250)

label_info_pressure = Label(gui, text="PRESSURE", font=("Georgia", 20, "bold"), fg="black")
label_info_pressure.place(x=305, y=350)

# weather condition and temperature
temp_info = Label(font=("Times New Roman", 40, "bold"), fg="#ee666d")
temp_info.place(x=50, y=410)
condition_info = Label(font=("Times New Roman", 16, "bold"))
condition_info.place(x=50, y=470)

# Default state values
wind = Label(text="....", font=("Times New Roman", 18, "bold") )
wind.place(x=370, y=200,anchor=CENTER)
humidity = Label(text="....", font=("Times New Roman", 18, "bold") )
humidity.place(x=370, y=300,anchor=CENTER)
pressure = Label(text="....", font=("Times New Roman", 18, "bold"))
pressure.place(x=370, y=400,anchor=CENTER)

gui.mainloop()