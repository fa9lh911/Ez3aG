import pyautogui 
from time import sleep

msg = input("fahad : ")
num_msg = int(input("+966541074393: "))
time_msg = float(input("100h :"))

for num in range (num_msg + 1 ) :
    pyautogui.typewrite(msg)
    sleep(time_msg)
    pyautogui.press('Enter')
    sleep(time_msg)
    
    
