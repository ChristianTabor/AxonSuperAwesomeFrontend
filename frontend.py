import tkinter as tk
from tkinter import *
from sql import *

LARGEFONT = ("Verdana", 35)


def open_popup(self, text: str):
    top = Toplevel(self)
    top.geometry("250x150")
    top.title("Error")
    Label(top, text=text, font=('arial 8 bold'), justify='center').place(x=125, y=75)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, NewUser, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.title("Registration Form")
        self.geometry("500x300")
        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = Label(self, text="Startpage", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = Button(self, text="Page 1",
                         command=lambda: controller.show_frame(NewUser))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = Button(self, text="Page 2",
                         command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = Button(self, text="Error Test",
                         command=lambda: open_popup(self, "Herro"))

        button3.grid(row=3, column=1, padx=10, pady=10)


# second window frame page1
class NewUser(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        Label(self, text="Name:").grid(row=1, column=1)
        Label(self, text="Email Address:").grid(row=2, column=1)
        Label(self, text="Phone Number:").grid(row=3, column=1)
        Label(self, text="Company:").grid(row=4, column=1)
        Label(self, text="Badge Number:").grid(row=5, column=1)

        nameVal = StringVar()
        emailVal = StringVar()
        phoneVal = StringVar()
        companyVal = StringVar()
        badgeVal = StringVar()

        Entry(self, textvariable=nameVal).grid(row=1, column=2, ipadx=20)
        Entry(self, textvariable=emailVal).grid(row=2, column=2, ipadx=20)
        Entry(self, textvariable=phoneVal).grid(row=3, column=2, ipadx=20)
        Entry(self, textvariable=companyVal).grid(row=4, column=2, ipadx=20)
        Entry(self, textvariable=badgeVal).grid(row=5, column=2, ipadx=20)

        def clear():
            # clear the content of text entry box
            nameVal.set("")
            emailVal.set("")
            phoneVal.set("")
            companyVal.set("")
            badgeVal.set("")

        # Function just get the data from entry box and displaying it to console
        # Then calling clear() to set entry box ''
        def getvals():
            print(nameVal.get())
            print(emailVal.get())
            print(phoneVal.get())
            print(companyVal.get())
            badgeNum = int(badgeVal.get())
            print(badgeNum)
            lastid = insert_attendee(nameVal.get(), emailVal.get(), phoneVal.get(), companyVal.get())
            print(lastid)
            register(lastid, badgeNum)
            clear()

        Button(self, text='Register', command=getvals, font='arial 8 bold').grid(row=6, column=2)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = Button(self, text="Page 1",
                         command=lambda: controller.show_frame(NewUser))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = Button(self, text="Startpage",
                         command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()
