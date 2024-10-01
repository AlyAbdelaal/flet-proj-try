from flet import *
count = 0

def main(page:Page):
    page.horizontal_alignment="center"
    page.vertical_alignment="center"


    
    def action(*args):
        global count
        count += 1
        tx.value=str(count)
        page.update()
        



    tx = Text("0",
              color=colors.BLACK,
              bgcolor=colors.WHITE10,
              size=27,
              height=40,
              width=40
              )
    bt = ElevatedButton(
        "Add",
        icon=icons.ADD,
        icon_color=colors.BLUE,
        on_click=action
    )
    
    page.add(tx,bt)
    page.update()

app(target=main)