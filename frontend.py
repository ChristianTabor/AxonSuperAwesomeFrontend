import tkinter as tk
from tkinter import *

import excel
from sql import *
from excel import *
from tkcalendar import Calendar

LARGEFONT = ("Verdana", 35)


def open_popup(self, text: str):
    top = Toplevel(self)
    top.geometry("250x150")
    top.title("Error")
    Label(top, text=text, font='arial 8 bold', justify='center').grid(row=1, column=2)
    Button(top, text='Close', command=lambda: top.destroy(), font='arial 8 bold').grid(row=2, column=2)


def confirm(self):
    top = Toplevel(self)
    top.geometry("250x150")
    top.title("Error")
    Label(top, text="Are you sure you want to reset all badges?", font='arial 8 bold', justify='center').grid(row=1,
                                                                                                              column=2)
    Button(top, text='Reset All Badges', command=lambda: unregisterAndClose(), font='arial 8 bold').grid(row=2,
                                                                                                         column=2)

    def unregisterAndClose():
        unregisterall()
        top.destroy()


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
        for F in (HomePage, NewUser, NewBooth, NewEvent, SetEvent, Export):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.title("Registration Form")
        self.geometry("1000x500")
        self.show_frame(HomePage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = Label(self, text="Home", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = Button(self, text="Register A New User",
                         command=lambda: controller.show_frame(NewUser))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # putting the button in its place by
        # using grid

        button2 = Button(self, text="Add New Event",
                         command=lambda: controller.show_frame(NewEvent))

        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = Button(self, text="Add New Booth",
                         command=lambda: controller.show_frame(NewBooth))

        button3.grid(row=3, column=1, padx=10, pady=10)

        button4 = Button(self, text="Set Event",
                         command=lambda: controller.show_frame(SetEvent))

        button4.grid(row=4, column=1, padx=10, pady=10)

        button5 = Button(self, text="Export To Excel",
                         command=lambda: controller.show_frame(Export))

        button5.grid(row=5, column=1, padx=10, pady=10)

        button6 = Button(self, text="Reset All Badges",
                         command=lambda: confirm(self))

        button6.grid(row=6, column=1, padx=10, pady=10)


# second window frame page1
class NewUser(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Register A New User", font=LARGEFONT)
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
            badgeNum = int(badgeVal.get())
            lastid = insert_attendee(nameVal.get(), emailVal.get(), phoneVal.get(), companyVal.get())
            register_badge(lastid, badgeNum)
            clear()

        Button(self, text='Register', command=getvals, font='arial 8 bold').grid(row=6, column=2)
        Button(self, text='Back', command=lambda: controller.show_frame(HomePage), font='arial 8 bold').grid(row=7,
                                                                                                             column=2)


class NewEvent(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Add A New Event", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        Label(self, text="Name:").grid(row=1, column=1)
        Label(self, text="Location:").grid(row=2, column=1)
        Label(self, text="ZIP Code:").grid(row=3, column=1)

        nameVal = StringVar()
        locationVal = StringVar()
        zipVal = StringVar()

        Entry(self, textvariable=nameVal).grid(row=1, column=2, ipadx=20)
        Entry(self, textvariable=locationVal).grid(row=2, column=2, ipadx=20)
        Entry(self, textvariable=zipVal).grid(row=3, column=2, ipadx=20)

        def clear():
            # clear the content of text entry box
            nameVal.set("")
            locationVal.set("")
            zipVal.set("")

        # Function just get the data from entry box and displaying it to console
        # Then calling clear() to set entry box ''
        def getvals():
            zipNum = int(zipVal.get())
            lastid = insert_event(nameVal.get(), locationVal.get(), zipNum)
            open_popup(self, "Event Added With Id:{}".format(lastid))
            clear()

        Button(self, text='Register', command=getvals, font='arial 8 bold').grid(row=4, column=2)
        Button(self, text='Back', command=lambda: controller.show_frame(HomePage), font='arial 8 bold').grid(row=5,
                                                                                                             column=2)


class NewBooth(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Add A new Booth", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        Label(self, text="Name:").grid(row=1, column=1)

        nameVal = StringVar()

        Entry(self, textvariable=nameVal).grid(row=1, column=2, ipadx=20)

        def clear():
            # clear the content of text entry box
            nameVal.set("")

        # Function just get the data from entry box and displaying it to console
        # Then calling clear() to set entry box ''
        def getvals():
            lastid = insert_booth(nameVal.get())
            string = "Booth Added With Id:%s" % lastid
            open_popup(self, string)
            clear()

        Button(self, text='Add New Booth', command=getvals, font='arial 8 bold').grid(row=2, column=2)
        Button(self, text='Back', command=lambda: controller.show_frame(HomePage), font='arial 8 bold').grid(row=3,
                                                                                                             column=2)


class SetEvent(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Set Event", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        options = getAllEventsMenu()
        if options is None:
            options = ["No Events Current Available"]
        clicked = StringVar()

        # initial menu text
        clicked.set("Select An Option")

        # Create Dropdown menu
        OptionMenu(self, clicked, *options).grid(row=1, column=2)

        # Create button, it will change label text

        Button(self, text="Set Event", command=lambda: setEvent(match())).grid(row=2, column=2)
        Button(self, text="Back", command=lambda: controller.show_frame(HomePage)).grid(row=3, column=2)

        def match() -> int:
            for i in options:
                if str(i) == clicked.get():
                    return i[0]
            return 0


class Export(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Export To Excel", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)

        sqlVars = []
        attendees = IntVar()
        booths = IntVar()
        events = IntVar()
        interactions = IntVar()

        Checkbutton(self, text="Attendees", variable=attendees, onvalue=1, offvalue=0).grid(row=2, column=0)
        Checkbutton(self, text="Booths", variable=booths, onvalue=1, offvalue=0).grid(row=3, column=0)
        Checkbutton(self, text="Events", variable=events, onvalue=1, offvalue=0).grid(row=4, column=0)
        Checkbutton(self, text="Interactions", variable=interactions, onvalue=1, offvalue=0).grid(row=5, column=0)

        calStart = Calendar(self, selectmode='day')

        calStart.grid(row=1, column=0)

        calEnd = Calendar(self, selectmode='day')

        calEnd.grid(row=1, column=1)

        allDates = IntVar()
        Checkbutton(self, text="All Dates", variable=allDates, onvalue=1, offvalue=0).grid(row=2, column=1)

        # Add Button and Label
        Button(self, text="Submit",
               command=lambda: setTimeRange()).grid(row=3, column=1)
        Button(self, text='Back', command=lambda: controller.show_frame(HomePage), font='arial 8 bold').grid(row=4,
                                                                                                             column=1)

        options = ["All Events", "Current Event"]
        x = getAllEventsMenu()
        for i in x:
            options.append(i)

        clicked = StringVar()

        # initial menu text
        clicked.set("Select An Option")

        # Create Dropdown menu
        OptionMenu(self, clicked, *options).grid(row=6, column=0)

        def setTimeRange():
            sqlVars = [calStart.get_date(), calEnd.get_date(), allDates.get(), clicked.get()]
            print(sqlVars)
            filename = "AxonOutPut-" + datetime.datetime.now().strftime("%b-%d-%Y-%H-%M-%S") + ".xlsx"
            wb = Workbook()
            ws = wb.active
            ws['A1'] = 12
            ws.insert_rows(1)
            wb.save(filename)
            if attendees.get():
                excelGetAttendees(sqlVars, filename)
            if booths.get():
                excelGetBooths(sqlVars, filename)
            if events.get():
                excelGetEvents(sqlVars, filename)
            if interactions.get():
                excelGetInteractions(sqlVars, filename)
            wb = load_workbook(filename=filename)
            wb.remove(wb["Sheet"])
            wb.save(filename)


# Driver Code
app = tkinterApp()
app.mainloop()
