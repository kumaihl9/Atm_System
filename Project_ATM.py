import flet as ft
from flet import *
import sqlite3

con = sqlite3.connect("project.db", check_same_thread=False)
cur = con.cursor()

# cur.execute('drop table customer')
cur.execute("Create table customer(ID int,Password,Name,Cash int)")
con.commit()

cur.execute("insert into customer values(330000,'20456','kumail',223000),(2444,'4232','ammar',24252)")

con.commit()


def main(page: Page):
    page.fonts = {
        "Poppins": "fonts/Poppins.ttf",
        "San Fransisco": "fonts/SFS.otf"
    }
    page.title = "ATM Machine"
    page.bgcolor = "#081d33"
    page.padding = 20
    page.window_width = 550
    page.window_height = 650

    def logoutPage(e):
        page.clean()
        page.theme = Theme(font_family='San Fransisco')
        page.add(
            Row(
                [
                    Container(
                        expand=True,
                        height=60,
                        bgcolor="#fdfdfd",
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        padding=padding.only(left=15, right=15),
                        content=IconButton(icons.HOME, on_click=FirstPage),
                    ),
                ],
            ),
            Row(
                [
                    Text("Login Account", size=20, weight="bold", font_family='San Fransisco'),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [id],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [password],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=FirstPage,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Login",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=Register,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Register",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        ),

    def Register(e):
        page.clean()
        page.add(
            Row(
                [
                    Container(
                        expand=True,
                        height=60,
                        bgcolor="#fdfdfd",
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        padding=padding.only(left=15, right=15),
                        content=IconButton(icons.HOME, on_click=FirstPage),
                    ),
                ],
            ),
            Row(
                [
                    Text("Register Account", size=20, weight="bold", font_family='San Fransisco'),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [id],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [password],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [name],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [cash],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=LoginPage,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Register",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        ),
    
    def wrongPass():
        page.clean()
        page.theme = Theme(font_family='San Fransisco')
        page.add(
            Row(
                [
                    Container(
                        expand=True,
                        height=60,
                        bgcolor="#fdfdfd",
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        padding=padding.only(left=15, right=15),
                        content=IconButton(icons.HOME, on_click=FirstPage),
                    ),
                ],
            ),
            Row(
                [
                    Text("Login Account", size=20, weight="bold", font_family='San Fransisco'),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [id],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [password],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=FirstPage,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Login",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=Register,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Register",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [Text("Wrong Email or Password", size=15, weight="bold", font_family='San Fransisco')],
                alignment=MainAxisAlignment.CENTER,
            ),
        ),
    
    

    def FirstPage(e):
    
        cur.execute("select * from customer")
        if (cur.execute(f"select * from customer where {id.value}=ID AND '{password.value}'=Password")):
            global rows
            rows = cur.fetchall()

        if len(rows)==0:
            wrongPass()
                 
        elif (len(rows))==1:
            page.clean()
            page.add(
                Row(
                    [
                        Container(
                            expand=True,
                            height=60,
                            bgcolor="#fdfdfd",
                            border_radius=border_radius.only(top_left=15, top_right=15),
                            padding=padding.only(left=15, right=15),
                            content=IconButton(icons.HOME, on_click=FirstPage),
                        ),
                    ],
                ),
                Row(
                    [
                        Container(
                            padding=30,
                            alignment=alignment.center,
                            content=ElevatedButton(
                                on_click=NewPage,
                                bgcolor="#081d33",
                                color="white",
                                content=Row(
                                    controls=[
                                        Text(
                                            "Saving Account",
                                            size=15,
                                            weight="bold", font_family='San Fransisco',
                                        ),
                                    ],
                                ),
                                style=ButtonStyle(
                                    shape={
                                        "": RoundedRectangleBorder(radius=6),
                                    },
                                    color={"": "white"},
                                ),
                                height=88,
                                width=330,
                            ),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [
                        Container(
                            padding=30,
                            alignment=alignment.center,
                            content=ElevatedButton(
                                on_click=NewPage,
                                bgcolor="#081d33",
                                color="white",
                                content=Row(
                                    controls=[
                                        Text(
                                            "Current Account",
                                            size=15,
                                            weight="bold", font_family='San Fransisco',
                                        ),
                                    ],
                                ),
                                style=ButtonStyle(
                                    shape={
                                        "": RoundedRectangleBorder(radius=6),
                                    },
                                    color={"": "white"},
                                ),
                                height=88,
                                width=330,
                            ),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [
                        Container(
                            padding = 60,
                            alignment=alignment.center,
                            content=ElevatedButton(
                                on_click=logoutPage,
                                bgcolor="#081d33",
                                color="white",
                                content=Row(
                                    controls=[
                                        Text(
                                            "Logout!",
                                            size=15,
                                            weight="bold", font_family='San Fransisco',
                                        ),
                                    ],
                                ),
                                style=ButtonStyle(
                                    shape={
                                        "": RoundedRectangleBorder(radius=6),
                                    },
                                    color={"": "white"},
                                ),
                                height=58,
                                width=130,
                            ),
                        ),
                    ],
                    alignment= MainAxisAlignment.END
                )
            ),

    def NewPage(e):
        page.clean()
        page.add(
            Row(
                [
                    Container(
                        expand=True,
                        height=60,
                        bgcolor="#fdfdfd",
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        padding=padding.only(left=15, right=15),
                        content=IconButton(icons.HOME, on_click=FirstPage),
                    ),
                ],
            ),
            Row(
                [
                    Container(
                        padding=15,
                        alignment=alignment.center,
                        content=ElevatedButton(
                            on_click=Withdrawal,
                            bgcolor="#081d33",
                            color="white",
                            content=Row(
                                controls=[
                                    Text(
                                        "Cash Withdrawal",
                                        size=15,
                                        weight="bold", font_family='San Fransisco',
                                    ),
                                ],
                            ),
                            style=ButtonStyle(
                                shape={
                                    "": RoundedRectangleBorder(radius=6),
                                },
                                color={"": "white"},
                            ),
                            height=88,
                            width=330,
                        ),
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    Container(
                        padding=15,
                        alignment=alignment.center,
                        content=ElevatedButton(
                            on_click=Transfer,
                            bgcolor="#081d33",
                            color="white",
                            content=Row(
                                controls=[
                                    Text(
                                        "Transfer Money",
                                        size=15,
                                        weight="bold", font_family='San Fransisco',
                                    ),
                                ],
                            ),
                            style=ButtonStyle(
                                shape={
                                    "": RoundedRectangleBorder(radius=6),
                                },
                                color={"": "white"},
                            ),
                            height=88,
                            width=330,
                        ),
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_AROUND,
            ),
            Row(
                [
                    Container(
                        padding=15,
                        alignment=alignment.center,
                        content=ElevatedButton(
                            on_click=Deposit,
                            bgcolor="#081d33",
                            color="white",
                            content=Row(
                                controls=[
                                    Text(
                                        "Deposit Money",
                                        size=15,
                                        weight="bold", font_family='San Fransisco',
                                    ),
                                ],
                            ),
                            style=ButtonStyle(
                                shape={
                                    "": RoundedRectangleBorder(radius=6),
                                },
                                color={"": "white"},
                            ),
                            height=88,
                            width=330,
                        ),
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_AROUND,
            ),
            Row(
                [
                    Container(
                        padding=15,
                        alignment=alignment.center,
                        content=ElevatedButton(
                            on_click=Balance,
                            bgcolor="#081d33",
                            color="white",
                            content=Row(
                                controls=[
                                    Text(
                                        "Balance Inquiry",
                                        size=15,
                                        weight="bold", font_family='San Fransisco',
                                    ),
                                ],
                            ),
                            style=ButtonStyle(
                                shape={
                                    "": RoundedRectangleBorder(radius=6),
                                },
                                color={"": "white"},
                            ),
                            height=88,
                            width=330,
                        ),
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_AROUND,
            ),
        ),

    def Balance(e):
        balanceName = rows[0][2]
        balanceAmount = rows[0][3]
        page.clean()
        page.add(
            Row(
                [
                    Container(
                        expand=True,
                        height=60,
                        bgcolor="#fdfdfd",
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        padding=padding.only(left=15, right=15),
                        content=IconButton(icons.HOME, on_click=FirstPage),
                    ),
                ],
            ),
            Row(
                [Text("Current Balance", size=25, weight="bold", font_family='San Fransisco')],
                alignment=MainAxisAlignment.CENTER,
            ),
            
            Row([
                Text(f"Name: {balanceName}\nBalance: {balanceAmount}", size=25)
            ],
            alignment=MainAxisAlignment.CENTER),
            Row(
                [
                    ElevatedButton(
                        on_click=NewPage,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Go Back",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        ),
    

    def Deposit(e):
        page.clean()
        global deposit
        deposit = TextField(
            label="Enter Amount",
            autofocus=True,
            border_color="transparent",
            icon=icons.MONEY_ROUNDED,
            content_padding=15,
        )
        page.add(
            Row(
                [
                    Container(
                        expand=True,
                        height=60,
                        bgcolor="#fdfdfd",
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        padding=padding.only(left=15, right=15),
                        content=IconButton(icons.HOME, on_click=FirstPage),
                    ),
                ],
            ),
            Row(
                [
                    Text("Deposit Amount", size=20, weight="bold", font_family='San Fransisco'),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [deposit],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=depositProcessing,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Deposit",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=NewPage,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Go Back",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        ),
    
    def depositProcessing(e):
        updatedValue = rows[0][3] + int(deposit.value)
        updateID = rows[0][0]
        cur.execute(f"Update customer set Cash = {updatedValue} where ID = {updateID}")
        con.commit()
        page.add(
            Row(
            [
                Text('Money Deposited')
            ],
            alignment= MainAxisAlignment.CENTER
            )
        )

    def Transfer(e):
        page.clean()
        global transfer
        transfer = TextField(
            label="Enter Amount",
            autofocus=True,
            border_color="transparent",
            icon=icons.MONEY_ROUNDED,
            content_padding=15,
        )
        global To
        To = TextField(
            label="Enter ID",
            autofocus=True,
            border_color="transparent",
            icon=icons.MONEY_ROUNDED,
            content_padding=15,
        )

        page.add(
            Row(
                [
                    Container(
                        expand=True,
                        height=60,
                        bgcolor="#fdfdfd",
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        padding=padding.only(left=15, right=15),
                        content=IconButton(icons.HOME, on_click=FirstPage),
                    ),
                ],
            ),
            Row(
                [
                    Text("Transfer Amount", size=20, weight="bold", font_family='San Fransisco'),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [transfer],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row([
                Text('To', size=20, weight="bold", font_family='San Fransisco')
            ],
                alignment=MainAxisAlignment.CENTER,
            ),

            Row(
                [To],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=transferProcessing,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Transfer",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=NewPage,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Go Back",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        ),
    def transferProcessing(e):
        subtractValue = rows[0][3] - int(transfer.value)
        updateID = rows[0][0]
        cur.execute(f"Update customer set Cash = {subtractValue} where ID = {updateID}")
        cur.execute("select * from customer")
        if (cur.execute(f"select * from customer where {To.value} = ID")):
            global transferID
            transferID = cur.fetchall()

        if len(transferID)==0:
            page.add(
                Row([
                    Text('Wrong ID')
                ],
                alignment=MainAxisAlignment.CENTER)
            )

        TransferAmount = transferID[0][3] + int(transfer.value)
        cur.execute(F"Update customer set Cash = {TransferAmount} where ID = {To.value}")
        page.add(
            Row([
                Text('Amount Transferred')
            ],alignment=MainAxisAlignment.CENTER)
        )
        con.commit()

    def Withdrawal(e):
        page.clean()
        global withdraw
        withdraw = TextField(
            label="Enter Amount",
            autofocus=True,
            border_color="transparent",
            icon=icons.MONEY_ROUNDED,
            content_padding=15,
        )
        page.add(
            Row(
                [
                    Container(
                        expand=True,
                        height=60,
                        bgcolor="#fdfdfd",
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        padding=padding.only(left=15, right=15),
                        content=IconButton(icons.HOME, on_click=FirstPage),
                    ),
                ],
            ),
            Row(
                [
                    Text("Withdraw Amount", size=20, weight="bold", font_family='San Fransisco'),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [withdraw],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=withdrawProcessing,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Withdraw",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=NewPage,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Go Back",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        ),
    
    def withdrawProcessing(e):
        TransferAmount = rows[0][3] - int(withdraw.value)
        TransferID = rows[0][0]

        cur.execute(F"Update customer set Cash = {TransferAmount} where ID = {TransferID}")
        con.commit()
        page.add(
            Row(
            [
                Text('Money Withdrawn')
            ],
            alignment=MainAxisAlignment.CENTER
            )
        )

    id = TextField(
        label="Enter ID",
        autofocus=True,
        border_color="transparent",
        icon=icons.CARD_MEMBERSHIP,
        content_padding=15,
    )
    password = TextField(
        label="Enter Password",
        autofocus=True,
        border_color="transparent",
        icon=icons.PASSWORD,
        content_padding=15,
        password=True,
        can_reveal_password=True,
    )
    name = TextField(
        label="Enter Name",
        autofocus=True,
        border_color="transparent",
        icon=icons.PERSON,
        content_padding=15,
    )
    cash = TextField(
        label="Initial Cash",
        autofocus=True,
        border_color="transparent",
        icon=icons.PERSON,
        content_padding=15,
    )
    page.add(
        Row(
            [
                Container(
                    expand=True,
                    height=60,
                    bgcolor="#fdfdfd",
                    border_radius=border_radius.only(top_left=15, top_right=15),
                    padding=padding.only(left=15, right=15),
                    content=IconButton(icons.HOME, on_click=FirstPage),
                ),
            ],
        ),
        Row(
            [
                Text("Login Account", size=20, weight="bold", font_family='San Fransisco'),
            ],
            alignment=MainAxisAlignment.CENTER,
        ),
        Row(
            [id],
            alignment=MainAxisAlignment.CENTER,
        ),
        Row(
            [password],
            alignment=MainAxisAlignment.CENTER,
        ),
        Row(
            [
                ElevatedButton(
                    on_click=FirstPage,
                    bgcolor="#081d33",
                    color="white",
                    content=Row(
                        controls=[
                            Text(
                                "Login",
                                size=13,
                                weight="bold", font_family='San Fransisco',
                            ),
                        ],
                    ),
                    style=ButtonStyle(
                        shape={
                            "": RoundedRectangleBorder(radius=6),
                        },
                        color={"": "white"},
                    ),
                    height=68,
                    width=195,
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
        ),
        Row(
            [
                ElevatedButton(
                    on_click=Register,
                    bgcolor="#081d33",
                    color="white",
                    content=Row(
                        controls=[
                            Text(
                                "Register",
                                size=13,
                                weight="bold", font_family='San Fransisco',
                            ),
                        ],
                    ),
                    style=ButtonStyle(
                        shape={
                            "": RoundedRectangleBorder(radius=6),
                        },
                        color={"": "white"},
                    ),
                    height=68,
                    width=195,
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
        ),
    ),

    def LoginPage(e):
        print(f"insert into customer values({id},'{password}','{name}',{cash})")
        cur.execute(
            f"insert into customer values({id.value},'{password.value}','{name.value}',{cash.value})"
        )
        con.commit()

        page.clean()
        page.add(
            Row(
                [
                    Container(
                        expand=True,
                        height=60,
                        bgcolor="#fdfdfd",
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        padding=padding.only(left=15, right=15),
                        content=IconButton(icons.HOME, on_click=FirstPage),
                    ),
                ],
            ),
            Row(
                [
                    Text("Login Account", size=20, weight="bold", font_family='San Fransisco'),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [id],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [password],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=FirstPage,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Login",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                [
                    ElevatedButton(
                        on_click=Register,
                        bgcolor="#081d33",
                        color="white",
                        content=Row(
                            controls=[
                                Text(
                                    "Register",
                                    size=13,
                                    weight="bold", font_family='San Fransisco',
                                ),
                            ],
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=6),
                            },
                            color={"": "white"},
                        ),
                        height=68,
                        width=195,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        ),

    page.update()
    pass


if __name__ == "__main__":
    ft.app(target=main)
