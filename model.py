import numpy as np

class Categories:
    def __init__(self, created_date : str, cat_id : str, cat_name : str):
        self.created_date = created_date
        self.cat_id = cat_id
        self.cat_name = cat_name

    def display_info(self):
        print(f"Category Info: {self.cat_id} {self.cat_name} {self.created_date}")

class Item:
    def __init__(self, created_date :str, item_id : str, name : str, qr_code : str, price : int, buying_price :int, category : Categories):
        self.created_date = created_date
        self.item_id = item_id
        self.name = name
        self.qr_code = qr_code
        self.price = price
        self.buying_price = buying_price
        self.category = category

    def getProfit(self):
        return int(self.price -self.buying_price)
    
class SaleItem:
    def __init__(self, customer_id : str, created_date : str, item : Item):
        self.customer_id = customer_id
        self.created_date = created_date
        self.item = item

    def getCategoryandProfit(self):
        return (self.item.category.cat_name, self.item.name, self.item.getProfit())