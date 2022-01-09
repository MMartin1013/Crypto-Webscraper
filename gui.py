from tkinter import *
from webscraper import WebScraper

#Defines webscraper
scraper = WebScraper()

current = None

#Initializes and defines dimensions for root window
root = Tk()
root.title('Crypto Stats from coinmarketcap.com')
root.geometry('700x750')
root.minsize(700,750)

#Initializes frame to hold data
frame = LabelFrame(root, text="Info", bg='white', fg ='black', padx=25,pady=25)
frame.place(relx=0.5, rely=0.4, anchor=CENTER)
Label(frame, text='1. Click trending for Trending cryptocurrencies\n\n2. Click Top 5 for the Top5 cryptocurrencies\n\n3. The values dynamically update', bg='white', fg='black', font='Helvetica 12').pack(padx=150, pady=150)

#Displays directions
def directions():
    clear()
    Label(frame, text='1. Click trending for Trending cryptocurrencies\n\n2. Click Top 5 for the Top5 cryptocurrencies\n\n3. The values dynamically update', bg='white', fg='black', font='Helvetica 12').pack(padx=150, pady=150)

#Clears the frame
def clear():
    global current
    widgets = frame.pack_slaves()
    for widget in widgets:
        widget.destroy()
    current = clear if current != directions else current



#Displays trending data
def trending():
    clear()
    global current
    current = trending
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
    global current
    current = topfive
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

#Updates results every 5 seconds
def update():
    current()
    root.after(5000,update)
    
current = directions if current == None else current


#Title and buttons
title = Label(root, text="Crypto Info Gatherer").pack(anchor=CENTER)
exit_button = Button(root, text='Exit', command=root.quit).place(relx=0.25, rely=0.8, anchor=CENTER)
trending_button = Button(root, text='Trending', command=lambda: trending()).place(relx=0.5, rely=0.8, anchor=CENTER)
top5_button = Button(root, text='Top 5', command=lambda: topfive()).place(relx=0.75, rely=0.8, anchor=CENTER)
clear_button = Button(root, text='Clear', command=lambda: clear()).place(relx=0.5, rely=0.90, anchor=CENTER)

#Starts loop
root.after(5000, update)
root.mainloop()