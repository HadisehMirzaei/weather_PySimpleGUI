import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests

def get_weather_data(location):
    url =f"https://www.google.com/search?q=weather+{location.replace(' ','')}"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    html = session.get(url)

    # create a new soup
    soup = bs(html.text, "html.parser")
    time = soup.find("div", attrs={'id': 'wob_dts'}).text
    weather = soup.find("span", attrs={'id': 'wob_dc'}).text
    temp = soup.find("span", attrs={'id': 'wob_tm'}).text
    return time, weather, temp


sg.theme("reddit")
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
    if event == "-BUTTON-":
        time, weather, temp = get_weather_data(values["-INPUT-"])
        window["-LOCATION-"].update(values["-INPUT-"], visible=True)
        window["-TIME-"].update(time, visible=True)
        window["-TEMP-"].update(f"{temp}\u2103 ({weather})", visible=True)
        window["-IMAGE-"].update(f"symbols/sun.png")
        # sun
        


window.close()

