import tkinter as tk
from tkinter import filedialog
import affine, hill, vigenere

fields_text = 'Text', 'Key'
fields_menu = 'Input Type', 'Action', 'Algorithm'

input_types = [
    "Text",
    "File"
] 

actions = [
    "Encrypt",
    "Decrypt"
]

algorithms = [
    "Vigenere Cipher",
    "Full Vigenere Cipher",
    "Auto Vigenere Cipher",
    "Extended Vigenere Cipher",
    "Playfair Cipher",
    "Super Enkripsi",
    "Affine Chiper",
    "Hill Chiper"
]

def fetch(entries):
    # for entry in entries:
    #     field = entry[0]
    #     text  = entry[1].get()
    #     print('%s: "%s"' % (field, text))
    # print(getKey(entries), getText(entries), entries[0][1].get(), entries[3][1].get())

    if (entries[2][1].get() == "Vigenere Cipher"):
        if (entries[1][1].get() == "Encrypt"):
            print(vigenere.encryptStandard(getText(entries), getKey(entries)[0][0]))
        elif (entries[1][1].get() == "Decrypt"):
            print(vigenere.decryptStandard(getText(entries), getKey(entries)[0][0]))
    elif (entries[2][1].get() == "Auto Vigenere Cipher"):
        if (entries[1][1].get() == "Encrypt"):
            print(vigenere.encryptAutoKey(getText(entries), getKey(entries)[0][0]))
        elif (entries[1][1].get() == "Decrypt"):
            print(vigenere.decryptAutoKey(getText(entries), getKey(entries)[0][0]))
    elif (entries[2][1].get() == "Extended Vigenere Cipher"):
        if (entries[1][1].get() == "Encrypt"):
            print(vigenere.encryptExtended(getText(entries), getKey(entries)[0][0]))
        elif (entries[1][1].get() == "Decrypt"):
            print(vigenere.decryptExtended(getText(entries), getKey(entries)[0][0]))
    elif (entries[2][1].get() == "Affine Cipher"):
        if (entries[1][1].get() == "Encrypt"):
            print(affine.encrypt(getText(entries), int(getKey(entries)[0][0]), int(getKey(entries)[1][0])))
        elif (entries[1][1].get() == "Decrypt"):
            print(affine.decrypt(getText(entries), int(getKey(entries)[0][0]), int(getKey(entries)[1][0])))
    elif (entries[2][1].get() == "Hill Cipher"):
        if (entries[1][1].get() == "Encrypt"):
            print(hill.encrypt(getText(entries), getKey(entries)))
        elif (entries[1][1].get() == "Decrypt"):
            print(hill.decrypt(getText(entries), getKey(entries)))

def getText(entries):
    if (entries[0][1].get() == "Text"):
        return entries[3][1].get()
    elif (entries[0][1].get() == "File"):
        pass # baca dari file

def getKey(entries):
    result = []
    for elmt in entries[4][1].get().split(' ') :
        result.append(elmt.split(','))
    return result

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def chooseMenu(menu_label):
    if (menu_label == "Input Type"):
        return input_types
    elif (menu_label == "Action"):
        return actions
    else:
        return algorithms

def makeMenu(root, fields, entries):
    for field in fields:
        variable = tk.StringVar(root)
        variable.set(field)
        opt = tk.OptionMenu(root, variable, *chooseMenu(field))
        opt.config(width=60)
        opt.pack()
        entries.append((field, variable))
    return entries

def makeForm(root, fields, entries):
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row, width=45)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    entries = []
    ents = makeMenu(root, fields_menu, entries)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    ents = makeForm(root, fields_text, ents)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = tk.Button(root, text='Show',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=3, pady=5)
    b2 = tk.Button(root, text='Upload', command=UploadAction)
    b2.pack(side=tk.LEFT, padx=3, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=3, pady=5)
    root.mainloop()