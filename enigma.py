

import random
from typing import Self


class Rotor: 
    def __init__(self):
        self.position = self.setPosition()
        self.offset = self.setOffset()
        self.wiring = self.setWiring()
        self.rotation = self.setRotation()
        print(f"Rotor-position: {self.position}\n Rotor-offset: {self.offset}\n rotation: {self.rotation}\n Wiring: {''.join(self.wiring)}")
        
    def turn(self):
            self.rotation += 1
            if self.rotation == 27:
                self.rotation = 0    
            return self.rotation            
    def encrypt(self, letter):
            wiring = self.wiring
            orignalAlphabeticalOrder = ord(letter) - 96
            newLetter = wiring[orignalAlphabeticalOrder - 1]
            return newLetter
    def decrypt(self, letter):
            wiring = self.wiring
            encryptedAlphabeticalOrder = ord(letter) - 96
            orignalLetter = wiring[encryptedAlphabeticalOrder -1]
            return orignalLetter 

        
    @staticmethod
    def setPosition():
            print("Please enter the position of the rotor. (1-26)")
            position = int(input())
            return position
    
    @staticmethod
    def setOffset():
            print("Would you like set an offset? (Y/N)")
            response = input().lower() 
            if response == "y":
                print("Please enter the value of the rotor offset.")
                offset = int(input())
            else :
                print("setting a default offset (1 or 2)")
                offset = random.randint(1,2)
            return offset
    
    @staticmethod
    def setWiring():
            print("Would you like to input a wiring? (Y/N)")
            response = input().lower()
            if response != "y":
                wiring = []
                i_list = list("abcdefghijklmnopqrstuvwxyz")
                while len(i_list) > 0:
                        patternNumber = random.randint(0, (len(i_list)-1))
                        wiring.append(i_list[patternNumber])
                        i_list.pop(patternNumber)
            else:
                print("Please enter the wiring list. only 'a' format input." )
                wiring = list(input())
            return wiring
    
    @staticmethod
    def setRotation():
        rotation = random.randint(1,26)
        return rotation
    

class Plugboard:
    def __init__(self):
        self.wiring = self.setWiring()
        
    def swap_with_plugboard(letter, plugboard):
        return plugboard.get(letter, letter)

    @staticmethod
    def setWiring():
        wiring = {}
        alphabet = ["abcdefghijklmnopqrstuvwxyz"]
        keys = random.choices(alphabet, 10)
        values = alphabet.remove(keys)
        for i in keys:
            wiring.update(keys[i], values[i])
            values.remove(values[i])
        wiring.update(values)  
        print(wiring)  
        return wiring

class Reflector:
   def __init__(self):
    self.signal = []

class EnigmaMachine:
    
    plugboard = Plugboard()
    reflector = Reflector()

    def start(self, letter):
        self.rotor1.encrypt(letter)
        return letter
    def __init__(self):
        print("Please enter the first rotor's rotation.")
        # rotorRotation = int(input())
        # rotorWiring = list(input())
        self.rotor2 = Rotor()
        self.rotor3 = Rotor()
        self.rotor1 = Rotor()

        pass
def main():
 while(True):
    print("-------------------------")
    print("Enigma online. Please enter a option")
    print("1) Encrpty a letter.")
    print("2) Decrypt a leter.")
    print("3) Encrypt a passage.")
    print("4) Decrypt a passage.")
    print("5) Exit")
    option = int(input())

    match option:
     case 1:
          rotor1 = Rotor()
          print("Please input a letter to encrypt:")
          letter = input()
          print(f"The encrypted letter for {letter} is {rotor1.encrypt(letter)}")
     case 2:
          rotor1 = Rotor()
          print("Please input the letter to decrypt:")
          encryptedLetter = input()
          print(f"The orignal letter for {encryptedLetter} is {rotor1.decrypt(encryptedLetter)}")
     case 3:
          return 0
     case 4:
          return 0
     case 5:
          exit()












if __name__ == "__main__":
    main()
    
