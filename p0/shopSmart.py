# shopSmart.py
# ------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""

import shop

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """

    "This if statement checks to see if the list of shops is empty or not"
    if len(fruitShops) == 0:
        return None
   
    """
      The bottom two variables are initialized to the first shop object of the fruitShops 
      list and the total price of the first shop's fruits needed 
    """ 
    bestShop = fruitShops[0]
    bestCost = fruitShops[0].getPriceOfOrder(orderList)

    "This for loop goes through all the shops of the fruitShops list"
    for shop in fruitShops:
        
        """
          This if statement checks to see if the price of the fruits 
          in the next shop is cheaper than that of the previous shop.
          If the fruits combined are cheaper, then this new shop would
          be declared as the bestCost and the bestShop
        """
        if bestCost > shop.getPriceOfOrder(orderList):
            bestCost = shop.getPriceOfOrder(orderList)
            bestShop = shop
    
    "The bestShop object is returned which holds the shop object that is the cheapest"         
    return bestShop 
    
if __name__ == '__main__':
  "This code runs when you invoke the script from the command line"
  orders = [('apples',1.0), ('oranges',3.0)]
  dir1 = {'apples': 2.0, 'oranges':1.0}
  shop1 =  shop.FruitShop('shop1',dir1)
  dir2 = {'apples': 1.0, 'oranges': 5.0}
  shop2 = shop.FruitShop('shop2',dir2)
  shops = [shop1, shop2]
  print "For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName()
  orders = [('apples',3.0)]
  print "For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName()
