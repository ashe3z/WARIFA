# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 09:56:24 2021

@author: Ashenafi
"""

import tkinter as tk
from tkinter import *
import tkinter.messagebox
import requests, json

from tkinter import ttk
from tkinter import StringVar

import math
# import base64, PIL, urllib
import urllib
# from PIL import ImageTk
# from urllib import *
import urllib.request



global geolat
global geolon
api_key = "Your API key, Get one from the Openweather page"

def get_weathers():
    city_name= entry_usercity.get()
   
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    
    response = requests.get(url).json()
    temp = response['main']['temp']
    temprature = temp-273.15
    
    feels_like = response['main']['feels_like']
    feels_like = feels_like-273.15
    
    humidity = response['main']['humidity']
    
    geolon = response['coord']['lon']
    geolat = response['coord']['lat']
    
    urlairpol = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={geolat}&lon={geolon}&appid={api_key}'

    response = requests.get(urlairpol).json()
    AQI = response['list'][0]['main']['aqi']
    CO = response['list'][0]['components']['co']
    NO = response['list'][0]['components']['no']
    NO2 = response['list'][0]['components']['no2']
    O3 = response['list'][0]['components']['o3']
    SO2 = response['list'][0]['components']['so2']
    PM2_5 = response['list'][0]['components']['pm2_5']
    PM10 = response['list'][0]['components']['pm10']
    NH3 = response['list'][0]['components']['nh3']
    
   
     
    urlsolar = f'https://api.openweathermap.org/data/2.5/onecall?lat={geolat}&lon={geolon}&appid={api_key}'
    response = requests.get(urlsolar).json()

    UvI = response['current']['uvi']
    Pressure = response['current']['pressure']
    Cloud = response['current']['clouds']
    timezoneoffset = response['timezone_offset']
    timezone = response['timezone']
    visibility = response['current']['visibility'] 
    windspeed= response['current']['wind_speed'] 
    wind_deg= response['current']['wind_deg']
    dewpoint = response['current']['dew_point']
    weatherdescription = response['current']['weather'][0]['description']
    weathericon = response['current']['weather'][0]['icon']
    
    with urllib.request.urlopen(f'http://openweathermap.org/img/wn/{weathericon}@2x.png') as url:
        raw_data11 = url.read()
        image11 = PhotoImage(data=raw_data11)
    
    ### Update labeles values
    labelweather.config(text =f"Temprature: {math.floor(temprature)} Degree celcius")
    labelweatherhumid.config(text =f"Humidity: {humidity} %")
    labelweatherfeel.config(text =f"Feels like: {math.floor(feels_like)} Degree celcius")
    labelairpolution.config(text =f"Air Quality: {math.floor(AQI)}")
    labelairpolution2.config(text =f"Carbon monoxide: {math.floor(CO)} μg/m3")
    labelairpolution3.config(text =f"Nitrogen monoxide: {math.floor(NO)} μg/m3")
    labelairpolution4.config(text =f"Nitrogen dioxide: {math.floor(NO2)} μg/m3")
    labelairpolution5.config(text =f"Ozone: {math.floor(O3)} μg/m3")
    labelairpolution6.config(text =f"Sulphur dioxide: {math.floor(SO2)} μg/m3")
    labelairpolution7.config(text =f"Fine particles matter: {math.floor(PM2_5)} μg/m3")
    labelairpolution8.config(text =f"Coarse particulate matter: {math.floor(PM10)} μg/m3")
    labelairpolution9.config(text =f"Ammonia: {math.floor(NH3)} μg/m3")
    labelsolar.config(text =f"UVI Index: {UvI} Midday")
    labelsolar2.config(text =f"Cloud: {Cloud} %")
    labelsolar3.config(text =f"Pressure: {Pressure} hPa")
    labelsolar4.config(text =f"Visibility: {visibility} Average, metres")
    labelsolar5.config(text =f"Windspeed: {windspeed} metre/sec")
    labelsolar6.config(text =f"Wind direction: {wind_deg} degrees")
    labelsolar7.config(text =f"Dewpoint: {dewpoint} kelvin")
    labelsolar8.config(text =f"Weather description: {weatherdescription}")
    label_timezone.config(text =f"City Name: {city_name}")
    label_timezone2.config(text =f"Timezone: {timezone, (timezoneoffset/(60*60))} UTC")
    labelsolar9.config(image =image11)
    labelsolar9.image = image11


############################ Main Task
global fontExample 
fontExample = ("Courier", 20, "bold")
root = tk.Tk()
root.title("WARIFA APP")
user_city = StringVar()
countrys = StringVar()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

#Notebook adding tabs
mygreen = "#d2ffd2"
myred = "#ccffff"
s = ttk.Style()

s.theme_create( "maffinman", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [1, 2, 1, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [100, 1], "background": mygreen,
                                        "font" : ('URW Gothic L', '20', 'bold')},
                          "map":{"background": [("selected", myred)],"expand": [("selected", [1, 1, 1, 0])] }}})
s.theme_use("maffinman")
############################ creat the sheet
my_notebook =ttk.Notebook(root, height =HEIGHT, width = WIDTH)
my_notebook.pack()
sheet1 = tk.Frame(my_notebook)
sheet1.pack(fill="both",expand=True)
my_notebook.add(sheet1, text="Home")

######## adding background impage to home screen
background_image =  tk.PhotoImage(file='C:/Users/Ashenafi/Documents/phytoncourse/Warifa-colours-noclaim.png')
background_label = tk.Label(sheet1, image=background_image)
background_label.place(relwidth=1,relheight=1)

# ######## user entry
frame_usercity = tk.Frame(sheet1,bg = '#80c1ff', bd=7)
frame_usercity.place(relx=0.5, rely=0.05,relwidth=0.55, relheight=0.1, anchor = 'n')
label_usercity = tk.Label(frame_usercity,text="City", font=('bold',25),justify= 'left',bd=17 )
label_usercity.place(relx=0.05, rely=0.12,relwidth = 0.25, relheight=0.5)

entry_usercity=tk.Entry(sheet1,textvariable=user_city,font=('bold',25))
entry_usercity.place(relx=0.40, rely=0.067,relwidth = 0.25, relheight=0.045)

Submit_button = tk.Button(frame_usercity, text = "Submit", font=('bold',25), command=get_weathers)
Submit_button.place(relx=0.8,rely=0.12,relheight=0.5,relwidth=0.2)


####### Timezone frame
frame_timezone = tk.Frame(sheet1,bg='#80c1ff', bd=7)
frame_timezone.place(relx=0.5, rely=0.2,relwidth=0.55, relheight=0.1, anchor = 'n')
label_timezone = tk.Label(frame_timezone,text="City", font=('courier',20,'bold'),justify= 'left',bd=17)
label_timezone.place(relx=0, rely=0,relwidth=1, relheight=0.45)
label_timezone2 = tk.Label(frame_timezone,text="Time Zone info", font=('courier',20,'bold'),justify= 'left',bd=17)
label_timezone2.place(relx=0, rely=0.49,relwidth=1, relheight=0.5)


## Lower Frame
lower_frame = tk.Frame(sheet1, bg = '#80c1ff', bd=7)
lower_frame.place(relx=0.5, rely=0.38, relwidth=0.95, relheight=0.6, anchor = 'n')

### Label Weather Information
labelweather = tk.Label(lower_frame,text='Temprature', font=('courier',20,'bold'),justify= 'center',bd=17)
labelweather.place(relx=0, rely=0.0,relwidth=0.3, relheight=0.33)
labelweatherfeel = tk.Label(lower_frame,text='Feels like', font=('courier',20,'bold'),justify= 'center',bd=17)
labelweatherfeel.place(relx=0, rely=0.33,relwidth=0.3, relheight=0.33)
labelweatherhumid = tk.Label(lower_frame,text='Humidity', font=('courier',20,'bold'),justify= 'center',bd=17)
labelweatherhumid.place(relx=0, rely=0.66,relwidth=0.3, relheight=0.34)

### Lable air polution information
labelairpolution = tk.Label(lower_frame,text="Air Quality", font=('courier',20,'bold'),justify= 'center',bd=4)
labelairpolution.place(relx=0.34, rely=0,relwidth=0.3, relheight=0.1)
labelairpolution2 = tk.Label(lower_frame,text="Carbon monoxide", font=('courier',20,'bold'),justify= 'center',bd=4)
labelairpolution2.place(relx=0.34, rely=0.11,relwidth=0.3, relheight=0.1)
labelairpolution3 = tk.Label(lower_frame,text="Nitrogen monoxide", font=('courier',20,'bold'),justify= 'center',bd=4)
labelairpolution3.place(relx=0.34, rely=0.22,relwidth=0.3, relheight=0.1)
labelairpolution4 = tk.Label(lower_frame,text="Nitrogen dioxide", font=('courier',20,'bold'),justify= 'center',bd=4)
labelairpolution4.place(relx=0.34, rely=0.33,relwidth=0.3, relheight=0.1)
labelairpolution5 = tk.Label(lower_frame,text="Ozone", font=('courier',20,'bold'),justify= 'center',bd=4)
labelairpolution5.place(relx=0.34, rely=0.44,relwidth=0.3, relheight=0.1)
labelairpolution6 = tk.Label(lower_frame,text="Sulphur dioxide", font=('courier',20,'bold'),justify= 'center',bd=4)
labelairpolution6.place(relx=0.34, rely=0.55,relwidth=0.3, relheight=0.1)
labelairpolution7 = tk.Label(lower_frame,text="Fine particles matter", font=('courier',20,'bold'),justify= 'center',bd=4)
labelairpolution7.place(relx=0.34, rely=0.66,relwidth=0.3, relheight=0.1)
labelairpolution8 = tk.Label(lower_frame,text="Coarse particulate matter", font=('courier',20,'bold'),justify= 'center',bd=4)
labelairpolution8.place(relx=0.34, rely=0.77,relwidth=0.3, relheight=0.1)
labelairpolution9 = tk.Label(lower_frame,text="Ammonia", font=('courier',20,'bold'),justify= 'center',bd=4)
labelairpolution9.place(relx=0.34, rely=0.88,relwidth=0.3, relheight=0.1)

### lable solar radition information
labelsolar = tk.Label(lower_frame,text="UVI Index", font=('courier',20,'bold'),justify= 'center',bd=4)
labelsolar.place(relx=0.68, rely=0,relwidth=0.3, relheight=0.1)
labelsolar2 = tk.Label(lower_frame,text="Cloud", font=('courier',20,'bold'),justify= 'center',bd=4)
labelsolar2.place(relx=0.68, rely=0.11,relwidth=0.3, relheight=0.1)
labelsolar3 = tk.Label(lower_frame,text="Pressure", font=('courier',20,'bold'),justify= 'center',bd=4)
labelsolar3.place(relx=0.68, rely=0.22,relwidth=0.3, relheight=0.1)
labelsolar4 = tk.Label(lower_frame,text="Visibility", font=('courier',20,'bold'),justify= 'center',bd=4)
labelsolar4.place(relx=0.68, rely=0.33,relwidth=0.3, relheight=0.1)
labelsolar5 = tk.Label(lower_frame,text="Windspeed", font=('courier',20,'bold'),justify= 'center',bd=4)
labelsolar5.place(relx=0.68, rely=0.44,relwidth=0.3, relheight=0.1)
labelsolar6 = tk.Label(lower_frame,text="Wind degree", font=('courier',20,'bold'),justify= 'center',bd=4)
labelsolar6.place(relx=0.68, rely=0.55,relwidth=0.3, relheight=0.1)
labelsolar7 = tk.Label(lower_frame,text="Dewpoint", font=('courier',20,'bold'),justify= 'center',bd=4)
labelsolar7.place(relx=0.68, rely=0.66,relwidth=0.3, relheight=0.1)
labelsolar8 = tk.Label(lower_frame,text="Weather description", font=('courier',20,'bold'),justify= 'center',bd=4)
labelsolar8.place(relx=0.68, rely=0.77,relwidth=0.3, relheight=0.1)

with urllib.request.urlopen("http://openweathermap.org/img/wn/01n@2x.png") as url:
    raw_data1 = url.read()
    image1 = PhotoImage(data=raw_data1)
labelsolar9 = tk.Label(lower_frame,image=image1,bg='#80c1ff',justify= 'center',bd=4)
labelsolar9.place(relx=0.68, rely=0.88,relwidth=0.3, relheight=0.1)



root.mainloop()



















