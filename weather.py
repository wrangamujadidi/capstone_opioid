

import urllib.request
import json
import pandas as pd
import numpy as np
import csv


lat = 38.889939
long = -77.009051


#to put the lat, long inside the URL:

#url = "https://api.darksky.net/forecast/1fb8adfac09f5dacb0274c523ee6be7b/38.87296,-77.01065,\
#255589200?UNITS=us?exclude=currently,flags,hourly,minutely"

#to put the lat, long, month as variables: 


#Reading in the 2017 Weather Data into a CSV

with open('weather2017.csv', 'w', newline='') as f:
    
    writer = csv.writer(f)
    
    leading_zero = '0'

    for i in range(1,7):
    
        month = leading_zero + str(i) 
    
        for day in range (1, 29):
        
            if day < 10:
        
                day = leading_zero + str(day)
        
                url = "https://api.darksky.net/forecast/1fb8adfac09f5dacb0274c523ee6be7b/{},{},2017-{}-{}T12:00:00?UNITS=us?\
exclude=currently,flags,hourly,minutely".format(lat, long, month, day)

    
                def response(url):
                    with urllib.request.urlopen(url) as response:
                        return response.read()
        
                res = response(url)
                parsed = json.loads(res)
    
                temp = parsed['currently']['temperature']
                precip = parsed['currently']['precipIntensity']
                humidity = parsed['currently']['humidity']


                row = month, day, temp, precip, humidity
                writer.writerows([row])
            
            else: 
            
                url = "https://api.darksky.net/forecast/1fb8adfac09f5dacb0274c523ee6be7b/{},{},2017-{}-{}T12:00:00?UNITS=us?\
exclude=currently,flags,hourly,minutely".format(lat, long, month, day)

                def response(url):
                    with urllib.request.urlopen(url) as response:
                        return response.read()
        
        
                res = response(url)
                parsed = json.loads(res)
    
                temp = parsed['currently']['temperature']
                precip = parsed['currently']['precipIntensity']
                humidity = parsed['currently']['humidity']


                row = month, day, temp, precip, humidity
                writer.writerows([row])


#Reading in the 2016 Weather Data into a CSV

with open('weather.csv', 'w', newline='') as f:
    
    writer = csv.writer(f)
    
    leading_zero = '0'

    for i in range(1,10):
    
        month = leading_zero + str(i) 
    
        for day in range (1, 29):
        
            if day < 10:
        
                day = leading_zero + str(day)
        
                url = "https://api.darksky.net/forecast/1fb8adfac09f5dacb0274c523ee6be7b/{},{},2016-{}-{}T12:00:00?UNITS=us?\
exclude=currently,flags,hourly,minutely".format(lat, long, month, day)

    
                def response(url):
                    with urllib.request.urlopen(url) as response:
                        return response.read()
        
                res = response(url)
                parsed = json.loads(res)
    
                temp = parsed['currently']['temperature']
                precip = parsed['currently']['precipIntensity']
                humidity = parsed['currently']['humidity']


                row = month, day, temp, precip, humidity
                writer.writerows([row])
            
            else: 
            
                url = "https://api.darksky.net/forecast/1fb8adfac09f5dacb0274c523ee6be7b/{},{},2016-{}-{}T12:00:00?UNITS=us?\
exclude=currently,flags,hourly,minutely".format(lat, long, month, day)

                def response(url):
                    with urllib.request.urlopen(url) as response:
                        return response.read()
        
        
                res = response(url)
                parsed = json.loads(res)
    
                temp = parsed['currently']['temperature']
                precip = parsed['currently']['precipIntensity']
                humidity = parsed['currently']['humidity']


                row = month, day, temp, precip, humidity
                writer.writerows([row])
        
        
    for month in range(10,13):
        
        for day in range (1, 29):
        
            if day < 10:
    
                day = leading_zero + str(day)
        
                url = "https://api.darksky.net/forecast/1fb8adfac09f5dacb0274c523ee6be7b/{},{},2016-{}-{}T12:00:00?UNITS=us?\
exclude=currently,flags,hourly,minutely".format(lat, long, month, day)

    
                def response(url):
                    with urllib.request.urlopen(url) as response:
                        return response.read()
        
        
                res = response(url)
                parsed = json.loads(res)
    
                temp = parsed['currently']['temperature']
                precip = parsed['currently']['precipIntensity']
                humidity = parsed['currently']['humidity']

                row = month, day, temp, precip, humidity
                writer.writerows([row])
 
            
            else: 
            
                url = "https://api.darksky.net/forecast/1fb8adfac09f5dacb0274c523ee6be7b/{},{},2016-{}-{}T12:00:00?UNITS=us?\
exclude=currently,flags,hourly,minutely".format(lat, long, month, day)

                def response(url):
                    with urllib.request.urlopen(url) as response:
                        return response.read()
        
        
                res = response(url)
                parsed = json.loads(res)
    
                temp = parsed['currently']['temperature']
                precip = parsed['currently']['precipIntensity']
                humidity = parsed['currently']['humidity']

                row = month, day, temp, precip, humidity
                writer.writerows([row])
        





