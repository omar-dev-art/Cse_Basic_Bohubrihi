user_area = 'gulshan'

total_purchase_price= 400

if user_area in ['mirpur','farmgate','dhanmondi']:
    if total_purchase_price >=600:
        print("shipping is free")
    elif total_purchase_price >=300 and total_purchase_price <600:
        print("shipping price is 80")
    else:
        print("shipping is 150")

elif user_area in ['mohakhali','gulshan']:
    if total_purchase_price >=800:
        print("shipping is free")
    elif total_purchase_price >=500 and total_purchase_price <800:
        print("shipping price is 100")
    else:
        print("shipping price is 200")

else :
    print("shipping currently not available")