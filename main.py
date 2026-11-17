import flet as ft

def main(page: ft.Page):
    page.add(ft.Text("Hello Flet"))

    ft.run(main, view=ft.AppView.WEB_BROWSER, port=8080)