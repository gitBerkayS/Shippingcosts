#Shipping costs
weight =input("Determine your weight, to calculate the cheapest form of shipping.\n")
print("You've enetered:", weight, "kg")
print("")
try:
    weight = float(weight)
except ValueError:
    print("Please enter a valid number and RERUN")
    exit()

#Ground Shipping
flat_rate = 20.00
if weight <= 2:
  shipping_price_ground = flat_rate + (1.50 * weight)
elif weight <= 6:
  shipping_price_ground = flat_rate + (3.00 * weight)
elif weight <=10:
  shipping_price_ground = flat_rate + (4.00 * weight)
else:
  shipping_price_ground = flat_rate + (4.75 * weight)
print("Ground shipping price: $", shipping_price_ground)

#Premium Ground Shipping
shipping_price_premium = 125.00
print("Premium ground shipping price: $", shipping_price_premium)

#Drone Shipping
flat_rate = 0.00
if weight <= 2:
  shipping_price_drone = flat_rate + (4.5 * weight)
elif weight <= 6:
  shipping_price_drone = flat_rate + (9.00 * weight)
elif weight <=10:
  shipping_price_drone = flat_rate + (12.00 * weight)
else:
  shipping_price_drone = flat_rate + (14.25 * weight)
print("Drone shipping price: $", shipping_price_drone)

print("")
if shipping_price_ground < shipping_price_premium and shipping_price_drone:
  print("You should use GROUND shipping. It seems to be the cheapest :)")
elif shipping_price_premium < shipping_price_ground and shipping_price_drone:
  print("You should use PREMIUM shipping. It seems to be the cheapest :)")
elif shipping_price_drone < shipping_price_ground and shipping_price_premium:
  print("You should use DRONE shipping. It seems to be the cheapest :)")
elif shipping_price_ground == shipping_price_premium or shipping_price_drone:
  print("I've recognized multiple prices that are simillar. You should use the quickest shipping option :)")
elif shipping_price_drone == shipping_price_premium or shipping_price_ground:
  print("I've recognized multiple prices that are simillar. You should use the quickest shipping option :)")
else:
  print("Please report this option to an admin. It seems like you've found a bug!")
exit()

