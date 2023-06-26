import mysql.connector
import os

# w3schools.com for instruction on how to use Python/MySQL connector module and help with
# Python and SQL commands. 

db = mysql.connector.connect(host = "localhost", database = "travelplanner", username = "root", password ="root")
cursor = db.cursor()
cursor = db.cursor(buffered=True)

# DESTINATION METHODS
def getDestinationMaxKey():
    cursor.execute("SELECT MAX(destination_id) FROM destination")
    result = cursor.fetchall()
    for x in result:
        if x[0] == None:
            return 1
        return x[0]
def get_destination_id(count):
    list = (count, )
    cursor.execute("SELECT destination_id FROM destination WHERE destination_id=%s", list)
    result = cursor.fetchall()
    for char in result:
        for x in char:
            if x != '\'':
                print('Destination Key: ', x)
def get_destination_location(count):
    list = (count, )
    cursor.execute("SELECT location FROM destination WHERE destination_id=%s", list)
    result = cursor.fetchall()
    for char in result:
        for x in char:
            if x != '\'':
                print('Location: ', x)
def get_destination_cost_per_night(count):
    list = (count, )
    cursor.execute("SELECT cost_per_night FROM destination WHERE destination_id=%s", list)
    result = cursor.fetchall()
    for char in result:
        for x in char:
            if x != '\'':
                print('Cost Per Night: ', x)
def get_destination_nights(count):
    list = (count, )
    cursor.execute("SELECT nights FROM destination WHERE destination_id=%s", list)
    result = cursor.fetchall()
    for char in result:
        for x in char:
            if x != '\'':
                print('Number of Nights: ', x)

# TRANSPORTATION METHODS
def getTransportationMaxKey():
    cursor.execute("SELECT MAX(transportation_id) FROM transportation")
    result = cursor.fetchall()
    for x in result:
        if x[0] == None:
            return 1
        return x[0]
def get_transportation_key(count):
    list = (count, )
    cursor.execute("SELECT transportation_id FROM transportation WHERE transportation_id=%s", list)
    result = cursor.fetchall()
    for char in result:
        for x in char:
            if x != '\'':
                print('Transportation Key: ', x)
def get_transportation_method(count):
    list = (count, )
    cursor.execute("SELECT method FROM transportation WHERE transportation_id=%s", list)
    result = cursor.fetchall()
    for char in result:
        for x in char:
            if x != '\'':
                print('Method: ', x)
def get_transportation_cost(count):
    list = (count, )
    cursor.execute("SELECT cost FROM transportation WHERE transportation_id=%s", list)
    result = cursor.fetchall()
    for char in result:
        for x in char:
            if x != '\'':
                print('Cost: ', x)

# ITINERARY METHODS
def getItineraryMaxKey():
    cursor.execute("SELECT MAX(itinerary_id) FROM itinerary")
    result = cursor.fetchall()
    for x in result:
        if x[0] == None:
            return 1
        return x[0]
def get_itinerary_key(count):
    list = (count, )
    cursor.execute("SELECT itinerary_id FROM itinerary WHERE itinerary_id=%s", list)
    result = cursor.fetchall()
    for char in result:
        for x in char:
            if x != '\'':
                print('Itinerary Key: ', x)
def get_itinerary_excursion(count):
    list = (count, )
    cursor.execute("SELECT excursion FROM itinerary WHERE itinerary_id=%s", list)
    result = cursor.fetchall()
    for char in result:
        for x in char:
            if x != '\'':
                print('Excursion: ', x)
def get_itinerary_datetime(count):
    list = (count, )
    cursor.execute("SELECT date_time FROM itinerary WHERE itinerary_id=%s", list)
    result = cursor.fetchall()
    for char in result:
        for x in char:
            if x != '\'':
                print('Date: ', x)
def get_itinerary_cost(count):
    list = (count, )
    cursor.execute("SELECT cost FROM itinerary WHERE itinerary_id=%s", list)
    result = cursor.fetchall()
    for char in result:
        for x in char:
            if x != '\'':
                print('Cost: ', x)

# VIEW METHODS
def view_destination(count):
    get_destination_location(count)
    get_destination_cost_per_night(count)
    get_destination_nights(count)

def view_transportation(count): 
    get_transportation_method(count)
    get_transportation_cost(count)

def view_itinerary(count):
    get_itinerary_excursion(count)
    get_itinerary_datetime(count)
    get_itinerary_cost(count)

# ADD METHODS
def add_destination(count, destination, cost, nights):
    total_price = int(cost) * int(nights)
    add_destination = ("INSERT INTO destination "
                "(destination_id, location, cost_per_night, nights, total_price)"
                "VALUES (%s, %s, %s, %s, %s)")
    data_destination = (count, destination, cost, nights, total_price)
    cursor.execute(add_destination, data_destination)
    db.commit()

def add_transportation(count, method, cost):
    add_transportation = ("INSERT INTO transportation "
                "(transportation_id, method, cost)"
                "VALUES (%s, %s, %s)")
    data_transportation = (count, method, cost)
    cursor.execute(add_transportation, data_transportation)
    db.commit()

def add_event(count, title, date, cost):
    add_event = ("INSERT INTO itinerary "
                "(itinerary_id, excursion, date_time, cost)"
                "VALUES (%s, %s, %s, %s)")
    data_event = (count, title, date, cost)
    cursor.execute(add_event, data_event)
    db.commit()

# DELETE METHODS
def delete_destination(location):
    cursor.execute("DELETE FROM Destination WHERE location=%s", location)
    db.commit()
def delete_transportation(method):
    cursor.execute("DELETE FROM transportation WHERE method=%s", method)
    db.commit()
def delete_event(excursion):
    cursor.execute("DELETE FROM Itinerary WHERE excursion=%s", excursion)
    db.commit()
def delete_all():
    cursor.execute("DELETE FROM destination;")
    cursor.execute("DELETE FROM itinerary;")
    cursor.execute("DELETE FROM transportation;")
    db.commit()

# COST METHODS
def cost_destination():
    cursor.execute("SELECT sum(total_price) FROM Destination")
    cost = cursor.fetchall()
    for char in cost:
        for x in char:
            if x != '\'' and x != None:
                print('Destination Cost: ', x)
def cost_transportation():
    cursor.execute("SELECT sum(cost) FROM Transportation")
    cost = cursor.fetchall()
    for char in cost:
        for x in char:
            if x != '\'' and x != None:
                print('Transportation Cost: ', x)
def cost_itinerary():
    cursor.execute("SELECT sum(cost) FROM itinerary")
    cost = cursor.fetchall()
    for char in cost:
        for x in char:
            if x != '\'' and x != None:
                print('Itinerary Cost: ', x)
def total_cost():
    d = 0.0
    t = 0.0
    i = 0.0
    cursor.execute("SELECT sum(total_price) FROM Destination")
    cost = cursor.fetchall()
    for char in cost:
        for x in char:
            if x != '\'' and x != None:
                d = d + x
    cursor.execute("SELECT sum(cost) FROM Transportation")
    cost = cursor.fetchall()
    for char in cost:
        for x in char:
            if x != '\'' and x != None:
                t = t + x
    cursor.execute("SELECT sum(cost) FROM itinerary")
    cost = cursor.fetchall()
    for char in cost:
        for x in char:
            if x != '\'' and x != None:
                i = i + x
    print("Total Cost: ", d + t + i)
    


def main():
    destinationCount = getDestinationMaxKey()+1
    transportationCount = getTransportationMaxKey()+1
    itineraryCount = getItineraryMaxKey()+1
    cursor.execute("select database();")
    while (1>0):
        os.system('clear')
        print('MAIN MENU')
        print('Option 1: Add Information')
        print('Option 2: Delete Information')
        print('Option 3: View Information')
        print('Option 4: View Cost')
        print('Option 5: Quit')
        try:
            option = int(input('Please Choose an Option: '))
        except:
            print('\nError: Please choose a number between 1 and 10\n')
            continue
        if option == 1:
            while (1>0):
                os.system('clear')
                print("ADD INFORMATION")
                print("Option 1: Add Destination Information")
                print("Option 2: Add Transportation Information")
                print("Option 3: Add Event to Itinerary")
                print("Option 4: Go Back")
                try:
                    choice = int(input("Please Choose an Option: "))
                except:
                    continue
                if choice == 1:
                    destination = input("What is the location? ")
                    cost = input("How much will it cost per night? ")
                    nights = input("How many nights will you be staying? ")
                    add_destination(destinationCount, destination, cost, nights)
                    destinationCount+=1
                if choice == 2:
                    method = input("What is the transportation method? ")
                    cost = input("How much will it cost? ")
                    add_transportation(transportationCount, method, cost)
                    transportationCount+=1
                elif choice == 3:
                    title = input("What is the name of the event? ")
                    date = input("What is the date? yyyy-mm-dd ")
                    cost = int(input("What is the cost? "))
                    add_event(itineraryCount, title, date, cost)
                    itineraryCount+=1
                if choice == 4:
                    break
        elif option == 2:
            while 1>0:
                os.system("clear")
                print("DELETE INFORMATION")
                print("Option 1: Delete Destination")
                print("Option 2: Delete Transportation")
                print("Option 3: Delete from Itinerary")
                print("Option 4: Delete All")
                print("Option 5: Go Back")
                try:
                    choice = int(input("Please Choose an Option: "))
                except:
                    continue
                if choice == 1:
                    os.system('clear')
                    for i in range(1, getDestinationMaxKey()+1):
                        view_destination(i)
                    location = input("What is the name of the location? ")
                    tup = (location, )
                    delete_destination(tup)
                if choice == 2:
                    os.system('clear')
                    for i in range(1, getTransportationMaxKey()+1):
                        view_transportation(i)
                    transportation = input("What is the method of transportation? ")
                    tup = (transportation, )
                    delete_transportation(tup)
                if choice == 3:
                    os.system('clear')
                    for i in range(1, getItineraryMaxKey()+1):
                        view_itinerary(i)
                    event = input("What is the name of the event? ")
                    tup = (event, )
                    delete_event(event)
                if choice == 4:
                    print("Destination Information: ")
                    for i in range(1, getDestinationMaxKey()+1):
                        view_destination(i)
                    print("Transportation Information: ")
                    for i in range(1, getTransportationMaxKey()+1):
                        view_transportation(i)
                    print("Itinerary Information")
                    for i in range(1, getItineraryMaxKey()+1):
                        view_itinerary(i)
                    choice = input("Are you sure you want to delete everything? y/n ")
                    if choice == 'y':
                        delete_all()
                if choice == 5:
                    break

        elif option == 3:
            while 1>0:
                os.system('clear')
                print("VIEW INFORMATION")
                print("Option 1: View Destination Information")
                print("Option 2: View Transportation Information")
                print("Option 3: View Itinerary")
                print("Option 4: View All Information")
                print("Option 5: Go Back")
                try:
                    choice = int(input("Please Choose an Option: "))
                except:
                    continue
                if choice == 1:
                    os.system('clear')
                    print('DESTINATION: ')
                    for i in range(1, getDestinationMaxKey()+1):
                        view_destination(i)
                    back = input("\nEnter Any Key To Return: ")
                    if back != '\n':
                        continue
                if choice == 2:
                    os.system('clear')
                    print('TRANSPORTATION: ')
                    for i in range(1, getTransportationMaxKey()+1):
                        view_transportation(i)
                    back = input("\nEnter Any Key To Return: ")
                    if back != '\n':
                        continue
                if choice == 3:
                    os.system('clear')
                    print('ITINERARY: ')
                    for i in range(1, getItineraryMaxKey()+1):
                        view_itinerary(i)
                    back = input("\nEnter Any Key To Return: ")
                    if back != '\n':
                        continue
                if choice == 4:
                    os.system('clear')
                    print("DESTINATION: ")
                    for i in range(1, getDestinationMaxKey()+1):
                        view_destination(i)
                    print("\nTRANSPORTATION: ")
                    for i in range(1, getTransportationMaxKey()+1):
                        view_transportation(i)
                    print("\nITINERARY: ")
                    for i in range(1, getItineraryMaxKey()+1):
                        view_itinerary(i)
                    back = input("\nEnter Any Key To Return: ")
                    if back != '\n':
                        break
                if choice == 5:
                    break
        elif option == 4:
            while (1>0):
                os.system('clear')
                print("COST INFORMATION")
                print("Option 1: Destination Cost")
                print("Option 2: Transportation Cost")
                print("Option 3: Itinerary Cost")
                print("Option 4: Total Cost")
                print("Option 5: Go Back")
                try:
                    choice = int(input("Please Choose an Option: "))
                except:
                    continue
                if choice == 1:
                    os.system('clear')
                    cost_destination()
                    back = input("\nEnter Any Key To Return: ")
                    if back != '\n':
                        continue
                if choice == 2:
                    os.system('clear')
                    cost_transportation()
                    back = input("\nEnter Any Key To Return: ")
                    if back != '\n':
                        continue
                if choice == 3:
                    os.system('clear')
                    cost_itinerary()
                    back = input("\nEnter Any Key To Return: ")
                    if back != '\n':
                        continue
                if choice == 4:
                    os.system('clear')
                    total_cost()
                    back = input("\nEnter Any Key To Return: ")
                    if back != '\n':
                        continue
                if choice == 5:
                    break
        else:
                os.system('clear')
                break



if __name__ == "__main__":
    main()
