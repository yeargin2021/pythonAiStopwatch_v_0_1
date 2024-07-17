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