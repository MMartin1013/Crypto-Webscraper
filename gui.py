from tkinter import *
from webscraper import WebScraper

#Defines webscraper
scraper = WebScraper()

#Initializes and defines dimensions for root window
root = Tk()
root.title('Crypto Stats')
root.geometry('700x750')
root.minsize(700,750)

#Initializes frame to hold data
frame = LabelFrame(root, text="Info", bg='white', fg ='black', padx=25,pady=25)
frame.place(relx=0.5, rely=0.4, anchor=CENTER)
placeholder = Label(frame, text='', bg='white').pack(padx=200, pady=200)


#Clears the frame
def clear():
    widgets = frame.pack_slaves()
    for widget in widgets:
        widget.destroy()

#Displays trending data
def trending():
    clear()
    trendinginfo = scraper.get_categories()
    for category in trendinginfo:
        Label(frame, text=category.name + ':', bg='white', fg='black', font='Helvetica 24 bold').pack(anchor='w')
        for company in category.companies:
            formatframe = LabelFrame(frame, text='', bg='white', fg ='black', borderwidth=0, highlightthickness=0)
            formatframe.pack()
            Label(formatframe,text=company.rank, bg='white', fg='black',font='Helvetica 16 bold').pack(side='left')
            Label(formatframe,text=company.name, bg='white', fg='black',font='Helvetica 16').pack(side='left')
            if company.pricechange[0] == '-':
                color = 'red' 
            elif company.pricechange[0] == '+':
                color = 'green'
            else:
                color = 'black'
            Label(formatframe,text=company.pricechange, bg='white', fg=color,font='Helvetica 16').pack(side='right')


    
#Displays top5 companies
def topfive():
    clear()
    top5 = scraper.get_table()
    for company in top5:
        Label(frame,text=company.rank + ' ' + company.name + ':', bg='white', fg='black',font='Helvetica 12 bold').pack(anchor='w')
        formatframe = LabelFrame(frame, text='', bg='white', fg ='black', borderwidth=0, highlightthickness=0)
        formatframe.pack()
        Label(formatframe,text=company.get_pricechange(), bg='white', fg='black', font='Helvetica 12').pack(side='left')
        color = 'red' if company.dayprice[0] == '-' else 'green'
        Label(formatframe,text=company.get_dayprice(), bg='white', fg=color, font='Helvetica 12').pack(side='left')
        color = 'red' if company.sevendayprice[0] == '-' else 'green'
        Label(formatframe,text=company.get_sevendayprice(), bg='white', fg=color,font='Helvetica 12').pack(side='left')
        Label(formatframe,text=company.get_marketcap(), bg='white', fg='black',font='Helvetica 12').pack(side='left')
        Label(formatframe,text=company.get_volume(), bg='white', fg='black',font='Helvetica 12').pack(side='left')
        Label(frame,text=company.get_circulatingsupply(), bg='white', fg='black',font='Helvetica 12').pack()
    
    


#Title and buttons
title = Label(root, text="Crypto Info Gatherer").pack(anchor=CENTER)
exit_button = Button(root, text='Exit', command=root.quit).place(relx=0.25, rely=0.8, anchor=CENTER)
trending_button = Button(root, text='Trending', command=lambda: trending()).place(relx=0.5, rely=0.8, anchor=CENTER)
top5_button = Button(root, text='Top 5', command=lambda: topfive()).place(relx=0.75, rely=0.8, anchor=CENTER)
clear_button = Button(root, text='Clear', command=lambda: clear()).place(relx=0.5, rely=0.90, anchor=CENTER)

root.mainloop()