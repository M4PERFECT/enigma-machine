from turtle import position


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