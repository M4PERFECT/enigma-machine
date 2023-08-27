from os import remove
from readline import append_history_file
import signal
from turtle import position
from webbrowser import get


def turn():
        position += 1
        wiring = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
        print("turned")
        if position == notch:
           position = 1
           new_wiring = wiring.copy()
           new_wiring.pop(1)
           
            return True
        return False
def wiring_rotation(wiring):
     wiring = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
     item = wiring.popitem()
     print(item)
     print(wiring.keys)
     return wiring

def set_position():
        wiring = {}
        position = 3
        for i in position:
            wiring.insert(0, .wiring.pop())
        return position

def encryption():
     position = 4
     signal = 'a'
     wiring = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
     signal_alphabetical_order = ord(signal) - 96 + position - 1
     new_signal = wiring.get(signal_alphabetical_order)
     print(new_signal)
     print(signal_alphabetical_order)

def decryption():
     position = 4
     signal = 'd'
     wiring = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
     signal_alphabetical_order = ord(signal) - 96 - position + 1
     new_signal = wiring.get(signal_alphabetical_order)
     print(new_signal)
     print(signal_alphabetical_order)

def reflector_encryption(){
     wiring = {"y": "z","z": "y","l": "q","q": "l","v": "t","t": "v","d": "f","f": "d","h": "e","e": "h","n": "g","g": "n","r": "m","m": "r","k": "s","s": "k","a": "j","j": "a","x": "w","w": "x","p": "i","i": "p","o": "c","c": "o","b": "u","u": "b"}
     signal = "L"
     signal = signal.lower()
     print(wiring.get(signal, signal))

}

def setting_wiring(){
     orignal = tuple(input())
     alpha = ['E', 'A', 'K', 'B', 'M', 'C', 'F', 'D', 'L', 'E', 'G', 'F', 'D', 'G', 'Q', 'H', 'V', 'I', 'Z', 'J', 'N', 'K', 'T', 'L', 'O', 'M', 'W', 'N', 'Y', 'O', 'H', 'P', 'X', 'Q', 'U', 'R', 'S', 'S', 'P', 'T', 'A', 'U', 'I', 'V', 'B', 'W', 'R', 'X', 'C', 'Y', 'J', 'Z']
     while i <= len(alpha):
          for a in alpha:
               b = a
               b.append()
               print(b)
     
     print(orignal) 
     }