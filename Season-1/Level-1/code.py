'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ITEM_AMOUNT = 100000  
MAX_QUANTITY = 100        
MIN_QUANTITY = 1          
MAX_TOTAL = Decimal('1e6')  
EPSILON = Decimal('1e-6')  

def validorder(order):
    payments = Decimal('0')
    expenses = Decimal('0')

    for item in order.items:
        if item.type == 'payment':
            
            if isinstance(item.amount, (int, float)):
                payments += Decimal(item.amount)
            else:
                return f"Invalid payment amount: {item.amount}"
        elif item.type == 'product':
            
            if isinstance(item.quantity, int) and MIN_QUANTITY <= item.quantity <= MAX_QUANTITY:
                if 0 < item.amount <= MAX_ITEM_AMOUNT:
                    expenses += Decimal(item.amount) * item.quantity
                else:
                    return f"Invalid product cost: {item.amount}"
            else:
                return f"Invalid product quantity: {item.quantity}"
        else:
            return f"Invalid item type: {item.type}"

    if abs(payments) > MAX_TOTAL or expenses > MAX_TOTAL:
        return "Total amount payable for an order exceeded"

    if abs(payments - expenses) > EPSILON:
        return f"Order ID: {order.id} - Payment imbalance: ${payments - expenses:.2f}"
    else:
        return f"Order ID: {order.id} - Full payment received!"







