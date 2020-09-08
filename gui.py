import tkinter as tk
from tkinter import Label, StringVar, filedialog
import affine, hill
import string

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
    "Affine Cipher",
    "Hill Cipher"
]

result = ""
spaced_result = ""

def fetch(entries):
    # for entry in entries:
    #     field = entry[0]
    #     text  = entry[1].get()
    #     print('%s: "%s"' % (field, text))
    # print(getKey(entries), getText(entries), entries[0][1].get(), entries[3][1].get())

    res = ""

    if (entries[2][1].get() == "Vigenere Cipher"):
        if (entries[1][1].get() == "Encrypt"):
            pass
        elif (entries[1][1].get() == "Decrypt"):
            pass

    elif (entries[2][1].get() == "Affine Cipher"):
        if (entries[1][1].get() == "Encrypt"):
            res = affine.encrypt(getText(entries), int(getKey(entries)[0][0]), int(getKey(entries)[1][0]))
        elif (entries[1][1].get() == "Decrypt"):
            res = affine.decrypt(getText(entries), int(getKey(entries)[0][0]), int(getKey(entries)[1][0]))

    elif (entries[2][1].get() == "Hill Cipher"):
        if (entries[1][1].get() == "Encrypt"):
            res = hill.encrypt(getText(entries), getKey(entries))
        elif (entries[1][1].get() == "Decrypt"):
            res = hill.decrypt(getText(entries), getKey(entries))

    printResult(res)

def printResult(res):
    if (entries[0][1].get() == "Text"):
        result.set(res)
        if (entries[1][1].get() == "Encrypt"):
            spaced_result.set(getSpacedResult(res))
        elif (entries[1][1].get() == "Decrypt"):
            spaced_result.set("")
    else:
        result.set("")
        spaced_result.set("")

def getText(entries):
    if (entries[0][1].get() == "Text"):
        result = entries[3][1].get()
        if (entries[2][1].get() == "Extended Vigenere Cipher"):
            return result
        else:
            result = result.replace(" ", "")
            result = ''.join(i for i in result if not i.isdigit())
            result = result.translate(str.maketrans('', '', string.punctuation))
            return result.lower()
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

def getSpacedResult(ciphertext):
    result = ""
    for i in range(len(ciphertext)):
        if (i % 5 == 0):
            result += " "
        result += ciphertext[i]
    return(result)

if __name__ == '__main__':
    root = tk.Tk()

    entries = []
    ents = makeMenu(root, fields_menu, entries)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    
    ents = makeForm(root, fields_text, ents)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))

    result = StringVar()
    spaced_result = StringVar()

    Label(root, textvariable=result).pack()
    Label(root, textvariable=spaced_result).pack()

    b1 = tk.Button(root, text='Show',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=3, pady=5)
    b2 = tk.Button(root, text='Upload', command=UploadAction)
    b2.pack(side=tk.LEFT, padx=3, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=3, pady=5)

    root.mainloop()