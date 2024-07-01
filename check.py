import flet as ft

def main(page: ft.Page):
    
    def checked(e):
        text.value = f"You've learned Sky! [{checkbox.value}]"
        page.add(text)
        page.update()
        
    text = ft.Text()
    checkbox = ft.Checkbox(label="Learn Sky", value=False, on_change=checked)
    
    page.add(checkbox)
    
ft.app(main) 
    