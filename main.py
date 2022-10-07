import PySimpleGUI as sg

sg.theme('DarkTeal9')

layout=[
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Name',size=(15,1)),sg.InputText(key='Name')],
    [sg.Submit(),sg.Exit()]
]

window = sg.Window('Simple data entry form',layout)

while True:
    event, values = window.read()
    if event