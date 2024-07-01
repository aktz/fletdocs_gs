import flet as ft

def main(page: ft.Page):
    
    def button_clicked(e):
        if not name.value:
            name.error_text = "Ingresa tu nombre"
            page.update()
        else:
            title = name.value
            page.clean()
            page.add(ft.Text(f"Hello {title}"))
    
    name = ft.TextField(label="Your name")
    
    page.add(
        name,
        ft.ElevatedButton("Say Hello!", on_click=button_clicked)
    )
    
ft.app(main)