from libs.openWeather import Weather
from libs.color import Colors

API_KEY = "<YOUR_API_KEY_HERE>"
cl = Colors()

attr = {
    "temp" : cl.OKGREEN + cl.BOLD + "Temprature : " + cl.ENDC,
    "weat" : cl.OKGREEN + cl.BOLD + "Weather : " + cl.ENDC,
    "count": cl.OKGREEN + cl.BOLD + "Country: " + cl.ENDC,
    "dev": cl.OKBLUE + cl.BOLD + "AzizbekDeveloper" + cl.ENDC,
    "gitHub": cl.OKCYAN + "https://github.com/azizbekQozoqov/" + cl.ENDC,
    "quitInfo": cl.WARNING + "Thanks for using." + cl.ENDC
}
welcome_message = "Made by {}\n{}\nEnter the city name to get WEATHER information. Or quit to stop work".format(attr["dev"], attr["gitHub"])
print(welcome_message)
while True:
    msg = input("$: ")

    if msg.lower() != "quit":
        res = Weather(API_KEY, msg).get_weathetr()

        if res["NotFoundError"]:
            print(cl.FAIL + cl.BOLD +res["message"] + cl.ENDC)
        else:
            print("Weather informations for: " + msg.upper())
            print(attr["temp"], res["main"]["temp"])
            print(attr["weat"], res["weather"][0]["description"].title())
            print(attr["count"], res["sys"]["country"])
    else:
        print(attr["quitInfo"])
        break