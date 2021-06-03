import requests
import time
from datetime import datetime
import schedule
dist = 313
channel_id = "@gwlvaccineslot"
now = datetime.now()
today_date = now.strftime("%d-%m-%Y")
api_url_telegram = "https://api.telegram.org/bot1850217717:AAGPEBy9LvIhomu0Osz0fhQjVRXsrbVPToE/sendMessage?chat_id={}&text=".format(channel_id)
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}'.format(
    dist, today_date)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

print("Starting Slot Searching")    


def findAvailability():
    result = requests.get(URL, headers=header)
    response_json = result.json()
    for center in response_json["centers"]:
        for session in center["sessions"]:
            if session["available_capacity_dose2"] > 10 and session["min_age_limit"]==18 and session["vaccine"]=="COVAXIN" :
               message = "⚠Vaccination centers for 18-44 age group❗ \n🔰Center: {} \n🌍Pincode: {} \n💉Vaccine: {} \n💸Fee type: {}  \n🧑Age: {} \n💉Dose 1: {} \n💉Dose 2: {} \n📅Date: {} \n\n🌐Cowin: https://selfregistration.cowin.gov.in | @gwlvaccineslot".format(
                center["name"],
                center["pincode"],
                session["vaccine"],
                center["fee_type"],
                session["min_age_limit"],
                session["available_capacity_dose1"],
                session["available_capacity_dose2"],
                session["date"])      
               send_message_telegram(message)

def send_message_telegram(message):
        final_telegram_url = api_url_telegram + message
        response = requests.get(final_telegram_url)
        print(response)
         

schedule.every(5).seconds.do(findAvailability)        

 
while True:
    schedule.run_pending()
    time.sleep(1)

    
  


