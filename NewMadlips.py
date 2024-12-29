from tkinter import Tk, Toplevel, Label, Button, Entry
tl = Toplevel

def story1(win):
    print("Story 1 triggered")
    print("Creating NewScreen")



NewScreen = Tk()
NewScreen.title("My New MadLips")
NewScreen.geometry('400x400')
NewScreen.config(bg="blue")
Label(NewScreen, text='To the store') .place(x=100, y=20)
story1Button = Button(NewScreen, text='To the store', font=("Time New Roman", 14),command=lambda: story1(NewScreen),bg='green')
story1Button.place(x=140, y=90)
story2Button = Button(NewScreen, text='Job', font=("Time New Roman", 14),command=lambda: story1(NewScreen),bg='green')
story2Button.place(x=150, y=150)

NewScreen.update()
NewScreen.mainloop()

def story1(win):
    def final(tl: Toplevel, name, place, snack, drink):
        text = f'''
            One day a man {name} decided to go to {place} to get food but all he would was {snack} and {drink} '''
        tl.geometry(newGeometry='500x500')
    
        Label(tl, text='story:', wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text = text,wraplength=tl.winfo_width()).place(x=0, y=330)
    
    NewScreen = Toplevel(win, bg='yellow') 
    NewScreen.title("To the store")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='To the store').place(x=100, y=0)
    Label(NewScreen, text='Name:').place(x=0, y=35)
    Label(NewScreen, text='Enter a place:').place(x=0, y=70)
    Label(NewScreen, text='Enter a snack:').place(x=0, y=110)
    Label(NewScreen, text='Enter a drink:').place(x=0, y=150)
    Name = Entry(NewScreen, width=17)
    Name.place(x=250, y=35)
    place = Entry(NewScreen, width=17)
    place.place(x=250, y=70)
    snack = Entry(NewScreen, width=17)
    snack.place(x=250, y=105)
    drink = Entry(NewScreen, width=17)
    drink.place(x=250, y=150)
    SubmitButton = Button(NewScreen, text="Submit", background="Red", font=('Times', 12),command=lambda:final(NewScreen, Name.get(), place.get(), snack.get(), drink.get()))
    SubmitButton.place(x=150, y=270)

    NewScreen.mainloop()

def story2(win):
    def final(tl: Toplevel, date, location, job, time):
        global text
        text = f'''
            On {date} I was told to go to {location} for an interview at a company for a {job} interview I needed to be there at {time} '''

    tl.geometry(newGeometry='500x500')

    Label(tl, text='story:', wraplength=tl.winfo_width()).place(x=160, y=310)
    Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)

    NewScreen = Toplevel(win, bg='yellow')
    NewScreen.title("Job")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='Job').place(x=100, y=0)
    Label(NewScreen, text='date:').place(x=0, y=35)
    Label(NewScreen, text='Enter a location:').place(x=0, y=70)
    Label(NewScreen, text='Enter a job:').place(x=0, y=110)
    Label(NewScreen, text='Enter a time:').place(x=0, y=150)
    date = Entry(NewScreen, width=17)
    date.place(x=250, y=35)
    location = Entry(NewScreen, width=17)
    location.place(x=250, y=70)
    job = Entry(NewScreen, width=17)
    job.place(x=250, y=105)
    time = Entry(NewScreen, width=17)
    time.place(x=250, y=150)
    SubmitButton = Button(NewScreen, text="Submit", background="Red", font=('Times', 12), command=lambda: final(NewScreen, date.get(), location.get(), job.get(), time.get()))
    SubmitButton.place(x=150, y=270)
