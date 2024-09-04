'''
Crie um programa que automatize uma busca na Internet por videoaulas sobre Python no Youtube.
'''

import pyautogui as auto
import time

auto.PAUSE = 0.5

auto.press('win')
auto.write('firefox')
auto.press('enter')
auto.hotkey('alt','space')
auto.press('x')
auto.write('youtube.com.br')
auto.press('enter')

time.sleep(2)

for i in range(4):
    auto.press('tab')

auto.write('Python')
auto.press('enter')