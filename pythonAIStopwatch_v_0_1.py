"""
    PYTHON AI STOPWATCH V. 0.1
    Copyright (C) 2024  Tommy H. Yeargin, Jr.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

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
            self.current_time = "{:02d}:{:02d}:{:02d}.{:02d}".format(hours, minutes, seconds,
                                                                     diff.microseconds // 10000)
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

        self.reset = tk.Button(self, text="RESET", command=self.reset_watch)
        self.reset.pack(side="left")

    def start_watch(self):
        self.stopwatch.start()
        self.update_time()

    def stop_watch(self):
        self.stopwatch.stop()

    def reset_watch(self):
        self.stopwatch.reset()
        self.time_label.config(text=self.stopwatch.current_time)

    def update_time(self):
        if self.stopwatch.running:
            current_time = datetime.now()
            diff = current_time - self.stopwatch.start_time
            hours, rem = divmod(diff.seconds, 3600)
            minutes, seconds = divmod(rem, 60)
            new_time = "{:02d}:{:02d}:{:02d}.{:02d}".format(hours, minutes, seconds, diff.microseconds // 10000)
            self.time_label.config(text=new_time)
            self.after(10, self.update_time)


root = tk.Tk()
root.title("Stopwatch")
app = Application(master=root)
app.mainloop()
