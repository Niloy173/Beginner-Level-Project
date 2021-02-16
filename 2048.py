# Run the program and Play the Game
# Need Webdriver in this case I'm using Firefox

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

def play_2048():

    browser = webdriver.Firefox()

    keys = [Keys.UP,Keys.DOWN,Keys.RIGHT,Keys.LEFT]

    try:
        browser.get('https://play2048.co/')

        status_keys = browser.find_element_by_class_name('game-container')
        htmlelm = browser.find_element_by_css_selector('html')

        while status_keys.text !='Game Over!':

            htmlelm.send_keys(keys[random.randint(0,3)])
            status_keys = browser.find_element_by_class_name('game-container')

        score = browser.find_element_by_class_name('score-container').text

        print(f'game score : {score}')


    except Exception as error:
        print('The error is %s ' %(error))


if __name__ == '__main__':
    
    play_2048()



        
