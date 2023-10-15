import tkinter as tk
import sounddevice as sd
import numpy as np
import wave
import os
from datetime import datetime

class VoiceRecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice Recorder")

        self.record_button = tk.Button(self.master, text="Record", command=self.start_recording)
        self.record_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_recording)
        self.stop_button.pack(pady=10)
        self.stop_button.config(state=tk.DISABLED)

    def start_recording(self):
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.frames = []
        self.stream = sd.InputStream(callback=self.callback)
        self.stream.start()

    def stop_recording(self):
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        self.stream.stop()
        self.stream.close()

        self.save_recording()

    def callback(self, indata, frames, time, status):
        if status:
            print(status, flush=True)
        self.frames.append(indata.copy())

    def save_recording(self):
        if not os.path.exists("recordings"):
            os.makedirs("recordings")

        filename = f"recordings/recording_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"
        wavefile = wave.open(filename, 'wb')
        wavefile.setnchannels(1)
        wavefile.setsampwidth(2)
        wavefile.setframerate(44100)
        wavefile.writeframes(b''.join(self.frames))
        wavefile.close()

        print(f"Recording saved as {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()
