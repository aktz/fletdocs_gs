import flet as ft

def main(page: ft.Page):
    
    page.title = "Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    text = ft.TextField(value="0", text_align="right", width=100)
    
    def add_click(e):
        text.value = str(int(text.value) + 1)
        page.update()
        
    def sub_click(e):
        text.value = str(int(text.value) - 1)
        page.update()
        
        
    add = ft.ElevatedButton("+", on_click=add_click)
    sub = ft.ElevatedButton("-", on_click=sub_click)
    
    page.add(ft.Row([
        sub,
        text,
        add
    ], alignment=ft.MainAxisAlignment.CENTER))
    
    
    
ft.app(main)