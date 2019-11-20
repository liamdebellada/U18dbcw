from datetime import *
from guizero import *
import sqlite3
with sqlite3.connect('silver_dawn_coaches') as db:
    cursor = db.cursor()

app = App(title="Silver Dawn database management", width=500, height=400)

button_width = 11
current_date = date.today()



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
    
def booking_save(booking_seatnumber, booking_customer, booking_trip):
    
    print('This has passed')
    
    booking_seatnumber = booking_seatnumber.value
    booking_customer = booking_customer.value
    booking_trip = booking_trip.value
    #using current_date for date entry
    
    cursor.execute('''INSERT INTO Booking(customer_id, trip_id, seatNumber, bookingDate) VALUES(?,?,?,?)''', (booking_customer, booking_trip, booking_seatnumber, current_date,))
    db.commit()

def trip_save(trip_cost, trip_startdate, trip_duration, trip_destination, trip_coach, trip_driver):
    trip_cost = trip_cost.value
    trip_startdate = trip_startdate.value
    trip_duration = trip_duration.value
    trip_destination = trip_destination.value
    trip_coach = trip_coach.value
    trip_driver = trip_driver.value
    
    cursor.execute('''INSERT INTO Trip(destination_id, personCost, startDate, duration, coach_id, driver_id) VALUES(?,?,?,?,?,?)''', (trip_destination, trip_cost, trip_startdate, trip_duration, trip_coach, trip_driver,))
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
    
    booking_customer_text = Text(start_booking_window, 'Customer ID:')
    booking_customer = TextBox(start_booking_window, '')
        
    booking_trip_text = Text(start_booking_window, 'Trip ID:')
    booking_trip = TextBox(start_booking_window, '')
    
    save_button = PushButton(start_booking_window, text='Save', width=button_width, command=booking_save, args=[booking_seatnumber, booking_customer, booking_trip])

def trip():
    start_trip_window = Window(app, title='Add trip', width=500, height=400)
    
    trip_cost_text = Text(start_trip_window, 'Enter cost per person:')
    trip_cost = TextBox(start_trip_window, '')
    
    trip_startdate_text = Text(start_trip_window, 'Enter start date:')
    trip_startdate = TextBox(start_trip_window, '')
    
    trip_duration_text = Text(start_trip_window, 'Enter trip duration:')
    trip_duration = TextBox(start_trip_window, '')
    
    trip_destination_text = Text(start_trip_window, 'Enter destination ID:')
    trip_destination = TextBox(start_trip_window, '')
    
    trip_coach_text = Text(start_trip_window, 'Enter coach ID:')
    trip_coach = TextBox(start_trip_window, '')
    
    trip_driver_text = Text(start_trip_window, 'Enter driver ID:')
    trip_driver = TextBox(start_trip_window, '')
    
    trip_save_button = PushButton(start_trip_window, text='Save', width=button_width, command=trip_save, args=[trip_cost, trip_startdate, trip_duration, trip_destination, trip_coach, trip_driver])
    
def destination():
    start_destination_window = Window(app, title='Add destination', width=500, height=400)
    
    destination_name_text = Text(start_destination_window, 'Enter Destination name:')
    destination_name = TextBox(start_destination_window, '')
    
    destination_hotel_text = Text(start_destination_window, 'Enter Hotel name:')
    destination_hotel = TextBox(start_destination_window, '')
    
    destination_save_button = PushButton(start_destination_window, text='Save', command=destination_save, args=[destination_name, destination_hotel])
    
    

main_window_text = Text(app, 'Silver Dawn Coaches booking & management')

picture = Picture(app, image="logo.png")

add_customer_button = PushButton(app, text ='New customer', width=button_width, command=customer)
add_booking_button = PushButton(app, text ='New booking', width=button_width, command=booking)
add_trip_button = PushButton(app, text ='New trip', width=button_width, command=trip)
add_destination_button = PushButton(app, text ='New destination', width=button_width, command=destination)


app.display()
