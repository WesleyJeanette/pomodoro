import tkinter as tk
from tkinter import ttk
import time

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x250")

        # Timer variables
        self.time_left = tk.IntVar(value=1500)  # Default 25 min
        self.running = False

        # Preset times (in seconds)
        self.presets = {
            "25 min": 1500,
            "15 min": 900,
            "5 min": 300,
            "1 min": 60
        }

        self.create_widgets()
        self.update_timer()

    def create_widgets(self):
        # Timer display
        self.timer_label = ttk.Label(
            self.root,
            text="25:00",
            font=('Helvetica', 48)
        )
        self.timer_label.pack(pady=20)

        # Preset buttons
        preset_frame = ttk.Frame(self.root)
        preset_frame.pack()

        for text, secs in self.presets.items():
            btn = ttk.Button(
                preset_frame,
                text=text,
                command=lambda s=secs: self.set_time(s)
            )
            btn.pack(side=tk.LEFT, padx=5)

        # Manual time entry
        manual_frame = ttk.Frame(self.root)
        manual_frame.pack(pady=10)

        ttk.Label(manual_frame, text="Minutes:").pack(side=tk.LEFT)
        self.manual_entry = ttk.Entry(manual_frame, width=5)
        self.manual_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(
            manual_frame,
            text="Set",
            command=self.set_manual_time
        ).pack(side=tk.LEFT)

        # Control buttons
        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=10)

        self.start_btn = ttk.Button(
            control_frame,
            text="Start",
            command=self.start_timer
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.pause_btn = ttk.Button(
            control_frame,
            text="Pause",
            command=self.pause_timer,
            state=tk.DISABLED
        )
        self.pause_btn.pack(side=tk.LEFT, padx=5)

        ttk.Button(
            control_frame,
            text="Reset",
            command=self.reset_timer
        ).pack(side=tk.LEFT, padx=5)

    def set_time(self, seconds):
        self.time_left.set(seconds)
        self.update_display()

    def set_manual_time(self):
        try:
            minutes = int(self.manual_entry.get())
            self.set_time(minutes * 60)
        except ValueError:
            pass  # Ignore invalid input

    def start_timer(self):
        self.running = True
        self.start_btn.config(state=tk.DISABLED)
        self.pause_btn.config(state=tk.NORMAL)

    def pause_timer(self):
        self.running = False
        self.start_btn.config(state=tk.NORMAL)
        self.pause_btn.config(state=tk.DISABLED)

    def reset_timer(self):
        self.running = False
        self.set_time(self.time_left.get())  # Reset to current set time
        self.start_btn.config(state=tk.NORMAL)
        self.pause_btn.config(state=tk.DISABLED)

    def update_timer(self):
        if self.running and self.time_left.get() > 0:
            self.time_left.set(self.time_left.get() - 1)
            self.update_display()

        self.root.after(1000, self.update_timer)  # Update every second

    def update_display(self):
        mins, secs = divmod(self.time_left.get(), 60)
        self.timer_label.config(text=f"{mins:02d}:{secs:02d}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
