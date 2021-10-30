def is_monotonic(nums):
    ans = True
    for i in range(0, len(nums)-1):
        j=i+1
        while ans == True:
            if nums[i] <= nums[j]:
                ans = True
            else: ans = False
            break
    if ans == False:
        ans = True
        for i in range(0, len(nums) - 1):
            j=i+1
            while ans == True:
                if nums[i] >= nums[j]:
                    ans = True
                else:
                    ans = False
                break
    return (ans)

print(is_monotonic([1, 3, 2]))