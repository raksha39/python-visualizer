# Contents of /simple-sorting-visualizer/simple-sorting-visualizer/src/main.py

import tkinter as tk
from gui.main_window import MainWindow

def main():
    root = tk.Tk()
    root.title("Simple Sorting Visualizer")
    root.geometry("800x600")
    
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()