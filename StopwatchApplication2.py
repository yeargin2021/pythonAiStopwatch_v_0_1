import tkinter as tk
from datetime import datetime 

class StopWatch:
    def __init__(self):
        self.start_time = None
        self.running = False
        self.current_time = "00:00:00.00"

    def start(self):
        if not self.running:
            self.start_time = datetime.now()
            self.running = True

    def stop(self):
        if self.running:
            end_time = datetime.now()
            diff = end_time - self.start_time
            hours, rem = divmod(diff.seconds, 3600)
            minutes, seconds = divmod(rem, 60)
            self.current_time = "{:02d}:{:02d}:{:02d}.{:02d}".format(hours, minutes, seconds, diff.microseconds//10000)
            self.running = False 

    def reset(self):
        self.start_time = None
        self.running = False
        self.current_time = "00:00:00.00"


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.stopwatch = StopWatch()
        self.create_widgets()

    def create_widgets(self):
        self.time_label = tk.Label(self, text=self.stopwatch.current_time, font=("Helvetica", 24))
        self.time_label.pack()

        self.start = tk.Button(self, text="START", command=self.start_watch)
        self.start.pack(side="left")

        self.stop = tk.Button(self, text="STOP", command=self.stop_watch)
        self.stop.pack(side="left")