#maximum sum of a subarray of size n
def MaxSumSubarray(arr,k):
    window_sum=sum(arr[:k]) #8
    max_sum=window_sum

    for i in range(len(arr)-k): #6-3=3 range(0,3), range(1,3), range(3)
        window_sum=window_sum-arr[i]+arr[i+k] #8-2+1=7, 7-1+3=9 , 9-5+2=6
        max_sum=max(max_sum,window_sum) #8,7    8,9    9,6
    return max_sum

k=3
arr = [2, 1, 5, 1, 3, 2]
print(MaxSumSubarray(arr,k))

