from tkinter import*
import calendar

window=Tk()
window.geometry("300x300")
window.title('Calender')
window.config(background='Orange')

title_l=Label(window,text='Calender',font='calibri 25')
year_l=Label(window,text='Year',font='calibri 18')
entry_i=Entry(window)
show_b=Button(window,text='Show Calender')
show_e=Button(window,text='Exit')


title_l.grid(row=0,column=0)
year_l.grid(row=1,column=0)
entry_i.grid(row=2,column=0)
show_b.grid(row=3,column=0)
show_e.grid(row=4,column=0)
window.mainloop()