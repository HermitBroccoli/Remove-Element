nums = [3, 2, 2, 3]

def y(val):
    l = []
    for i in range(len(nums)):
        if nums[i] == val:
            l.append(i)

    l.reverse()

    for j in range(len(l)):
        nums.pop(l[j])
    
    l.clear()

    return len(nums)

print(y(3))