import requests
import smtplib
import datetime as dt
import time

MY_LAT = 40.070190
MY_LNG = 113.311254
ISS_URL = "http://api.open-notify.org/iss-now.json"
SUNTIME_URL = "https://api.sunrise-sunset.org/json"
# Not the real login info
MY_EMAIL = "1084927875@qq.com"
MY_PWD = "bvgaeyfivuuifgic"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

def is_overhead():
    res = requests.get(url=ISS_URL)
    iss_lat = float(res.json()["iss_position"]["latitude"])
    iss_lng = float(res.json()["iss_position"]["longitude"])
    if (MY_LAT - 5 <= iss_lat <= MY_LAT + 5) and (MY_LNG - 5 <= iss_lng <= MY_LNG):
        return True
    return False

def is_night():
    current_hour = dt.datetime.now().hour
    res = requests.get(url=SUNTIME_URL, params=parameters)
    sunrise = int(res.json()["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset = int(res.json()["results"]["sunset"].split('T')[1].split(':')[0])
    if current_hour <= sunrise or current_hour >= sunset:
        return True
    return False

def send_mail():
    connection = smtplib.SMTP("smtp.qq.com") 
    connection.starttls()
    connection.login(MY_EMAIL, MY_PWD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
    )

while True:  
    time.sleep(60)
    if is_night() and is_overhead():
        send_mail()
        print("A email has been sent.")
    else:
        print("None.")
    

