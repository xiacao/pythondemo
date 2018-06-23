from tkinter import *

def processOK():
    print("OK button is clicked")

def processCancel():
    print("Cancel button is clicked")

def main():
    tk = Tk()
    btnOK = Button(tk, text = "OK", bg = "red",
                   command = processOK)
    btnCancel = Button(tk, text="Cancel", bg = "yellow",
                       command = processCancel)
    btnOK.pack()
    btnCancel.pack()

    tk.mainloop()


if __name__ == "__main__":
    main()
