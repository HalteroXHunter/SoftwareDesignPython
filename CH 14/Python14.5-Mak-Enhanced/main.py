from ticket import Ticket

def print_ticket(name, ticket):
    print()
    print(f"{name}'s ticket:")
    ticket.print_ticket()
    print(f"TOTAL COST: ${ticket.cost}")

if __name__ == '__main__':
    john_ticket = Ticket(True, True, 2)
    print_ticket('John', john_ticket)

    mary_ticket = Ticket(True, False, 3)
    print_ticket('Mary', mary_ticket)

    leslie_ticket = Ticket()
    print_ticket('Leslie', leslie_ticket)

    sidney_ticket = Ticket(False, True, 1)
    print_ticket('Sidney', sidney_ticket)
