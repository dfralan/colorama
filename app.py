import random
import os



def genColorama():
    while True:
        random_number = random.randint(0,16777215)
        hex_number = format(random_number,'x')
        hex_full = '#' + hex_number + '.svg'

        if hex_full in os.listdir("Hexas"):
            print("El " + hex_full + " estaba repetido rey, we re alcahuete, sigooooooooooooooooooooooooooooo")
            return genColorama()        
        
        else:
            file = open('Hexas/'+hex_full, 'a')
            file.write('<?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="500px" height="500px" viewBox="0 0 500 500" version="1.1"><g><rect x="0" y="0" width="500" height="500" style="fill:#' + str(hex_number) + ';"/></g></svg>')
            print('Color generado, se llama ',hex_full)
            file.close()

genColorama()
