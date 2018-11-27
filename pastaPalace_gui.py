from graphics import *

def main():
    win = GraphWin("Build your Order", 600, 600)
    win.setCoords(0.0, 0.0, 12.0, 12.0)

    title = Text(Point(6.0, 11.0), "PASTA PALACE")
    title.setFill("red")
    title.setSize(25)
    title.setStyle("italic")
    title.draw(win)

    Line(Point(6.0, 0.0), Point(6.0, 12.0)).draw(win)
    Line(Point(0.0, 6.0), Point(12.0, 6.0)).draw(win)

    # Top left section
    textEntree = Text(Point(3.0, 10.0), "Choose your entrees")
    textEntree.draw(win)
    Text(Point(2.5, 9.5), "Spaghetti with tomato sauce: $8.99").draw(win)
    Text(Point(2.0, 9.0), "Meatballs: $2.00 (each)").draw(win)
    Text(Point(2.0, 8.5), "Vegetable lasagna: $10.25").draw(win)
    Text(Point(1.5, 8.0), "Baked ziti: $9.50").draw(win)
    spaghettiInput = Entry(Point(5.0, 9.5), 5)
    spaghettiInput.setText("0")#*
    spaghettiInput.draw(win)
    meatballInput = Entry(Point(5.0, 9.0), 5)
    meatballInput.setText("0")#*
    meatballInput.draw(win)
    lasagnaInput = Entry(Point(5.0, 8.5), 5)
    lasagnaInput.setText("0")#*
    lasagnaInput.draw(win)
    zitiInput = Entry(Point(5.0, 8.0), 5)
    zitiInput.setText("0")#*
    zitiInput.draw(win)

    # Top right section
    textExtra = Text(Point(9.0, 10.0), "Choose your extras")
    textExtra.draw(win)
    Text(Point(8.75, 9.5), "Sauce on side: $2.50 (extra) [Y/N]").draw(win)
    Text(Point(8.75, 9.0), "Grated parmesan: (no charge) [Y/N]").draw(win)
    sauceInput = Entry(Point(11.0, 9.5), 5)
    sauceInput.draw(win)
    cheeseInput = Entry(Point(11.0, 9.0), 5)
    cheeseInput.draw(win)

    # Bottom left section
    textUser = Text(Point(3.0, 5.0), "Enter your information")
    textUser.draw(win)
    Text(Point(1.0, 4.5), "Name:").draw(win) # Do we need to do something with
    Text(Point(1.0, 4.0), "Address:").draw(win) # the name and address?
    nameInput = Entry(Point(4.0, 4.5), 20)
    nameInput.draw(win)
    addressInput = Entry(Point(4.0, 4.0), 20)
    addressInput.draw(win)
    button = Rectangle(Point(2.25, 3.5), Point(3.75, 2.5))
    button.setOutline("green")
    button.draw(win)
    Text(Point(3.0, 3.0), "Checkout").draw(win)

    #Bottom right section
    textSection = Text(Point(9.0, 5.0), "Order details")
    textSection.draw(win)
    Text(Point(6.75, 4.5), "Tax due:").draw(win)
    taxDueOutput = Text(Point(11.0, 4.5), "")
    taxDueOutput.draw(win)
    Text(Point(6.75, 4.0), "Total:").draw(win)
    totalOutput = Text(Point(11.0, 4.0), "")
    totalOutput.draw(win)
    Text(Point(7.0, 3.5), "Delivery time:").draw(win)
    timeOutput = Text(Point(11.0, 3.5), "")
    timeOutput.draw(win)

    win.getMouse()

    # Not sure if variables need to be initialized
    taxRate = 0.072
    priceSpaghetti = 8.99
    priceMeatball = 2.0
    priceLasagna = 10.25
    priceZiti = 9.5
    priceSauce = 2.5
    priceCheese = 0.0 # If Pasta Palace decides to charge for parmesan in the future,
    quantitySpaghetti = 0 # I think programming like this would make it easier
    quantityMeatball = 0
    quantityLasagna = 0
    quantityZiti = 0
    quantitySauce = ""
    quantityCheese = ""
    name = ""
    address = ""
    deliveryTime = 0

    quantitySpaghetti = int(spaghettiInput.getText())
    quantityMeatball = int(meatballInput.getText())
    quantityLasagna = int(lasagnaInput.getText())
    quantityZiti = int(zitiInput.getText())
    quantitySauce = sauceInput.getText()
    quantityCheese = cheeseInput.getText()

    totalSpaghetti = quantitySpaghetti * priceSpaghetti
    totalMeatball = quantityMeatball * priceMeatball
    totalLasagna = quantityLasagna * priceLasagna
    totalZiti = quantityZiti * priceZiti
    #totalSauce    Not sure if this is needed
    #totalCheese    Not sure if this is needed

    totalSubtotal = totalSpaghetti + totalMeatball + totalLasagna + totalZiti #totalSauce + totalCheese    Not sure if this is needed
    taxDue = totalSubtotal * taxRate
    totalCost = totalSubtotal * taxRate

    if quantitySauce.find("Y") or quantityCheese.find("Y"):
        totalCost = totalCost + priceSauce + priceCheese
    #else:    Not sure if this is needed

    if quantityLasagna > 0 or quantityZiti > 0:
        deliveryTime = 20
    else:
        deliveryTime = 10

    taxDueOutput.setText(round(taxDue, 2))#$ # Formats output like money
    totalOutput.setText(round(totalCost, 2))#$ # Formats output like money
    timeOutput.setText(deliveryTime)#$
main()
#* I got a lot of errors without these because if the user doesn't type
# anything into the box, then a blank space would try to be converted to
# an integer.

#$ I got a lot of errors when I tried the code below  because the object was
# already drawn:
#   taxDueOutput.setText(taxDue)
#   taxDueOutput.draw(win)
