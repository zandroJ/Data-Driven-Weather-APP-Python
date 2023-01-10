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
        
        condition_images = { #stores the both the matching text and imgs on a dict
            "Clear": "sunny.png",
            "Clouds": "cloud.png",
            "Rain": "rain.png",
            "Snow": "cloud.png",
            "Thunderstorm": "thunderstorm.png",
            "Fog": "cloud.png",
            "Haze": "haze.png",
        }

        # Get the file path for the current weather condition
        image_file = condition_images.get(condition) #get condition and match it correspondingly
        image = Image.open(image_file)
        image_tk = ImageTk.PhotoImage(image)

        # Open and display the image
        image_label.config(image=image_tk)
        image_label.image = image_tk
        image_label.place(x=10,y=120)
    except Exception:
        messagebox.showerror("Weather App", "Invalid Input!")


api_key = '30d4741c779ba94c470ca1f63045390a'

gui = tk.Tk()
gui.geometry("500x600")
gui.title("Weather App")
gui.resizable(False, False) #makes it impossible to resize for both x y
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

# Logo default state, will later get overlapped by weather condition.
logo_img = Image.open("logo.png")
resize_image = logo_img.resize((200, 200))
logo_image_resized = ImageTk.PhotoImage(resize_image)
logo = Label(image=logo_image_resized)
logo.size
logo.place(x=50, y=150)

# Image label to display weather image
image_label = Label(gui)
image_label.place(x=50, y=100)

#labels for texts
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

# Default state text values
wind = Label(text="....", font=("Times New Roman", 18, "bold") )
wind.place(x=370, y=200,anchor=CENTER)
humidity = Label(text="....", font=("Times New Roman", 18, "bold") )
humidity.place(x=370, y=300,anchor=CENTER)
pressure = Label(text="....", font=("Times New Roman", 18, "bold") )
pressure.place(x=370, y=400,anchor=CENTER)

# Window position
window_width = gui.winfo_reqwidth()
window_height = gui.winfo_reqheight()

# Centers the window on the screen
position_right = int(gui.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(gui.winfo_screenheight() / 2 - window_height / 2)

# Positions the window on the screen
gui.geometry(f"+{position_right}+{position_down}")

# App loop
gui.mainloop()

