import pyautogui

pyautogui.PAUSE = 2

# abrir a ferramenta/sistema/programa
pyautogui.press("winleft")
pyautogui.write("google")
pyautogui.press("enter")
pyautogui.write("consegui realizar o meu primeiro bot")
pyautogui.keyDown("ctrl")
pyautogui.press("w")
pyautogui.keyUp("ctrl")