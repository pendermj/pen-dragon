import flet as ft


#defining main function, variables and button click function

def main(page: ft.Page):
    page.title = "TO DO APP"


    txtapptitle = ft.Text(value="MY TODOs", color=ft.colors.INDIGO_500, 
                          size= 20, width=200)
    
    page.add(txtapptitle)
    

    def btnADD_clicked(e):
        page.add(ft.Checkbox(label=txtTodoInput.value))
        txtTodoInput.value=""
        page.update() 
            
    
# DEFINING THE variables relating to each control eg btnADD 

    
    btnADD=ft.ElevatedButton(text="ADD", on_click= btnADD_clicked)
    txtTodoInput= ft.TextField(hint_text="enter new TO DO",width=200)
   
   
    page.add(
        ft.Row(
            [
            txtTodoInput,
            btnADD
            ]
        )
    )
        
ft.app(target=main)