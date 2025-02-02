import time	
import easyocr
import pyautogui as pg
import numpy as np
import pygetwindow as gw
from deep_translator import GoogleTranslator

def translate(text):
    return translator.translate_batch(text)

def ocr_translate(ss):
    return translate(reader.readtext(np.array(ss), detail = 0))



source_language = 'ko'
target_language = 'en'
translator = GoogleTranslator(source=source_language, target=target_language)
reader = easyocr.Reader([source_language]) # this needs to run only once to load the model into memory

LiveCaptions = gw.getWindowsWithTitle('Live Captions')[0]

last_output = pg.screenshot(region=(LiveCaptions.left, LiveCaptions.top, LiveCaptions.width, LiveCaptions.height))
last_time = time.time()
while True:
    ss = pg.screenshot(region=(LiveCaptions.left, LiveCaptions.top, LiveCaptions.width, LiveCaptions.height))   
    # IDK I thinks this will make the pc be less stress when running :) 
    while True:                 #Delay if these outputs remain the same 
        current_output = ss
        if current_output == last_output:    # If the output is the same,...
            if time.time() - last_time > 1: # Output is the same for more than 1 second, translating...
                print(ocr_translate(ss))
                time.sleep(0.1)  
            elif time.time() - last_time > 2.5:   # Output is the same for more than 2.5 second, pause...
                time.sleep(3)   # Delay for 3 second b4 continuing
        else:   # If the output changes, continue processing
            last_time = time.time()  # Reset the time
            last_output = current_output  # Update the last output
        time.sleep(0.1)
        break  # A small delay to prevent excessive CPU usage  
    time.sleep(0.1)  
    
    
 