import tkinter as tk
from tkinter import N, filedialog
from tkinter import Tk, Text, Frame, Button


class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title('Sourish\'s Notepad')

        self.text_area: Text = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack(ipady=10)

        self.new_button: Button = Button(self.button_frame, text='New', command=self.new_file)
        self.new_button.pack(side=tk.LEFT,padx=5)

        self.save_button: Button = Button(self.button_frame, text='Save', command=self.save_file)
        self.save_button.pack(side=tk.LEFT,padx=5)

        self.load_button: Button = Button(self.button_frame, text='Load', command=self.load_file)
        self.load_button.pack(side=tk.LEFT,padx=5)

        self.file_path = None

    def save_file(self) -> None:
        if self.file_path: 
            with open(self.file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            print(f'File saved to: {self.file_path}')
        else:
            self.file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                                          filetypes=[('Text files', '*.txt')])
            with open(self.file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            print(f'File saved to: {self.file_path}')

    def load_file(self) -> None:
        file_path: str = filedialog.askopenfilename(defaultextension='.txt',
                                                     filetypes=[('Text files', '*.txt')])
        with open(file_path, 'r') as file:
            content: str = file.read()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.INSERT, content)
        self.file_path = file_path
        print(f'File loaded from: {self.file_path}')

    def new_file(self) -> None:
        file_path: str = filedialog.asksaveasfilename(defaultextension='.txt',
                                                     filetypes=[('Text files', '*.txt')])
        with open(file_path, 'w') as file:
            file.write('')
        self.text_area.delete(1.0, tk.END)
        self.file_path = file_path
        print(f'File created at: {self.file_path}')

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()


if __name__ == '__main__':
    main()