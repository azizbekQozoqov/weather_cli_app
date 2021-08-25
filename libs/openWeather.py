import requests
link = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
class Weather:
    def __init__(self, API_KEY,city_name):
        self.city_name = city_name
        self.API_KEY = API_KEY

    def get_weathetr(self):
        try:
            res = requests.get(link.format(self.city_name, self.API_KEY)).json()
            if int(res["cod"]) == 404:
                return {
                    "NotFoundError": True,
                    "message": "City is not found."
                }
            elif int(res["cod"]) == 401:
                return {
                    "NotFoundError": True,
                    "message": "Your api key is not found"
                }
            else:
                res["NotFoundError"] = False
                return res
        except:
            return "Any ERROR."