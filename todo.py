import flet as ft

def main(page: ft.Page):
    
    def add_clicked(e):
        page.add(ft.Checkbox(label=new.value))
        new.value = ""
        new.focus()
        new.update()
    
    new = ft.TextField(hint_text="What's need to be done?", width=300)
    page.add(ft.Row([new, ft.ElevatedButton("Add", on_click=add_clicked)]))
    
ft.app(main)