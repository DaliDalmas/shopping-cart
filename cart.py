from items import shelf
import pandas as pd

class Cart:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance
        self.cart_items = []

    def check_quantity(self, id, quantity):
        called_item = [item for item in shelf if item['id']==id][0]
        if quantity<=called_item['stock']:
            return True
        else:
            return False

    def add_to_cart(self):
        df = pd.DataFrame(shelf)
        while True:
            print("** ADD AN ITEM TO CART **")
            print(df)
            id = int(input('''select the id of the item you want to buy: '''))

            quantity = int(input('''How many do you want: '''))
            if self.check_quantity(id, quantity):
                called_item = [item for item in shelf if item['id']==id][0]
                called_item['quantity'] = quantity
                self.cart_items.append(called_item)
                checkout = input("Checkout? (y/n): ")
                if checkout == 'y':
                    break;
                continue;
            else:
                print("The quantity you have selected is more than stock, try again")
                continue;




Dali = Cart(12,1000000)
Dali.add_to_cart()
print(Dali.cart_items)