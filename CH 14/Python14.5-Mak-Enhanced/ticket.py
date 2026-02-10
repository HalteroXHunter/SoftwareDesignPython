class Ticket:
    BASE_PRICE   = 30
    PARTY_PRICE  = 25
    VIP_PRICE    = 20
    COUPON_PRICE =  5

    def __init__(self, party=False, vip=False, coupons=0):
        self._pregame_party = party
        self._vip_seating = vip
        self._drink_coupons = coupons
        
        self._cost = Ticket.BASE_PRICE
    
    @property
    def cost(self):
        if self._pregame_party:
            self._cost += Ticket.PARTY_PRICE
            
        if self._vip_seating:
            self._cost += Ticket.VIP_PRICE
            
        self._cost += self._drink_coupons*Ticket.COUPON_PRICE
        return self._cost
    
    def print_ticket(self):
        print('    base ticket price: $'
              f'{Ticket.BASE_PRICE}')
        
        if self._pregame_party:
            print('  pregame party price: $'
                  f'{Ticket.PARTY_PRICE}')
            
        if self._vip_seating:
            print('    VIP seating price: $'
                  f'{Ticket.VIP_PRICE}')

        if self._drink_coupons > 0:
            print('   drink coupon price: $'
                  f'{self._drink_coupons*Ticket.COUPON_PRICE}'
                  f' = {self._drink_coupons} x '
                  f'{Ticket.COUPON_PRICE}')
