def rate(downloads):
    if downloads <= 99: # test: 50
        discountRate = 0.0
    elif downloads >= 100 and downloads <= 179: #test: 150
        discountRate = .04
    elif downloads >= 180 and downloads <= 339: #test: 200
        discountRate = .075
    else: # test: 500
        discountRate = .09

    return discountRate #^

unitCost = 3.89
downloads = int(input("Enter the number of downloads: "))

if downloads > 600: # test: 700
    print("You may only download up to 600 movies per year.")
else:
    discountRate = rate(downloads)
    costBeforeDiscount = unitCost * downloads
    discountTotal = costBeforeDiscount * discountRate
    costAfterDiscount = costBeforeDiscount - discountTotal
    print("Your cost before discount is: $", costBeforeDiscount)
    print("Your discount rate is: ", discountRate, "%")
    print("Your total is: $", costAfterDiscount)
    print("Your amount saved is: $", discountTotal)

#^ Had a lot problems returning the correct value until
#^ changing the conditions from "and" to "or"
