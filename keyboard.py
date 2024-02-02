import time
import Quartz

command_keys = {'a': 0, 's': 1, 'd': 2, 'f': 3, 'h': 4, 'g': 5, 'z': 6, 'x': 7, 'c': 8, 'v': 9, 'b': 11, 'q': 12, 'w': 13, 'e': 14, 'r': 15, 'y': 16, 't': 17, '1': 18, '2': 19, '3': 20, '4': 21, '6': 22, '5': 23, '=': 24, '9': 25, '7': 26, '-': 27, '8': 28, '0': 29, ']': 30, 'o': 31, 'u': 32, '[': 33, 'i': 34, 'p': 35, 'l': 37, 'j': 38, "'": 39, 'k': 40, ';': 41, '\\': 42, ',': 43, '/': 44, 'n': 45, 'm': 46, '.': 47, '`': 50, 'k.': 65, 'k*': 67, 'k+': 69, 'kclear': 71, 'k/': 75, 'k\n': 76, 'k-': 78, 'k=': 81, 'k0': 82, 'k1': 83, 'k2': 84, 'k3': 85, 'k4': 86, 'k5': 87, 'k6': 88, 'k7': 89, 'k8': 91, 'k9': 92, '\n': 36, '\t': 48, ' ': 49, 'del': 51, 'delete': 51, 'esc': 53, 'escape': 53, 'cmd': 55, 'command': 55, 'shift': 56, 'caps lock': 57, 'option': 58, 'ctrl': 59, 'control': 59, 'right shift': 60, 'rshift': 60, 'right option': 61, 'roption': 61, 'right control': 62, 'rcontrol': 62, 'fun': 63, 'function': 63, 'f17': 64, 'volume up': 72, 'volume down': 73, 'mute': 74, 'f18': 79, 'f19': 80, 'f20': 90, 'f5': 96, 'f6': 97, 'f7': 98, 'f3': 99, 'f8': 100, 'f9': 101, 'f11': 103, 'f13': 105, 'f16': 106, 'f14': 107, 'f10': 109, 'f12': 111, 'f15': 113, 'help': 114, 'home': 115, 'pgup': 116, 'page up': 116, 'forward delete': 117, 'f4': 118, 'end': 119, 'f2': 120, 'page down': 121, 'pgdn': 121, 'f1': 122, 'left': 123, 'right': 124, 'down': 125, 'up': 126}

hotkeys = {}
def add_hotkey(key, callback):
    hotkeys[command_keys[key]] = callback

def press(key, sleep=0.01):
    print('pressing')
    Quartz.CGEventPost(
        Quartz.kCGSessionEventTap,
        Quartz.CGEventCreateKeyboardEvent(None, command_keys[key], True)
    )
    time.sleep(sleep)
    Quartz.CGEventPost(
        Quartz.kCGSessionEventTap,
        Quartz.CGEventCreateKeyboardEvent(None, command_keys[key], False)
    )

def keyPressCallback(proxy, type, event, refcon):
    if type == Quartz.kCGEventKeyDown:
        key = Quartz.CGEventGetIntegerValueField(event, Quartz.kCGKeyboardEventKeycode)
        print(key)
        if key in hotkeys:
            print(key, hotkeys)
            hotkeys[key]()

tap = Quartz.CGEventTapCreate(
    Quartz.kCGHIDEventTap,
    Quartz.kCGHeadInsertEventTap,
    Quartz.kCGEventTapOptionListenOnly,
    Quartz.CGEventMaskBit(Quartz.kCGEventKeyDown), # 2
    keyPressCallback,
    None
)

runLoopSource = Quartz.CFMachPortCreateRunLoopSource(Quartz.kCFAllocatorDefault, tap, 0)
Quartz.CFRunLoopAddSource(
    Quartz.CFRunLoopGetCurrent(),
    runLoopSource,
    Quartz.kCFRunLoopCommonModes
)
Quartz.CGEventTapEnable(tap, True)
def start():
    Quartz.CFRunLoopRun()