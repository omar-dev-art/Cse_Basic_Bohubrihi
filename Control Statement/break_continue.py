for i in range(1,11):
    if i ==5 :
        print("outside of loop")
        break

    print(i)
#print("outside of loop")
for i in range(1,11):
    if i >5 and i<8:
        continue
    print(i)