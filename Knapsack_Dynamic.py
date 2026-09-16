def  Knapsack_Dynamic(capacity,weights,values,n):
    dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weights[i-1]<=w:
                dp[i][w]=max(values[i-1]+dp[i-1][w-weights[i-1]] ,dp[i-1][w])
            else:
              dp[i][w]=dp[i-1][w]
    return dp[n][capacity]
n=int(input("enter the no of items:"))
weights=[]
values=[]
for i in range(n):
    weight=int(input("enter the weight of item"))
    value=int(input("enter the value of item"))
    weights.append(weight)
    values.append(value)
capacity=int(input("enetr the knapsack capacity:"))
max_profit=Knapsack_Dynamic(capacity,weights,values,n)
print("maximum profit:",max_profit)


