import flet as ft

def main(page: ft.Page):
    
    def clicked(e):
        text.value = f"Selected: {dropdown.value}"
        page.update()
    
    text = ft.Text()
    button = ft.ElevatedButton("Submit", on_click=clicked)
    dropdown = ft.Dropdown(
        options= [
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue")
        ],
    width=100)    
    
    page.add(text, dropdown, button)
    
ft.app(main)