

import flet as ft
import requests
CITIES = [
        ("East London", -33.02, 27.91),
            ("Cape Town", -33.92, 18.42),
                ("Johannesburg", -26.29, 28.05),
                    ("Durban", -29.86, 31.02),
                    ]
CODES = {0: "Clear sky", 1: "Mostly clear", 2: "Partly cloudy",
         3: "Overcast", 45: "Fog", 51: "Light drizzle",
                  61: "Rain", 80: "Rain showers", 95: "Thunderstorm"}
def get_weather(lat, lon):
        url = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}"
                   f"&longitude={lon}&current=temperature_2m,weather_code,wind_speed_10m")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()["current"]
def main(page: ft.Page):
            page.title = "South Africa Weather"
            page.bgcolor = ft.Colors.BLUE_GREY_900
            page.padding = 20
            index =0
            city  = ft.Text(size=24 , weight=ft.FontWeight .BOLD, color=ft.Colors.WHITE)
            temp = ft.Text(size=48, weight=ft.FontWeight  .BOLD , color=ft.Colors.WHITE)
            condition = ft.Text(size=20, color=ft.Colors.WHITE)
            wind = ft.Text( size=16, color=ft.Colors.RED_300)
          
            error = ft.Text(color=ft.Colors.RED_300)
            def load(e =None):
                    name, lat , lon = CITIES[index % len (CITIES)]
                    city.value = name
                    try:
                        data = get_weather(lat , lon)

                        temp.value = f"{data['temperature_2m']} C"
                        condition.value = CODES.get(data["weather_code"] , "Unknown ")
                        wind.value = f"wind: {data['wind_speed_10m']} km/h"
                        error.value = ""
                    except requests.exceptions.RequestException:
                        temp.value = ""
                        condition.value = ""
                        wind.value = ""
                        error.value = "Could not load weather "
                        page.update()
            def Refresh(e):
                        nonlocal index
                        index +=1
                        load()
            card = ft.Container(content=ft.Column ([temp , condition , wind]),
                    bgcolor=ft.Colors.BLUE_700,
                    padding =20,
                    border_radius = 16,
                    width=300,
                    )
            page.add(city ,card, error, ft.Button("Refresh" , on_click=Refresh))
                                                 
            load()
    if __name__ == "__main__":
        ft.run(main)