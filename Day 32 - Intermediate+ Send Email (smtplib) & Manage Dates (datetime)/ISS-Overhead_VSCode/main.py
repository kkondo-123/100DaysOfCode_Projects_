"""
Name: Kana Kondo
Date: 2025-07-17-Thu
Course: 100 Days of Code Day 32
Description: ISS Overhead Project
"""

import requests
from datetime import datetime
import smtplib
import time

'''
Install requests Python module in VSCode: https://pypi.org/project/requests/
(Assuming that pip is already installed, covered in Day 18)
 1. Open 'zsh' terminal and type 'python3 -m venv env' and press enter.
 2. A file called 'env' should appear.  Type 'source env/bin/activate'. 
 3. Type 'pip3 install requests' -> 'Successfully installed .... requests-2.32.4 ...'
 4. Ensure I already am in Python 3.8.10
'''

SENDER_EMAIL = 'SENDEREMAIL'
APP_PASSWORD = 'APPPASSWORD'  
RECEIVER_EMAIL = 'RECEIVEREMAIL'

# https://www.latlong.net/
MY_LAT = 0 # Your latitude
MY_LONG = 0 # Your longitude

is_close = None
is_dark = None

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_iss_close():
    global is_close

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    abs_lat_diff = abs(iss_latitude - MY_LAT)
    abs_long_diff = abs(iss_longitude - MY_LONG)

    # print(f"iss_latitude= {iss_latitude}, iss_longitude={iss_longitude}")
    # print(f"MY_LAT={MY_LAT}, MY_LONG={MY_LONG}")

    is_close = False
    if abs_lat_diff <= 5 and abs_long_diff <= 5:
        is_close = True

    # print(f"abs_lat_diff={abs_lat_diff}, abs_long_diff={abs_long_diff}")
    print(f"is_close={is_close}")

def is_it_dark():
    global is_dark

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.

    # Currently dark if the time now is in between sunset and sunrise
    is_dark = False

    # This is incorrect since we want IN BETWEEN sunset and sunrise.  That means after sunset (sunset <= current hour) and before sunrise (sunrise >= current_hour)
    # if sunrise <= datetime.now().hour <= sunset:  # https://www.freecodecamp.org/news/python-datetime-now-how-to-get-todays-date-and-time/
        
    if datetime.now().hour <= sunrise or datetime.now().hour >= sunset:
        is_dark = True

    print(f"datetime.now().hour={datetime.now().hour}")
    print(f"sunrise={sunrise}")
    print(f"sunset={sunset}")
    print(f"is_dark={is_dark}")
  
while True:
    print(" \nChecking ISS location and current time...")
    is_iss_close()
    is_it_dark()
    if is_dark and is_close:
        print("\nSending email...")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f"Subject: The ISS Is Overhead\n\nLook up!"  # https://www.datacamp.com/tutorial/how-to-convert-a-list-to-a-string-in-python
            )
    time.sleep(60)
