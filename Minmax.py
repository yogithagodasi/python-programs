def find_min_max(arr,low,high):
    if low==high:
        return arr[low],arr[low]
    if high==low+1:
        if arr[low]<arr[high]:
            return arr[low],arr[high]
        else:
            return arr[high],arr[low]
    mid=(low+high)//2
    min1,max1=find_min_max(arr,low,mid)
    min2,max2=find_min_max(arr,mid+1,high)
    minimum=min(min1,min2)
    maximum=max(max1,max2)
    return minimum,maximum
n=int(input("enter the no of elements"))
arr=list(map(int,input("enter the elements").split()))
minimum,maximum=find_min_max(arr,0,n-1)
print("Minimum element:", minimum)
print("Maximum element:", maximum)   