

class Rotor:
    def __init__(self, name, ring_position) -> object:
        self.name = name
        self.wiring = self.select_rotor_wiring()
        self.ring_position = ring_position
        pass
    def select_rotor_wiring(self, configuration):
        """
        docstring
        """
        
        pass

class Reflector:
    def __init__(self, wiring) -> None:
        self.wiring = wiring
        pass

class Plugboard():
    def __init__(self, wiring) -> None:
        self.wiring =wiring
        pass

class Enigma:
    def __init__(self, configuration) -> None:
        self.rotors = self.set_rotors()
        self.reflector = configuration['reflector']
        self.plugboard = configuration['plugboard']
        pass
    
    @classmethod
    def set_rotors(self):
        """
        docstring
        """
        rotors = []
        rotors.append(Rotor(name = "rotor_1", ring_position= "1", ))
        
        pass

if __name__ == "__main__":
    while True:
        print("-------------------------")
        print("Enigma online, Please enter an option")
        print("1) Encrypt a message")
        print("2) Decrypt a message")
        print("3) Exit")
        print("-------------------------")
        input = int(input())
        match input:
            case 1:
                print("please enter a message to encrypt.")
                message = str(input).upper
                pass
            case 2:
                print("please enter a message to decrypt.")
                message = str(input).upper
                pass
            case 3:
                print("Exiting...")
                break
    pass