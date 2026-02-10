import random
from enum import Enum

class State(Enum):
    READY       = 1
    VALIDATING  = 2
    TICKET_SOLD = 3
    SOLD_OUT    = 4
    
    def __str__(self): 
        return self.name

class Validity(Enum):
    YES     = 1
    NO      = 2
    UNKNOWN = 3
    
    def __str__(self): 
        return self.name

class TicketMachine:
    def __init__(self, count):
        self._state = State.READY
        self._count = count
        self._card_inserted = False
        self._card_validity = Validity.UNKNOWN
    
    def _insert_credit_card(self):
        match self._state:
            case State.READY:
                if not self._card_inserted:
                    print("Validating your credit card.")
                    
                    self._card_inserted = True
                    self._card_validity = Validity.UNKNOWN
                    self._state = State.VALIDATING
                    
                elif self._card_validity == Validity.NO:
                    print("*** Credit card rejected. ***")
                    print("Remove your card.")
                    
                else:
                    print("Remove the credit card that's "
                          "already inserted.")
                
            case State.VALIDATING: 
                print("Still checking your "
                      "credit card's validity.")
            
            case State.TICKET_SOLD:
                print("Take the ticket you've "
                      "already bought.")
                
                self._card_inserted = True;
                self._card_validity = Validity.UNKNOWN;
        
            case State.SOLD_OUT:
                print("*** Machine sold out. ***")
                print("Remove your credit card")
    
                self._card_inserted = True;
                self._card_validity = Validity.UNKNOWN;

    def _check_validity(self):
        match self._state:
            case State.READY:
                if not self._card_inserted:
                    print("First insert your credit card.")
                    
                elif self._card_validity == Validity.YES:
                    print("Remove the credit card that's "
                          "already inserted.")
                    
                else:
                    print("*** Credit card rejected. ***")
                    print("Remove your card.")
                
            case State.VALIDATING:
                if self._card_validity == Validity.UNKNOWN:
                    self._card_validity = Validity.YES \
                        if random.randint(0, 2) < 2 \
                        else Validity.NO
                        
                if self._card_validity == Validity.YES:
                    print("Your credit card is validated.")
                    print("Take your ticket.")
                    
                    self._state = State.TICKET_SOLD
                    
                else:
                    print("*** Credit card rejected. ***")
                    print("Remove your card.")
    
                    self._state = State.READY;
        
            case State.TICKET_SOLD:
                print("Take the ticket that you've "
                      "already bought.")
            
            case State.SOLD_OUT:
                print("*** Machine sold out. ***")
    
                if self._card_inserted:
                    print("Remove your credit card.")
        
    def _take_ticket(self):
        match self._state:
            case State.READY:
                if not self._card_inserted:
                    print("First insert your credit card.")
                    
                elif self._card_validity == Validity.UNKNOWN:
                    print("Still checking your "
                          "credit card's validity.")
                
                elif self._card_validity == Validity.YES:
                    print("Take the ticket that you've "
                          "already bought.")
                    print("Remove your card.")
                
                else:
                    print("*** Credit card rejected. ***")
                    print("Remove your card.")
                
            case State.VALIDATING:
                if self._card_validity == Validity.UNKNOWN:
                    print("Still checking your "
                          "credit card's validity.")
                    
                elif self._card_validity == Validity.YES:
                    print("Your card is already validated.")
                    print("Take your ticket.")
                    
                else:
                    print("*** Credit card rejected. ***")
                    print("Remove your card.")
        
            case State.TICKET_SOLD:
                print("Remove your credit card.")
                print("Enjoy the game!")
    
                self._count -= 1
                
                if self._count > 0:
                    self._state = State.READY
                else:
                    self._state = State.SOLD_OUT
        
            case State.SOLD_OUT:
                print("*** Machine sold out. ***")
    
                if self._card_inserted:
                    print("Remove your credit card.")
    
    def _remove_credit_card(self):
        match self._state:
            case State.READY:
                if self._card_inserted:
                    print("You've removed your credit card.")
                    
                else:
                    print("No credit card inserted.")
    
                self._card_inserted = False
                self._card_validity = Validity.UNKNOWN
                
            case State.VALIDATING:
                if not self._card_inserted:
                    print("No credit card inserted.")
                    
                elif self._card_validity == Validity.NO:
                    print("*** Credit card rejected. *** ")
                    print("Remove your card.")
                    
                else:
                    print("You removed your credit card "
                          "before it was validated.")
                    print("No sale.")
    
                self._card_inserted = False
                self._card_validity = Validity.UNKNOWN
                self._state = State.READY
        
            case State.TICKET_SOLD:
                print("First take your ticket.")
        
            case State.SOLD_OUT:
                if self._card_inserted:
                    print("You've removed your credit card.")
    
                    self._card_inserted = False
                    self._card_validity = Validity.UNKNOWN

                else:
                    print("No credit card inserted.")
                    
    def run(self):
        command = -1
        
        while command != 0:
            print()
            print("1: insert card, 2: check card validity")
            print("3: take ticket, 4: remove card, 0: quit")
            print(f"[{self._state} {self._count}"
                  f" {self._card_inserted}"
                  f" {self._card_validity}]")
            command = int(input("Command? "))
            
            match command:
                case 1: self._insert_credit_card()
                case 2: self._check_validity()
                case 3: self._take_ticket()
                case 4: self._remove_credit_card()
    
                case 0: 
                    print()
                    print("Done!")
    
                case _: 
                    print("*** Invalid command. ***")
