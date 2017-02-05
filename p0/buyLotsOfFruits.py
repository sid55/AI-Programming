# buyLotsOfFruit.py
# -----------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
To run this script, type

  python buyLotsOfFruit.py
  
Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""

fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,
              'limes':0.75, 'strawberries':1.00}

"""
This errorValue is set to 1 when a fruit does not exist in fruitPrices.
It is set to 2 when the orderList provided by the user is empty.
"""
errorValue = 0

def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples
            
    Returns cost of order
    """
    global errorValue

    "This is the total cost of the fruits initialized to 0.0"
    totalCost = 0.0
    
    "This if statement checks to see if the list is empty or not"
    if len(orderList) == 0:
        errorValue = 2
        return None

    "This for loop loops through all the fruits in orderList"
    for fruit, pounds in orderList:

        """
        The if/else statement checks if the fruit exists in fruitPrices.
        Exists => The pounds of the fruit is multiplied by the amount of that fruit.
                  This cost is then added to the total cost.
        Not Exists => The total cost will be set to None and the error value is set to 1.
                      In the main, there is check to see if the error value is set and if
                      it is, an error messege is printed.
        """

        if fruit in fruitPrices:
            totalCost += fruitPrices[fruit] * pounds
        else:
            errorValue = 1  
            return None          
 
    "The total cost is returned after the calculations are made"
    return totalCost
    
# Main Method    
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [ ('apples', 2.0), ('pears', 3.0), ('limes', 4.0) ]
    print 'Cost of', orderList, 'is', buyLotsOfFruit(orderList)

    "This errorValue checks if there has been an error or not"
    if errorValue == 1:
        print 'ERROR: A fruit you are looking for does not exist'
    elif errorValue == 2:
        print 'ERROR: The list of fruits and pounds you have provided is empty'

