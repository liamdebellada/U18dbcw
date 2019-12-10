from datetime import *
from guizero import *
import sqlite3
with sqlite3.connect('silver_dawn_coaches') as db:
    cursor = db.cursor()
    cursor.execute("PRAGMA foreign_keys = 1")

app = App(title="Silver Dawn database management", width=500, height=400)

button_width = 11
current_date = date.today()

booking_seatnumber = 0

def plusbutton(booking_seatnumber_value):
    global booking_seatnumber
    booking_seatnumber = booking_seatnumber + 1
    booking_seatnumber_value.value = booking_seatnumber
    
def minusbutton(booking_seatnumber_value):
    global booking_seatnumber
    booking_seatnumber = booking_seatnumber - 1
    booking_seatnumber_value.value = booking_seatnumber
    

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
    
def booking_save(booking_seatnumber_value, booking_customer, booking_trip):
    print('This has passed')
    booking_customer = booking_customer.value
    booking_trip = booking_trip.value
    #using current_date for date entry
    
    cursor.execute('''INSERT INTO Booking(customer_id, trip_id, seatNumber, bookingDate) VALUES(?,?,?,?)''', (booking_customer, booking_trip, booking_seatnumber, current_date,))
    db.commit()
    
def destination_save(destination_name, destination_hotel):
    print('woked')
    destination_name = destination_name.value
    destination_hotel = destination_hotel.value
    
    cursor.execute('''INSERT INTO Destination(destName, hotelName) VALUES(?,?)''', (destination_name, destination_hotel,))
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
    
    booking_seatnumber_text = Text(start_booking_window, 'Number of seats:')
    booking_seatnumber_value = Text(start_booking_window, '0')
    booking_plus = PushButton(start_booking_window, text="+", width=1, height=1, command=plusbutton, args=[booking_seatnumber_value])
    booking_minus = PushButton(start_booking_window, text='-', width=1, height=1, command=minusbutton, args=[booking_seatnumber_value])
    
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
    
def query():
    start_query_window = Window(app, title='Search', width=500, height=400)
    trips = []
    for row in cursor.execute("SELECT destName, trip_id FROM Trip INNER JOIN Destination on Destination.destination_id = Trip.destination_id ORDER BY startDate"):
        trips.append(row)
        #print(str(row))
    query_title = Text(start_query_window, 'Search the database')
    
    query_christmas_text = Text(start_query_window, 'Search Christmas trip:')
    query_christmas = PushButton(start_query_window, text='Search', width=button_width, command=christmas_trip)
    
    query_all_trip_text = Text(start_query_window, 'Search all trips:')
    query_all_trip = PushButton(start_query_window, text='Search', width=button_width, command=all_trip)
    
    query_e5_postcode_text = Text(start_query_window, 'Search all e5 postcodes:')
    query_e5_postcode = PushButton(start_query_window, text='Search', width=button_width, command=e5_postcode)
    
    query_trips_text = Text(start_query_window, 'Calculate income for all trips:')
    query_trips = Combo(start_query_window, options=trips, width=14)
    query_trips_calculated = Text(start_query_window, '')
    query_trips_button = PushButton(start_query_window, text='Calculate', command=Calculate, args=[query_trips])

def christmas_trip():
    report = open("report1.txt","w+")
    
    report.write('ID   Firstname   Surname   Address_1        Address_2    Phone_number   Email Address           Notes'+'\n'+'\n')
    
    cursor.execute("SELECT Trip_id from Trip INNER JOIN Destination ON Destination.destination_id = Trip.destination_id where destName = 'Lincoln Xmas Market'")
    trip_id = cursor.fetchall()
    trip_id = [tripI[0] for tripI in trip_id]
    trip_id = int(trip_id[0])
    
    #print(trip_id)
    cursor.execute("SELECT customer_id FROM Booking where trip_id=?", (trip_id,))
    customer_id = cursor.fetchall()
    customer_id = [customerI[0] for customerI in customer_id]
    #customer_id = int(customer_id[0])
    #print(customer_id)
    
    for i in customer_id:
        cursor.execute('SELECT * FROM Customer where customer_id=?', (i,))
        print(cursor.fetchall())
    
        for row in cursor.execute('SELECT * FROM Customer where customer_id=?', (i,)):
            #print(row)
            report.write(str(row))
            report.write("\n")
        
def all_trip():
    report = open('All_trips.txt', 'w+')
    report.write("Destination:    Startdate:    cost:    Duration: \n")
    for row in cursor.execute("SELECT destName, startDate, personCost, duration FROM Trip INNER JOIN Destination on Destination.destination_id = Trip.destination_id ORDER BY startDate"):
        
        #all_trip = cursor.fetchall()
        report.write(str(row))
        report.write('\n')

def e5_postcode():
    report = open('E5_leaflet.txt', 'w+')
    report.write('Address1: Address2: Postcode:\n')
    for row in cursor.execute("SELECT AddressLine1, AddressLine2, Postcode FROM customer WHERE Postcode LIKE 'E5%'"):
        report.write(str(row))
        report.write('\n')

def Calculate(query_trips):
    report = open('Trip_income.txt', 'w+')
    
    d = query_trips.value
    print(d)
    
    d = str(d)
    report.write('Trip Destination  Trip ID  PersonCost SumPersonCost \n')
    report.write(d)
    
    numbers = []
    
    customer_id = [customerI[0] for customerI in d]
    #print(customer_id)
    for i in customer_id:
        #print(i)
        if i.isdigit():
            numbers.append(i)
        
  
    #print(numbers)
    num = ("".join(numbers))
    num = int(num)
    print(num)
    
    cursor.execute('SELECT SUM(seatNumber) FROM Booking where trip_id=?', (num,))
    
    sums = cursor.fetchall()
    sums = [tripI[0] for tripI in sums]
    sums = int(sums[0])
    print(sums)
    
    for row in cursor.execute("SELECT trip_id, personCost, (personCost)*? FROM Trip INNER JOIN Destination on Destination.destination_id = Trip.destination_id WHERE trip_id = ?", (sums, num,)):
        row = str(row)
        report.write(row)

    
    
main_window_text = Text(app, 'Silver Dawn Coaches booking & management')

picture = Picture(app, image="logo.png")

add_customer_button = PushButton(app, text ='New customer', width=button_width, command=customer)
add_booking_button = PushButton(app, text ='New booking', width=button_width, command=booking)
add_trip_button = PushButton(app, text ='New trip', width=button_width, command=trip)
add_destination_button = PushButton(app, text ='New destination', width=button_width, command=destination)
search_button = PushButton(app, text = 'Search Data', width=button_width, command=query)


app.display()
