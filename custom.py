import flet as ft

class CustomButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.colors.BLUE_100
        self.color = ft.colors.BLUE_800
        self.text = text
        self.on_click = on_click

def main(page: ft.Page):
    
    def ok_clicked(e):
        print("OK clicked")

    def cancel_clicked(e):
        print("CANCEL clicked")
    
    page.add(CustomButton("OK", on_click=ok_clicked), CustomButton("Cancel", on_click=cancel_clicked))
    
ft.app(main)