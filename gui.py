import tkinter as tk
import affine

def show_entry_fields():
    print("Encrypt: %s\nDecript: %s" % (affine.encrypt(e1.get(), 3, 1), affine.decrypt(e2.get(), 3, 1)))

master = tk.Tk()
tk.Label(master, 
         text="Encrypt").grid(row=0)
tk.Label(master, 
         text="Decript").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()
