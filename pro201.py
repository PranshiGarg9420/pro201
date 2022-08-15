from email import message
from tkinter import *

window= Tk()
window.geometry('400x500')
window.title('INETREST CALCULATOR')
window.configure(bg='pink')

heading= Label(window, text='INTEREST CALCULATOR', fg='pink', bg='blue', font=('Calbri',20) , bd=5)
heading.place(x=50,y=20)

principal_label= Label(window, text='Enter Principal', fg='black',bg='pink', font=('Calbri',10))
entry= Entry(window, text='', bd=2, width=22)
entry.place(x=180, y=90)
principal_label.place(x=50, y=90)

interest_label= Label(window, text='Enter Interest rate', fg='black',bg='pink' , font=('Calbri',10))
interest= Entry(window, text='', bd=2, width=22)
interest_label.place(x=50, y=160)
interest.place(x=180, y=160)

time_label= Label(window, text='Enter time intervel', fg='black',bg='pink' , font=('Calbri',10))
time= Entry(window, text='', bd=2, width=22)
time_label.place(x=50, y=230)
time.place(x=180, y=230)

result_frame= LabelFrame(window, text='RESULT', bg='green',fg='yellow', font=('Calibri',12))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20, y=380)

show_label= Label(result_frame, text='Your Result will be displayed here', bg='green',fg='yellow', font=('Calibri',12), width=65)
show_label.place(x=20,y=20)
show_label.pack()

def calculate_interest():
    p=float(entry.get())
    r=float(interest.get())
    t=float(time.get())
    i=(p*r*t)/100
    final_int= round(i,2)

    message=Label(result_frame, text='Interest on Rs. '+str(p)+' at rate of interest '+str(r)+' for '+str(t)+' years is Rs.'+str(final_int),bg='green',fg='yellow', font=('Calibri',12), width=65)
    message.place(x=20,y=20)
    message.pack()

cal_button= Button(window, text=' Calculate', fg='black', bg='grey',bd=3, command=calculate_interest)
cal_button.place(x=190, y=300)

window.mainloop()