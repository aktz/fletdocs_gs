import time
import flet as ft

def main(page: ft.Page):
    
    def button_clicked(e):
        page.add(ft.Text("Clicked"))
    
    t = ft.Text(value="Hola Mundo", color="blue")
    page.add(t)
    
    for i in range(10):
        t.value = f"Paso {i}"
        page.update()
        time.sleep(1) 
        
    page.add(ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C"),
        ft.ElevatedButton(text="Botón", on_click=button_clicked)
    ]))
    
    col = ft.Column([
        ft.TextField(),
        ft.TextField()
    ])
    
    col.disabled = True
    page.add(col)

ft.app(main)
