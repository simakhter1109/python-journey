print("\033[1mE-COMMERCE STORE\033[0m")

cart_value = float(input("Enter cart value: ₹"))
membership = input("Membership (gold/silver/none): ").lower()
coupon = input("Enter coupon code: ").upper()
is_first_order = input("Is this your first order? (yes/no): ").lower()
delivery_distance = float(input("Enter delivery distance (km): "))

discount = 0
delivery_charge = 0


# CART DISCOUNT
if cart_value >= 10000:
    discount += 20
elif cart_value >= 5000:
    discount += 15
elif cart_value >= 2000:
    discount += 10
elif cart_value >= 1000:
    discount += 5
else:
    discount += 0


# MEMBERSHIP DISCOUNT
if membership == "gold":
    discount += 10
elif membership == "silver":
    discount += 5
elif membership == "none":
    pass
else:
    print("Invalid membership type.")
    membership = "none"


# COUPON
if coupon == "SAVE20":
    discount += 20
elif coupon == "SAVE10":
    discount += 10
elif coupon == "":
    print("No coupon applied.")
else:
    print("Invalid coupon code.")


# FIRST ORDER BONUS
if is_first_order == "yes":
    if cart_value >= 2000:
        discount += 5
        print("First order bonus applied!")
    else:
        print("First order bonus requires a cart value of ₹2000+")


# LIMIT MAXIMUM DISCOUNT
if discount > 40:
    discount = 40


# DELIVERY CHARGES
if cart_value >= 2000:
    delivery_charge = 0
elif delivery_distance <= 5:
    delivery_charge = 50
elif delivery_distance <= 10:
    delivery_charge = 100
else:
    delivery_charge = 150


# FINAL BILL
discount_amount = cart_value * discount / 100
final_price = cart_value - discount_amount + delivery_charge

print("\n\033[1mORDER SUMMARY\033[0m")
print(f"Cart Value       : ₹{cart_value:.2f}")
print(f"Discount         : {discount}%")
print(f"Discount Amount  : ₹{discount_amount:.2f}")
print(f"Delivery Charge  : ₹{delivery_charge:.2f}")
print(f"Final Amount     : ₹{final_price:.2f}")

if final_price >= 5000:
    print("\033[1mHigh-value order\033[0m")
elif final_price >= 2000:
    print("\033[1mRegular premium order\033[0m")
else:
    print("\033[1mStandard order\033[0m")

