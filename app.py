import random
from selenium import webdriver
import os



def genColorama():
    while True:
        color = '#' + "%06x" % random.randint(0, 0xFFFFFF)
        color_file = color + '.svg'
        if color_file in os.listdir("Colors"):
            print("El " + color + " estaba repetido rey, sigooooooooooooooooooooooooooooo!")
            return genColorama()
        else:
            file = open('Colors/' + color_file, 'a')
            file.write('<?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="500px" height="500px" viewBox="0 0 500 500" version="1.1"><g><rect x="0" y="0" width="500" height="500" style="fill:' + color + ';"/></g></svg>')
            print('El color generado se llama ' + color)
            file.close()
genColorama()
