# Escrever um texto com numeros
from pyfirmata import Arduino
import lcd
import time

board=Arduino ('COM6')
lcd.escrever(board, 0, 0, '3 DIA PYTHON')
lcd.escrever(board, 0, 1, 'SEJA BEM-VINDO')
time.sleep(5.0)
lcd.escrever(board, 0, 0, 'ESTOU'+3*' FELIZ')
lcd.escrever(board, 0, 1, 'EM RECEBE-LO    ')
time.sleep(100.0)
lcd.limpar(board)
board.exit()