
class Rotor: 
    position = 0
    offset = 0
    rotation = 0

    def turn():
        return 0
    def encrypt():
        return 0

class Plugboard:
    wiring = []

class Reflector:
    signal = []

class EnigmaMachine:
    rotor1 = Rotor()
    rotor2 = Rotor()
    rotor3 = Rotor()
    plugboard = Plugboard()
    reflector = Reflector()

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
          return 0
     case 2:
          return 0
     case 3:
          return 0
     case 4:
          return 0
     case 5:
          exit()












if __name__ == "__main__":
    main()
    
