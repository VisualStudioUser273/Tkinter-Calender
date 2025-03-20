from tkinter import*
import calendar

window=Tk()
window.geometry("250x140")
window.title('Calender')
window.config(background='Orange')


def showCal():
    fetchher=int(entry_i.get())
    calcontent=calendar.calendar(fetchher)
    outputwindow=Tk()
    outputwindow.geometry('550x600')
    outputlabel=Label(outputwindow,text=calcontent,font='Consolas 10 bold')
    outputlabel.grid(row=5,column=1,padx=20)
    outputwindow.mainloop()

    

title_l=Label(window,text='Calender',font='Times 28 bold')
year_l=Label(window,text='Year')
entry_i=Entry(window)
show_b=Button(window,text='Show Calender',command=showCal)
show_e=Button(window,text='Exit',command=exit)


title_l.grid(row=0,column=0)
year_l.grid(row=1,column=0)
entry_i.grid(row=2,column=0)
show_b.grid(row=3,column=0)
show_e.grid(row=4,column=0)
window.mainloop()
