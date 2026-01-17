import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()

# Enable macros 
macros = Macros()
keyboard.modules.append(macros)

# ===== PIN DEFINITIONS =====
# Each key connects GPIO → GND (active low)

PINS = [
    board.GP0,  # Key 1
    board.GP1,  # Key 2
    board.GP2,  # Key 3
    board.GP3,  # Key 4
    board.GP4,  # Key 5
    board.GP5,  # Key 6
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# ===== KEYMAP =====
keyboard.keymap = [
    [
        KC.N1,     # Key 1 → "1"
        KC.N2,     # Key 2 → "2"
        KC.N3,     # Key 3 → "3"
        KC.N4,     # Key 4 → "4"
        KC.N5,     # Key 5 → "5"
        KC.ENTER,  # Key 6
    ]
]

if __name__ == "__main__":
    keyboard.go()
