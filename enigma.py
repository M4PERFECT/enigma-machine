

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
        self.offset = random.randint(1, 2)
        self.wiring = self.generate_wiring()
        self.notch = 27


    def get_rotor(self):
        return {
        "Rotor-position": self.position,
        "Rotor-offset": self.offset,
        "Wiring": self.wiring
        }
    
    def encryption_turn(self):
        self.position += 1
        if self.position == self.notch:
            self.position = 1
            return True
        return False
    
    def decryption_turn(self):
        self.position -= 1
        if self.position == 0:
            self.position = self.notch
            return True
        return False
    
    def turn(self):
        self.position += 1
        if self.position == self.notch:
            self.position = 1
            return True
        return False
    
    def encrypt(self, signal):
        wiring = self.wiring
        # print(f"{self.name} signal input is {signal}")
        signal_alphabetical_order = ord(signal) - 96 + self.position - 1
        if signal_alphabetical_order > 26:
            signal_alphabetical_order = 1
        if signal_alphabetical_order < 1:
            signal_alphabetical_order = 26
        new_signal = wiring.get(signal_alphabetical_order)
        # print(f"{self.name} signal output is {new_signal}")
        return new_signal

    def decrypt(self, signal):
        wiring = self.wiring
        # print(f"{self.name} signal input is {signal}")
        signal_alphabetical_order = ord(signal) - 96 - self.position + 1
        if signal_alphabetical_order > 26:
            signal_alphabetical_order = 1
        if signal_alphabetical_order < 1:
            signal_alphabetical_order = 26
        new_signal = wiring.get(str(signal_alphabetical_order))
        # print(f"{self.name} signal output is {new_signal}")
        return new_signal

    def set_position(self):
        position = 1
        # for i in position:
        #     self.turn()
        return position

    def generate_wiring(self):
        wiring = {}
        alphabets = list('abcdefghijklmnopqrstuvwxyz')
        keys = range(1, 27)
        for key, alphabet in zip(keys, alphabets):
            wiring[key] = alphabet
        return wiring   


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
        self.rotors = [Rotor() for _ in range(num_rotors)]
        self.reflector = Reflector()
        for index, rotor in enumerate(self.rotors):
            rotor.name = f"rotor{index + 1}"

    def get_engima(self):
        enigma_config = {
        'plugboard': self.plugboard.get_plugboard(),
        'rotors': [rotor.get_rotor() for rotor in self.rotors],
        'reflector': self.reflector.get_reflector()
        }
        return json.dumps(enigma_config, indent=4)

    def encrypt(self, signal):
        print(f"Input letter: {signal}")
        # signal = self.plugboard.swap_with_plugboard(signal)
        # print(f"Swapped with the plugboard: {signal}")
        turn_next_rotor = False
        for rotor in self.rotors:
            if rotor.name == "rotor1" or turn_next_rotor:
                turn_next_rotor = rotor.encryption_turn()
                print(f"Incrementing position: {rotor.name} to {rotor.position}")
            signal = rotor.encrypt(signal)
            print(f"Encrypted by the {rotor.name}: {signal}")
        signal = self.reflector.reflect_signal(signal)
        print(f"Reflected letter: {signal}")
        self.rotors.reverse()
        for rotor in self.rotors:
            signal = rotor.encrypt(signal)
            print(f"Encrypted 2nd time by {rotor.name}: {signal}")
        # signal = self.plugboard.swap_with_plugboard(signal)
        # print(f"Swapped with plugboad: {signal}")
        self.rotors.reverse()
        return signal
    
    def decrypt(self, signal):
        print(f"Input letter: {signal}")
        # signal = self.plugboard.swap_with_plugboard(signal)
        # print(f"Swapped with the plugboard: {signal}")
        turn_next_rotor = False
        for rotor in self.rotors:
            if rotor.name == "rotor1" or turn_next_rotor:
                turn_next_rotor = rotor.turn()
                print(f"decrementing position: {rotor.name} to {rotor.position}")
            signal = rotor.decrypt(signal)
            print(f"Decrypted by the {rotor.name}: {signal}")
        signal = self.reflector.reflect_signal(signal)
        print(f"Reflected letter: {signal}")
        self.rotors.reverse()
        for rotor in self.rotors:
            signal = rotor.decrypt(signal)
            print(f"Encrypted 2nd time by {rotor.name}: {signal}")
        # signal = self.plugboard.swap_with_plugboard(signal)
        # print(f"Swapped with plugboad: {signal}")
        self.rotors.reverse()
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
                print("Please input a signal to encrypt:")
                signals = input().lower()
                encrypted_signals = ''
                for signal in signals:
                    encrypted_signals += enigma_3.encrypt(signal)
                print(
                    f"The encrypted signal for {signals} is {encrypted_signals}")
                with open('enigma_config.json', 'w') as file:
                    file.write(enigma_3.get_engima())
            case 2:
                with open('enigma_config.json', 'r') as file:
                    config = json.load(file)
                wiring = config['plugboard']
                enigma_3.plugboard.set_wiring(wiring)
                rotor_configs = config['rotors']
                for i, rotor_config in enumerate(rotor_configs):
                    enigma_3.rotors[i].position = rotor_config["Rotor-position"]
                    enigma_3.rotors[i].offset = rotor_config["Rotor-offset"]
                    enigma_3.rotors[i].wiring = rotor_config["Wiring"]
                letter_mapping = config['reflector']
                enigma_3.reflector.letter_mapping = letter_mapping

                print("Please input a signal to decrypt:")
                signals = input().lower()
                signals_processed = list(signals)
                signals_processed.reverse()
                signals = ''.join(signals_processed)
                decrypted_signals = ''
                for signal in signals:
                    decrypted_signals += enigma_3.decrypt(signal)
                    processed_decrypted_signals = list(decrypted_signals)
                    processed_decrypted_signals.reverse()
                    decrypted_signals = ''.join(processed_decrypted_signals)
                print(
                    f"The encrypted signal for {signals} is {decrypted_signals}")
            case 3:
                exit()


if __name__ == "__main__":
    main()
