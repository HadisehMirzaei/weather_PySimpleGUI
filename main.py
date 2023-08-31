import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests
image_col = sg.Column([[sg.Image("", key="-IMAGE-", background_color="white")]])
info_col = sg.Column([
    [sg.Text('test', key="-LOCATION-", font="Calibri 30", background_color="#FF0000", text_color="#FFFFFF",
             pad=0, visible=False)],
    [sg.Text('test', key="-TIME-", font="Calibri 16", background_color="#000000", text_color="#FFFFFF",
             pad=0, visible=False)],
    [sg.Text('test', key="-TEMP-", font="Calibri 16", background_color="#FFFFFF", text_color="#000000",
             pad=(0, 10), visible=False)]
])
layout = [
    [sg.Input(key="-INPUT-"), sg.Button("enter", key="-BUTTON-")],
    [image_col, info_col]
    ]

window = sg.Window("weather", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break


