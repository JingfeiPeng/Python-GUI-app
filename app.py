import tkinter as tk  #help to creat gui
from tkinter import filedialog, Text
import os


def addApp():
    for widget in frame.winfo_children():  # gives us access to everything attached to this frame
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    if filename != "":
        apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


apps = []
root = tk.Tk()


if os.path.isfile('save.txt'):
    with open("save.txt", "r") as f:
        tempApps = f.read()
        apps = tempApps.split(',')
        print(apps)
        apps = [ x for x in apps if x.strip()]


canvas = tk.Canvas(root, height=600, width=700, bg="#263D42")  # attach to root
canvas.pack()  # to make canvas effective

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5,
                     fg="white", bg="#263D42", command=addApp)  # fg =  foreground = text color
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5,
                    fg="white", bg="#263D42", command=runApps)  # fg =  foreground = text color
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app, bg="grey")
    label.pack()

root.mainloop()

# executed when app closes
with open('save.txt', "w") as f:
    for app in apps:
        f.write(app + ',')