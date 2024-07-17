import tkinter as tk
from datetime import datetime


class StopWatch:
    def __init__(self):
        self.start_time = None
        self.running = False
        self.current_time = "00:00:00"

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
            self.current_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            self.running = False

    def reset(self):
        self.start_time = None
        self.running = False
        self.current_time = "00:00:00"


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.start = tk.Button(self, text="START", command=self.start_watch)
        self.start.pack(side="left")

        self.stop = tk.Button(self, text="STOP", command=self.stop_watch)
        self.stop.pack(side="left")

        self.reset = tk.Button(self, text="RESET", command=self.reset_watch)
        self.reset.pack(side="left")

    def start_watch(self):
        self.stopwatch.start()
        self.after(1000, self.update_time)

    def stop_watch(self):
        self.stopwatch.stop()

    def reset_watch(self):
        self.stopwatch.reset()

    def update_time(self):
        if self.stopwatch.running:
            self.after(1000, self.update_time)
        self.time_display.config(text=self.stopwatch.current_time)


root = tk.Tk()
app = Application(master=root)
app.mainloop()