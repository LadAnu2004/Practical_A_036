num=[]

for i in range(1,101):
    if ( i % 2 != 0):
        num.append(i)
print("Odd numbers Between 1 to 100:")
print(num)
        
minimum_num=min(num)
print("Minimum odd numbers:",minimum_num)

maximum_num=max(num)
print("Maximum odd numbers:",maximum_num)

sum_odd = sum(num)
print("Sum  odd numbers:", sum_odd)
