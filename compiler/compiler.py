import parser.parser as parser
import tokenizer.tokenizer as tokenizer

import tkinter
from tkinter import filedialog

if __name__ == "__main__":
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Orthophosphate Files", "*.txt *.opo4")])

    SEPARATOR = "\n### ### ###\n"
    LESSER_SEPERATOR = "\n--- --- ---\n"

    with open(file_path, 'r') as file:
        src = file.read()

        tokens = tokenizer.tokenize(src)
        ast = parser.parse(tokens)

        print(SEPARATOR)
        print(src)
        print(SEPARATOR)
        print(tokens)
        print(SEPARATOR)
        print(repr(ast))
        print(LESSER_SEPERATOR)
        print(ast)
        print(SEPARATOR)