import pyautogui
#pip install pyautogui
import PySimpleGUI as sg
#pip install pysimplegui
import time

#Add a touch of color
#sg.theme_previewer()

sg.theme('LightGrey1')

def msgBloco(msg):
    nome = str(msg)
    pyautogui.PAUSE = 2
    pyautogui.press('winleft')
    pyautogui.write('bloco')
    pyautogui.press('enter')
    pyautogui.write("BEM VINDO A SEMANA DA CASA ABERTA DA ETEC DE POA, FOI UM PRAZER ")
    pyautogui.write(nome.upper())

def entraNav(video):
    pyautogui.PAUSE = 2
    pyautogui.press("winleft")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    pyautogui.write("youtube.com")
    pyautogui.press("enter")
    for c in range(1, 5):
        pyautogui.press("tab")
    pyautogui.write(video)
    pyautogui.press("enter")
    for c in range(1, 6):
        pyautogui.press("tab")
    pyautogui.press("enter")

def calculadora(num, num2, sinal): 
    pyautogui.PAUSE = 2
    number = str(num)
    number2 = str(num2)
    operacao = str(sinal)
    pyautogui.press("winleft")
    pyautogui.write("calculadora")
    pyautogui.press("enter")
    pyautogui.write(number2)
    pyautogui.write(operacao)
    pyautogui.write(number)
    pyautogui.write("=")

def jogoCobra():
    pyautogui.press("winleft")
    time.sleep (1)
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep (1)
    pyautogui.write("jogo da cobrinha")
    pyautogui.press("enter")
    for c in range(1, 23):
        time.sleep (0.25)
        pyautogui.press("tab")
    pyautogui.press("enter")
    for c in range(1, 4):
        time.sleep (0.5)
        pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep (2)
    pyautogui.press("right")
    time.sleep (1)
    pyautogui.press("up")
    time.sleep (0.5)
    pyautogui.press("left")
    time.sleep (0.5)
    pyautogui.press("down")
    time.sleep (0.5)
    pyautogui.press("right")
    time.sleep (1)
    pyautogui.press("up")
    time.sleep (0.5)
    pyautogui.press("left")
    time.sleep (0.5)
    pyautogui.press("down")
    time.sleep (0.5)
    pyautogui.press("left")
    time.sleep (1)
    pyautogui.press("up")
    time.sleep (0.5)
    pyautogui.press("right")
    time.sleep (0.75)
    pyautogui.press("down")
    time.sleep (1)
    pyautogui.press("left")
    time.sleep (1)
    pyautogui.press("up")
    time.sleep (1)
    pyautogui.press("right")
    time.sleep (1.25)
    pyautogui.press("down")
    time.sleep (1)
    pyautogui.press("left")
    time.sleep (0.75)
    pyautogui.press("up")
    time.sleep (1.25)
    pyautogui.press("right")
    time.sleep (1)
    pyautogui.press("down")
    time.sleep (1.3)
    pyautogui.press("left")
    time.sleep (1)
    pyautogui.press("up")
    time.sleep (0.6)
    pyautogui.press("right")
    time.sleep (1)
    pyautogui.press("down")
    time.sleep (1.5)
    pyautogui.press("left")

layout_Principal = [  [sg.Text('ESCOLHA UMA TAREFA: ')],
            [sg.Button('MENSAGEM NO BLOCO')],
            [sg.Button('ENTRAR NO YOUTUBE')],
            [sg.Button('JOGO DA COBRINHA')],
            [sg.Button('PLANILHA DO WENDELL')],
            [sg.Button('CALCULADORA')],
            [sg.Button('CANCELAR')],

        ]

layout_Nome = [[sg.Text('DIGITE SEU NOME: ')],
            [sg.Input()],
            [sg.Button('OK'), sg.Button('CANCELAR')]
        ]

layout_Video = [[sg.Text('DIGITE O NOME DO VIDEO: ')],
            [sg.Input()],
            [sg.Button('ASSISTIR'), sg.Button('CANCELAR')]
        ]

layout_Calculadora = [[sg.Text("DIGITE O PRIMEIRO NUMERO: ")],
            [sg.Input()],
            [sg.Text("DIGITE O SEGUNDO NUMERO: ")],
            [sg.Input()],
            [sg.Text("DIGITE O SINAL DA OPERAÇAO: ")],
            [sg.Input()],
            [sg.Button('OK'), sg.Button('CANCELAR')]
]

# Create the Window
window = sg.Window('TAREFAS AUTONOMAS', layout_Principal)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()#event is button clicked / values is inputs fields 
    if event == sg.WIN_CLOSED or event == 'CANCELAR': # if user closes window or clicks cancel
        break
    if event == 'MENSAGEM NO BLOCO':
        window = sg.Window('TAREFAS AUTONOMAS', layout_Nome)
        event, values = window.read()
    if event == 'OK':
        nome = values[0]     
        msgBloco(nome)
        break
    if event == 'ENTRAR NO YOUTUBE':
        window = sg.Window('TAREFAS AUTONOMAS', layout_Video)
        event, values = window.read()
    if event == 'ASSISTIR':
        video = values[0]     
        entraNav(video)
        break
    if event == 'CALCULADORA':
        window = sg.Window('TAREFAS AUTONOMAS', layout_Calculadora)
        event, values = window.read()
    if event == 'OK':
        num = values[1]
        num2 = values[0]
        sinal = values[2]
        calculadora(num, num2, sinal)
        break
    if event == 'JOGO DA COBRINHA':
        jogoCobra()