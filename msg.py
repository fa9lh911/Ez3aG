import pyautogui 
from time import sleep

msg = input("Enter Your Ms : ")
num_msg = int(input("Num Of Ms : "))
time_msg = float(input("Num Time Of ms :"))

for num in range (num_msg + 1 ) :
    pyautogui.typewrite(msg)
    sleep(time_msg)
    pyautogui.press('Enter')
    sleep(time_msg)
    
    