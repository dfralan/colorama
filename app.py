import random

random_number = random.randint(0,16777215)
hex_number =format(random_number,'x')
hex_full = '#' + hex_number
print('Eeeexito, look for me for',hex_full)
  
str(hex_number)
f = open(str(hex_full)+'.svg', 'a')
f.write('<?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="500px" height="500px" viewBox="0 0 700 700" version="1.1"><g><rect x="0" y="0" width="700" height="700" style="fill:#' + str(hex_number) + ';"/></g></svg>')
f.close()
