import sys
import tkinter as tk
from tkinter import messagebox

class GameGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Game Generator')

        self.label = tk.Label(self.root, text='Enter game details:')
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.generate_button = tk.Button(self.root, text='Generate Game', command=self.generate_game)
        self.generate_button.pack()

        self.quit_button = tk.Button(self.root, text='Quit', command=self.root.quit)
        self.quit_button.pack()

    def generate_game(self):
        game_details = self.entry.get()
        if not game_details:
            messagebox.showwarning('Input Error', 'Please enter valid game details.')
            return
        # Sample game generation logic
        print(f'Generating game with details: {game_details}')
        messagebox.showinfo('Game Generated', f'Game with details "{game_details}" has been created!')

    def run(self):
        self.root.mainloop()

def cli_interface():
    if len(sys.argv) < 2:
        print('Usage: python app.py <game details>')
        sys.exit(1)
    game_details = sys.argv[1]
    print(f'Generating game with details: {game_details}')
    # Implement actual game generation logic here
    print(f'Game with details "{game_details}" has been created!')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        cli_interface()
    else:
        app = GameGenerator()
        app.run()