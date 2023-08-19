

import random
import json
# need to fix the position independence of the rotor's encryption/decryption

def generate_wiring(num_pairs=10):
    wiring = {}
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    keys = random.sample(alphabet, k=num_pairs)
    values_list = [letter for letter in alphabet if letter not in keys]
    values = random.sample(values_list, k=num_pairs)
    for key, value in zip(keys, values):
        wiring[key] = value
        wiring[value] = key
    return wiring


class Rotor:
    def __init__(self):
        self.name = str()
        self.signal = list()
        self.position = self.set_position()
        self.offset = self.set_offset()
        self.wiring = self.generate_wiring()
        self.rotation = self.set_rotation()
        
    def get_rotor(self):
        return {
        "Rotor-position": self.position,
        "Rotor-offset": self.offset,
        "rotation": self.rotation,
        "Wiring": ''.join(self.wiring)
        }
    
    def turn(self):
        self.rotation += 1
        if self.rotation == 27:
            self.rotation = 0
        self.wiring.insert(0, self.wiring.pop())
        return self.rotation
    
    def encrypt(self, signal):
        wiring = self.wiring
        signal_alphabetical_order = ord(signal) - 96
        new_signal = wiring[signal_alphabetical_order - 1]
        return new_signal

    def decrypt(self, signal):
        wiring = self.wiring
        signal_alphabetical_order = ord(signal) - 96
        new_signal = wiring[signal_alphabetical_order - 1]
        return new_signal

    @staticmethod
    def set_position():
        position = 1
        return position

    @staticmethod
    def set_offset():
        offset = random.randint(1, 2)
        return offset

    @staticmethod
    def generate_wiring():
        wiring = []
        i_list = list("abcdefghijklmnopqrstuvwxyz")
        while len(i_list) > 0:
            pattern_number = random.randint(0, (len(i_list)-1))
            wiring.append(i_list[pattern_number])
            i_list.pop(pattern_number)    
        return wiring

    @staticmethod
    def set_rotation():
        rotation = random.randint(1, 26)
        return rotation


class Plugboard:
    def __init__(self):
        self.signal = self.set_signal()
        self.wiring = self.generate_wiring()

    def get_plugboard(self):
        return self.wiring
    
    def swap_with_plugboard(self, signal):
        return self.wiring.get(signal, signal)

    @staticmethod
    def generate_wiring():
        wiring = generate_wiring(num_pairs=10)
        return wiring
    
    def set_wiring(self, wiring):
        self.wiring = wiring
        return 

    @staticmethod
    def set_signal():
        return list()


class Reflector:
    def __init__(self):
        self.signal = self.set_signal()
        self.letter_mapping = self.generate_letter_mapping()

    def get_reflector(self):
        return self.letter_mapping
    
    def set_letter_mapping(self, letter_mapping):
        self.letter_mapping = letter_mapping
        return
    
    def reflect_signal(self, signal):
        return self.letter_mapping.get(signal, signal)
    
    @staticmethod
    def set_signal():
        signal = list()
        return signal

    @staticmethod
    def generate_letter_mapping():
        letter_mapping = generate_wiring(num_pairs=13)
        return letter_mapping


class EnigmaMachine:
    def __init__(self, num_rotors):
        self.plugboard = Plugboard()
        self.rotors = []
        for i in range(1, num_rotors + 1):
            rotor = Rotor()
            rotor.name = "rotor" + str(i)
            self.rotors.append(rotor)
            print(f"rotor created. {rotor.name} ")
        self.reflector = Reflector()

    def get_engima(self):
        enigma_config = {
        'plugboard': self.plugboard.get_plugboard(),
        'rotors': [rotor.get_rotor() for rotor in self.rotors],
        'reflector': self.reflector.get_reflector()
        }
        return json.dumps(enigma_config, indent=4)

    def encrypt(self, signal):
        signal = self.plugboard.swap_with_plugboard(signal)
        for rotor in self.rotors:
            signal = rotor.encrypt(signal)
            rotor.turn()
        signal = self.reflector.reflect_signal(signal)
        self.rotors.reverse()
        for rotor in self.rotors:
            signal = rotor.encrypt(signal)
        signal = self.plugboard.swap_with_plugboard(signal)
        return signal
    
    def decrypt(self, signal):
        signal = self.plugboard.swap_with_plugboard(signal)
        for rotor in self.rotors:
            signal = rotor.decrypt(signal)
            rotor.turn()
            print(f"Rotor rotated. {rotor.position}")
        signal = self.reflector.reflect_signal(signal)
        self.rotors.reverse()
        for rotor in self.rotors:
            signal = rotor.decrypt(signal)
        signal = self.plugboard.swap_with_plugboard(signal)
        return signal


def main():
    while (True):
        print("------------------------------------")
        print("Enigma online. Please enter a option")
        print("1) Encrpty a signal.")
        print("2) Decrypt a signal.")
        print("3) Exit.")
        print("------------------------------------")

        option = int(input())

        match option:
            case 1:
                enigma_3 = EnigmaMachine(num_rotors=3)
                with open('enigma_config.json', 'w') as file:
                    file.write(enigma_3.get_engima())
                print("Please input a signal to encrypt:")
                signals = input().lower()
                encrypted_signals = ''
                for signal in signals:
                    encrypted_signals += enigma_3.encrypt(signal)
                print(
                    f"The encrypted signal for {signals} is {encrypted_signals}")
            case 2:
                with open('enigma_config.json', 'r') as file:
                    config = json.load(file)
                wiring = config['plugboard']
                enigma_3.plugboard.set_wiring(wiring)
                rotor_configs = config['rotors']
                for i, rotor_config in enumerate(rotor_configs):
                    enigma_3.rotors[i].position = rotor_config["Rotor-position"]
                    enigma_3.rotors[i].offset = rotor_config["Rotor-offset"]
                    enigma_3.rotors[i].rotation = rotor_config["rotation"]
                    enigma_3.rotors[i].wiring = list(rotor_config["Wiring"])
                letter_mapping = config['reflector']
                enigma_3.reflector.letter_mapping = letter_mapping

                print("Please input a signal to decrypt:")
                signals = input().lower()
                decrypted_signals = ''
                for signal in signals:
                    decrypted_signals += enigma_3.decrypt(signal)
                print(
                    f"The encrypted signal for {signals} is {decrypted_signals}")
            case 3:
                exit()


if __name__ == "__main__":
    main()
