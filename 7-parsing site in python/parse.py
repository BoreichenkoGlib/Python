import tkinter
import requests
from tkinter import *


def refresh(new_choices):
    default_value_currencies.set('')
    select_menu_currencies['menu'].delete(0, 'end')
    count = 0

    for choice in new_choices:
        if count == 0:
            default_value_currencies.set(choice)
            count += 1
        select_menu_currencies['menu'].add_command(label=choice,
                                                   command=tkinter._setit(default_value_currencies, choice))


def confirm():
    output = Text(font='Arial 10')
    output.place(relx=.1, y=170, height=150, width=400)

    for organizations in data:
        if organizations == 'organizations':
            for keys in data[organizations]:
                if keys['title'] == default_value_bank_titles.get():
                    for currency in keys['currencies']:
                        if currency == default_value_currencies.get():
                            output.insert(END, 'Покупка - ' + str(keys['currencies'][currency]['bid']) + '\n')
                            output.insert(END, 'Продажа - ' + str(keys['currencies'][currency]['ask']) + '\n')
                            output.insert(END, 'Адреса - ' + str(keys['address']) + '\n')
                            output.insert(END, 'Адреса сайта - ' + str(keys['link']) + '\n')
                            output.insert(END, 'Дата - ' + str(data['date']))


def callback(*args):
    for organizations in data:
        if organizations == 'organizations':
            for id_organisation in data[organizations]:
                if id_organisation['title'] == default_value_bank_titles.get():
                    refresh(id_organisation['currencies'])


url = 'http://resources.finance.ua/ua/public/currency-cash.json'

response = requests.get(url=url)
data = response.json()
bank_titles = []

for organizations in data:
    if organizations == 'organizations':
        for id_organisation in data[organizations]:
            bank_titles.append(id_organisation['title'])

main = Tk(className='boreichenko ki4')
main.geometry('500x350+700+300')
main.resizable(False, False)

default_value_currencies = StringVar(main)
default_value_currencies.set('')

select_menu_currencies = OptionMenu(main, default_value_currencies, '')
select_menu_currencies.place(relx=.4, y=10)

default_value_bank_titles = StringVar(main)
default_value_bank_titles.trace("w", callback)
default_value_bank_titles.set(bank_titles[0])

select_menu_back_titles = OptionMenu(main, default_value_bank_titles, *bank_titles)
select_menu_back_titles.place(relx=.4, y=60)

button = Button(main, text="Підтвердити", command=confirm)
button.place(relx=.4, y=110, height=30, width=76)

label_currency = Label(main, text="Виберіть валюту:")
label_currency.place(relx=.1, y=10)

label_bank_titles = Label(main, text="Виберіть банк:")
label_bank_titles.place(relx=.1, y=60)

mainloop()
