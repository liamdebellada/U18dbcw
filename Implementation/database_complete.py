from guizero import *
import sqlite3
with sqlite3.connect('silver_dawn_coaches') as db:
    cursor = db.cursor()

app = App(title="Silver Dawn database management", width=500, height=400)

button_width = 11

def save(first_customer_name, second_customer_name, customer_address_1, customer_address_2, customer_email_address, customer_phone_number, customer_notes):
    print('This has been saved')
    first_customer_name = first_customer_name.value
    second_customer_name = second_customer_name.value
    customer_address_1 = customer_address_1.value
    customer_address_2 = customer_address_2.value
    customer_email_address = customer_email_address.value
    customer_phone_number = customer_phone_number.value
    customer_notes = customer_notes.value
    
    if customer_notes == '':
        customer_notes = 'None'
    
    cursor.execute('''INSERT INTO Customer(firstName, surname, AddressLine1, AddressLine2, phoneNum, email, specialNeed) VALUES(?,?,?,?,?,?,?)''', (first_customer_name, second_customer_name, customer_address_1, customer_address_2, customer_phone_number, customer_email_address, customer_notes,))
    db.commit()


def customer():
    start_customer_window = Window(app, title='Add customer', width=500, height=400)
    customer_window_text = Text(start_customer_window, 'New customer')
    
    
    customer_name_text = Text(start_customer_window, 'Enter name:')
    first_customer_name = TextBox(start_customer_window, text='', align='top')
    
    second_customer_name = TextBox(start_customer_window, text='', align='top')
    
    customer_address_text = Text(start_customer_window, 'Enter address:')
    customer_address_1 = TextBox(start_customer_window, text='')
    customer_address_2 = TextBox(start_customer_window, text='')
    
    customer_phone_number_text = Text(start_customer_window, 'Enter phone number:')
    customer_phone_number = TextBox(start_customer_window, text='')
    
    customer_email_address_text = Text(start_customer_window, 'Enter email address:')
    customer_email_address = TextBox(start_customer_window, text='')
    
    customer_notes_text = Text(start_customer_window, 'Additional info')
    customer_notes = TextBox(start_customer_window, '')
    
    
    save_button = PushButton(start_customer_window, text ='Save', width=button_width, command=save, args=[first_customer_name, second_customer_name, customer_address_1, customer_address_2, customer_email_address, customer_phone_number, customer_notes])
    
def booking():
    start_booking_window = Window(app, title='Add booking', width=500, height=400)
    
    booking_title = Text(start_booking_window, 'New booking')
    
    booking_seatnumber_text = Text(start_booking_window, 'Seat Number:')
    booking_seatnumber = TextBox(start_booking_window, '')
    
    booking_seatnumber_text = Text(start_booking_window, 'Booking Date:')
    booking_date = TextBox(start_booking_window, '')
    
    cursor.execute("SELECT firstName, surName, customer_id FROM customer")
    name_list = []
    names = cursor.fetchall()
    for i in names:
        name_list.append(i)
        
    
    booking_customer_text = Text(start_booking_window, 'Select customer')
    booking_customer = Combo(start_booking_window, options=name_list)
    

def trip():
    start_trip_window = Window(app, title='Add trip', width=500, height=400)
    
def destination():
    start_destination_window = Window(app, title='Add destination', width=500, height=400)
    
    

main_window_text = Text(app, 'Silver Dawn Coaches booking & management')

picture = Picture(app, image="logo.png")

add_customer_button = PushButton(app, text ='New customer', width=button_width, command=customer)
add_booking_button = PushButton(app, text ='New booking', width=button_width, command=booking)
add_trip_button = PushButton(app, text ='New trip', width=button_width, command=trip)
add_destination_button = PushButton(app, text ='New destination', width=button_width, command=destination)


app.display()
