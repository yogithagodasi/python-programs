def fractional_knapsack(capacity,items):
    items.sort(key=lambda x:x[0]/x[1],reverse=True)
    total_profit=0.0
    for weight,value in items:
        if capacity>=weight:
            capacity-=weight
            total_profit+=value
        else:
            total_profit+=value*(capacity/weight)
            break
    return total_profit
n=int(input("enter the no of items"))
items=[]
for i in range(n):
    weight=float(input("enter the weight{i+1}:"))
    value=float(input("enter the value{i+1}:"))
    items.append((weight,value))
capacity=int(input("enter the knapsack weight"))
max_profit=fractional_knapsack(capacity,items)
print("maximum profit:",round(max_profit,2))
