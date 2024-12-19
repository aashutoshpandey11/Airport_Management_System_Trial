import json

class AirportManagementSystem:
    def __init__(self):
        self.flights = []
        self.passengers = []
        self.employees = []

    # Flight Management
    def add_flight(self, flight_id, origin, destination, departure_time):
        flight = {
            "flight_id": flight_id,
            "origin": origin,
            "destination": destination,
            "departure_time": departure_time
        }
        self.flights.append(flight)
        print(f"Flight {flight_id} added successfully.")

    def list_flights(self):
        if not self.flights:
            print("No flights available.")
        else:
            for flight in self.flights:
                print(f"Flight ID: {flight['flight_id']}, Origin: {flight['origin']}, Destination: {flight['destination']}, Departure Time: {flight['departure_time']}")

    # Passenger Management
    def add_passenger(self, name, passport_number, flight_id):
        passenger = {
            "name": name,
            "passport_number": passport_number,
            "flight_id": flight_id
        }
        self.passengers.append(passenger)
        print(f"Passenger {name} added successfully.")

    def list_passengers(self):
        if not self.passengers:
            print("No passengers available.")
        else:
            for passenger in self.passengers:
                print(f"Name: {passenger['name']}, Passport Number: {passenger['passport_number']}, Flight ID: {passenger['flight_id']}")

    # Employee Management
    def add_employee(self, name, employee_id, position):
        employee = {
            "name": name,
            "employee_id": employee_id,
            "position": position
        }
        self.employees.append(employee)
        print(f"Employee {name} added successfully.")

    def list_employees(self):
        if not self.employees:
            print("No employees available.")
        else:
            for employee in self.employees:
                print(f"Name: {employee['name']}, Employee ID: {employee['employee_id']}, Position: {employee['position']}")

# Main Program
def main():
    system = AirportManagementSystem()

    while True:
        print("\n--- Airport Management System ---")
        print("1. Add Flight")
        print("2. List Flights")
        print("3. Add Passenger")
        print("4. List Passengers")
        print("5. Add Employee")
        print("6. List Employees")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            flight_id = input("Enter Flight ID: ")
            origin = input("Enter Origin: ")
            destination = input("Enter Destination: ")
            departure_time = input("Enter Departure Time: ")
            system.add_flight(flight_id, origin, destination, departure_time)
        elif choice == "2":
            system.list_flights()
        elif choice == "3":
            name = input("Enter Passenger Name: ")
            passport_number = input("Enter Passport Number: ")
            flight_id = input("Enter Flight ID: ")
            system.add_passenger(name, passport_number, flight_id)
        elif choice == "4":
            system.list_passengers()
        elif choice == "5":
            name = input("Enter Employee Name: ")
            employee_id = input("Enter Employee ID: ")
            position = input("Enter Position: ")
            system.add_employee(name, employee_id, position)
        elif choice == "6":
            system.list_employees()
        elif choice == "7":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()