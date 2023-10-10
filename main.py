import tkinter as tk
from tkinter import ttk
from gui import MovieRecommenderApp

def main():
    root = tk.Tk()
    app = MovieRecommenderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
