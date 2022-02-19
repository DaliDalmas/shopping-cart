from items import shelf as SHELF
import pandas as pd

class Cart:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance
        self.cart_items = []
        self.total_items_value = None
        self.shelf = SHELF

    def __repr__(self) -> str:
        return f'A class for {self.account} account id with {self.balance} account balance.'

    def _check_quantity(self, id, quantity):
        called_item = [item for item in self.shelf if item['id']==id][0]
        if quantity<=called_item['stock']:
            return True
        else:
            return False

    def add_to_cart(self):
        df = pd.DataFrame(self.shelf)
        while True:
            print("** ADD AN ITEM TO CART **")
            print(df)
            id = int(input('''select the id of the item you want to buy: '''))

            quantity = int(input('''How many do you want: '''))
            if self._check_quantity(id, quantity):
                called_item = [item for item in self.shelf if item['id']==id][0]
                called_item['quantity'] = quantity
                self.cart_items.append(called_item)
                checkout = input("Checkout? (y/n): ")
                if checkout == 'y':
                    break;
                continue;
            else:
                print("The quantity you have selected is more than stock, try again")
                continue;

    def remove_from_cart(self):
        while True:
            if len(self.cart_items)==0:
                print("You don't have items in cart")
                return None
            print("Here is your cart:")
            print(pd.DataFrame(self.cart_items))
            print('To quit type a value of id that is not in your cart\n')
            id = int(input('Select id of the item you want remove.: '))
            self.cart_items = [item for item in self.cart_items
                                if item['id']!=id]
            done = input('Do you want to continue removing from cart? (y/n)')
            if done == 'y':
                continue
            else:
                break;
        return None

    def checkout_and_pay(self):
        self.total_items_value = sum(
                                [float(item['unit price'])*float(item['quantity'])
                                for item in self.cart_items]
                            )
        if self.total_items_value>self.balance:
            print("You have insufficient funds")
            return None
        elif len(self.cart_items)==0:
            print("You dont have items in your cart")
            return None
        else:
            self.balance = self.balance-self.total_items_value
            shelf_df = pd.DataFrame(self.shelf)
            cart_df = pd.DataFrame(self.cart_items)
            print(cart_df.columns)
            cart_df.columns = ['id', 'cart_name', 'cart_price',
            'cart_rating', 'cart_stock','quantity']
            df = pd.merge(shelf_df, cart_df, on='id', how='left')
            print(df.columns)
            df['stock'] = df['stock'] - df['quantity_y']
            df = df[[col for col in df.columns if ('cart' not in col) ]]\
                .drop(['quantity_x','quantity_y'], axis=1)
            self.shelf = df.to_dict('records')
            return self.shelf, self.account, self.balance, self.cart_items