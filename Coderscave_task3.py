import tkinter as tk
from tkinter import messagebox
import random
import time
class TypingSpeedTester:





    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.text_to_type = self.generate_random_text()
        self.label_instruction = tk.Label(root, text="Type the following:")
        self.label_instruction.pack()
        self.text_display = tk.Text(root, height=5, width=50)
        self.text_display.insert(tk.END, self.text_to_type)
        self.text_display.config(state="disabled")
        self.text_display.pack()
        self.lbl_countdown = tk.Label(root, text="")
        self.lbl_countdown.pack()
        self.entry_user_input = tk.Entry(root, state="disabled")
        self.entry_user_input.pack()
        self.btn_start = tk.Button(root, text="Start Test", command=self.start_test)
        self.btn_start.pack()
        self.lbl_result = tk.Label(root, text="")
        self.lbl_result.pack()
        self.start_time = 0
    def generate_random_text(self):
        text_options = ["Hello Coderscave","Jai shree raam","Tomorrow is today"]
        return random.choice(text_options)
    def start_test(self):
        self.text_display.config(state="normal")
        self.text_display.delete(1.0, tk.END)  
        self.text_display.insert(tk.END, self.text_to_type)
        self.text_display.config(state="disabled")
        self.lbl_countdown.config(text="Get ready! Starting in 5 seconds...")
        self.root.after(5000, self.initiate_countdown)
        self.entry_user_input.config(state="disabled")
        self.btn_start.config(state="disabled")
    def initiate_countdown(self):
        self.lbl_countdown.config(text="Start typing now!,Press enter when done")
        self.entry_user_input.config(state="normal")
        self.entry_user_input.focus()  
        self.start_time = time.time()

        
        self.entry_user_input.bind("<Return>", self.check_input)
        self.btn_start.config(state="normal")  

    def check_input(self, event):
        user_input = self.entry_user_input.get()
        if user_input == self.text_to_type:
            elapsed_time = time.time() - self.start_time
            wpm = self.calculate_wpm(elapsed_time)
            self.lbl_result.config(text=f"Your typing speed: {wpm} WPM")
        else:
            
            messagebox.showinfo("Incorrect Text", "Please enter the correct text.")
            
            self.entry_user_input.delete(0, tk.END)
            self.entry_user_input.focus()

    def calculate_wpm(self, elapsed_time):
        words_per_minute = (len(self.text_to_type.split()) / elapsed_time) * 60
        return round(words_per_minute)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
