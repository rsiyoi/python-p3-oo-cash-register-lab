#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0
    
    def add_item(self, title, price, quantity=1):
        item_total = price * quantity
        self.total += item_total
        
        for _ in range(quantity):
            self.items.append(title)
        self.last_transaction_amount = item_total
    
    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
    
    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0