def get_ticket_price(age):
    if 1 <= age <= 12:
        return 150
    elif 13 <= age <= 25:
        return 350
    elif 26 <= age <= 49:
        return 600
    elif  50 <= age <=100 :
        return 300
    else:
        raise ValueError("Invalid age entered!")

def main():
    total_amount = 0
    tickets = []

    try:
        num_tickets = int(input("How many tickets do you want to book? "))
        if num_tickets <= 0:
            raise ValueError("Number of tickets must be positive.")

        for i in range(num_tickets):
            print(f"\nBooking Ticket {i+1}:")
            name = input("Enter your name: ")
            
            try:
                age = int(input("Enter your age: "))
                if age <= 0:
                    raise ValueError("Age must be positive.")
                price = get_ticket_price(age)
                tickets.append((name, age, price))
                total_amount += price
                print(f"{name}, your ticket amount is: ₹{price}")

            except ValueError as ve:
                print(f"Error: {ve}")
                print("Skipping this ticket due to invalid age.")

        print("\nBooking Summary:")
        for i, (name, age, price) in enumerate(tickets, start=1):
            print(f"Ticket {i}: Name: {name}, Age: {age}, Amount: ₹{price}")

        print(f"\nTotal amount for {len(tickets)} valid ticket(s): ₹{total_amount}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
