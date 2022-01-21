from threading import Thread
from time import sleep

vetor = ["a", "b", "4", "5", "6", "x", "c", "f", "g", "h", "z", "u", "9"]
ascii_values = []

def threadedNumero(arg):
    for character in vetor:
        ascii_values.append(ord(character))
    try:
        for i in range(arg):
            print("Thread Numero funcionando")
            if ascii_values[i] >=48 and ascii_values[i] <=57: 
                if i+2 < len(ascii_values) -1:
                    if ascii_values[i] == ascii_values[i+1] -1 and ascii_values[i] == ascii_values[i+2] - 2:
                        print(f'Tem 3 números consecutivos: {chr(ascii_values[i])}, {chr(ascii_values[i + 1])}, {chr(ascii_values[i + 2])}')   
                        #removendo do vetor
                        del ascii_values[i]
                        del ascii_values[i]
                        del ascii_values[i]                
            sleep(1) 
    except:
        print('', end='')    
def threadedLetras(arg):
    try:
        for i in range(arg):      
            print("Thread letras funcionando")                          
            if ascii_values[i] >=97 and ascii_values[i] <=122: 
                if i+2 < len(ascii_values) -1:
                    if ascii_values[i] == ascii_values[i+1] -1 and ascii_values[i] == ascii_values[i+2] - 2:
                        print(f'Tem 3 letras consecutivas: {chr(ascii_values[i])}, {chr(ascii_values[i + 1])}, {chr(ascii_values[i + 2])}')      
                        #removendo do vetor
                        del ascii_values[i]
                        del ascii_values[i]
                        del ascii_values[i]
            sleep(1)
    except:
        print('', end='')

if __name__ == "__main__":
    thread = Thread(target = threadedNumero, args = (len(vetor), ))
    thread2 = Thread(target = threadedLetras, args = (len(vetor), ))
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()
    
    newVetor = []
    for character in ascii_values:
        newVetor.append(chr(character))
    print (newVetor)
    print("\nThread finished...exiting")