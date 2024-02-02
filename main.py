from threading import Thread
import tkinter as tk
import keyboard
import time


class KeyPresser:
    def __init__(self):
        self.activated = False
        self.window = tk.Tk()
        self.hotkey = tk.StringVar(value="f5")
        self.key = tk.StringVar(value="f")
        # actionType: tap, hold
        self.actionType = tk.StringVar(value="tap")
        self.holdDuration = tk.IntVar(value=1)
        self.interval = tk.IntVar(value=1)
    
    def change_activated(self):
        print('changing')
        self.activated = False if self.activated else True
    
    def start_gui(self):
        self.window.title("Key presser")
        self.window.geometry("300x300")
        tk.Label(master=self.window, text="Key:").pack()
        tk.OptionMenu(self.window, self.key, *keyboard.command_keys.keys()).pack()
        tk.Label(master=self.window, text="Hotkey:").pack()
        tk.OptionMenu(self.window, self.hotkey, *keyboard.command_keys.keys()).pack()
        tk.Label(master=self.window, text="Action type:").pack()
        tk.OptionMenu(self.window, self.actionType, "tap", "hold").pack()
        tk.Label(master=self.window, text="Hold duration (seconds):").pack()
        tk.Entry(master=self.window, textvariable=self.holdDuration).pack()
        tk.Label(master=self.window, text="Interval (seconds):").pack()
        tk.Entry(master=self.window, textvariable=self.interval).pack()
        self.window.mainloop()

    def start_presser(self):
        keyboard.add_hotkey(self.hotkey.get(), self.change_activated)
        while True:
            if self.activated:
                if self.actionType.get() == "tap":
                    keyboard.press(self.key.get())
                else:
                    keyboard.press(self.key.get(), self.holdDuration.get())
                time.sleep(self.interval.get())

    def start(self):
        Thread(target=keyboard.start).start()
        Thread(target=self.start_presser).start()
        self.start_gui()

KeyPresser().start()