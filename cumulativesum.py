list1 = [2,3,5,1,7,8]

cumulative_sum = []
cumulative_sum.append(list1[0])



for i in range(1,(len(list1))):
    cumulative_sum.append(cumulative_sum[i-1] + list1[i])
    
print(cumulative_sum)