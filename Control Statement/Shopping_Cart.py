item_prices = [10,20,100,500,600]
total_budget = 500
total_count = 0
for i in item_prices:
    total_budget -= i
    if total_budget <0:
        break
    total_count += 1
print(total_count)