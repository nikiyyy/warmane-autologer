import subprocess
import pyautogui
import json
from time import sleep

def keyboard_type(word):
    for c in word:
        pyautogui.typewrite(c)

def file_reader():
    with open('credentials.txt') as f:
        json_data = json.loads(f.read())
        return json_data

def main():
    #read from file
    credentials = file_reader()
    path = credentials['c1']
    password = credentials['c2']
    
    #input credentials
    subprocess.run(f'start {path}', shell=True )
    sleep(5)
    keyboard_type(password)
    pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.press('esc')

if __name__ == "__main__":
    main()