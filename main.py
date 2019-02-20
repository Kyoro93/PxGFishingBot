import numpy as np
import pyscreenshot as ImageGrab
import cv2
import pyautogui
import time

gameCoords = [2018, 67, 2069, 121]
start_time = 0

quant_pescas = 0
tempo_pesca = 0


def iniciarPesca():
    global start_time

    pyautogui.press('f12')
    time.sleep(0.5)
    pyautogui.click(2045, 80)
    start_time = time.time()


def pescar():
    global start_time
    tempo = time.time() - start_time
    print("Tempo da ultima pesca: " + str(time.time() - start_time))
    pyautogui.press('f5')
    pyautogui.press('f6')
    pyautogui.press('f7')
    pyautogui.press('f8')
    pyautogui.press('f12')
    time.sleep(1.5)
    pyautogui.press('f12')
    time.sleep(0.5)
    pyautogui.click(2045, 80)
    start_time = time.time()
    contabilizarTempoPesca(tempo)


def contabilizarTempoPesca(tempo):
    global quant_pescas, tempo_pesca
    quant_pescas += 1
    tempo_pesca += tempo
    print("Tempo de pesca: " + str(tempo_pesca/60) + " minutos")
    print("Quantidade de pescas: " + str(quant_pescas))
    print("Tempo medio entre pescas: " + str(tempo_pesca/quant_pescas))


time.sleep(3)
iniciarPesca()

while True:
    time.sleep(0.5)
    try:
        screen = np.array(ImageGrab.grab(bbox=gameCoords))
        #screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        if screen.sum() > 800000:
            pescar()
            time.sleep(3)

    except Exception as e:
        if (time.time() - start_time) > 20:
            iniciarPesca()
        print(e)
        pass
