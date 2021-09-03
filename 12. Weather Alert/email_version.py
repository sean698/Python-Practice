import requests
import smtplib
import schedule
import time

# If it is going to rain in the next 12 hours, send an SMS

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "c5811c44b6b0dfa9598a4898a97f91df"
MY_LAT = 40.071766
MY_LNG = 113.316421
MY_EMAIL = "1084927875@qq.com"
MY_PWD = "bvgaeyfivuuifgic"

# We want hourly forecast in the next 12 hours from 7am everyday
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

def send_mail():
    connection = smtplib.SMTP("smtp.qq.com") 
    connection.starttls()
    connection.login(MY_EMAIL, MY_PWD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:From your boyfriend's love\n\nIt's going to rain today. Remember to bring an umbrella~~"
    )

def will_rain():
    res = requests.get(OWM_ENDPOINT, params=weather_params)
    weather_data = res.json()
    # Python slice feature
    weather_slice = weather_data["hourly"][:12]
    for hour_data in weather_slice:
        weather_id = hour_data["weather"][0]["id"]
        if weather_id < 700:
            return True
    return False

def job():
    if will_rain():
        send_mail()
        print("A email has been sent.")
    else:
        print("There is no rain today.")

schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

    

