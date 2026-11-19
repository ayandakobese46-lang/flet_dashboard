import flet as ft
import requests

def main(page: ft.page):
        page.title = "East London weather"
        page.bgcolor = ft.Colors.BLUE_Grey_900
        page.padding = 20 
    
URL = "https://api.open-meteo.com/v1/forecast?latitude=-33.02&longitude=27.91&current=temperature_2m,weather_code,wind_speed_10m"

CODES = {0: "Clear sky", 1: "Mostly clear", 2: "Partly cloudy",
         3: "Overcast", 45: "Fog", 51: "Light drizzle",
                  61: "Rain", 80: "Rain showers", 95: "Thunderstorm"}
def get_weather():
                      response = requests.get(URL, timeout=10)
                      response.raise_for_status()
                      return response.json()["current"]
def main(page: ft.Page):
                                  page.title = "East London Weather"
                                  page.bgcolor = ft.Colors.BLUE_GREY_900
                                  page.padding = 20

                                  temp = ft.Text(size=48, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
                                  condition = ft.Text(size=20, color=ft.Colors.AMBER_200)
                                  wind = ft.Text(size=16, color=ft.Colors.WHITE)
                                  error = ft.Text(color=ft.Colors.RED_300)

                                  def load(e=None):

                                    try:
                                        data = get_weather()  
                                        temp.value = f"{data['temperature_2m']} °C"        
                                        condition.value  = CODES.get(data['weather_code'], "Unknown")
                                        wind.value = f"wind: {data['wind_speed_10m']} kh/m"
                                        error.value = ""
                                    except requests.exceptions.RequestException:
                                          temp.value = ""
                                          condition.value = ""
                                          wind.value = ""
                                          error.value = "Could not load weather data. Please check your internet connection and Tap Refresh"
                                    page.update()
                                  card = ft.Container(content=ft.Column([temp, condition, wind]),bgcolor= ft.Colors.BLUE_700,padding=20, border_radius=16)

                                  page.add(ft.Text("East London" , size=24,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE),card , error, ft.Button("Refresh", on_click=load))
                                          
                                  load()







if __name__ == "__main__":
 ft.run(main)