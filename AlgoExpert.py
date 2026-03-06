'''
Merge overlapping intervals.

write the function bestSeat that takes in an array of integers representing 
seats where 1s are occupied seats and 0s are empty seats. 
The function should return the index of the seat that maximizes the distance to the nearest occupied seat.
 If there are multiple such seats, return the index of the first one. If there are no empty seats, return -1.
'''


def bestSeat(seats):
    # Write your code here.
    bestSeat = -1
    maxSpace = 0
    left = 0
    
    while left < len(seats):
        # Skip if current seat is empty (we need occupied seat to start from)
        if seats[left] == 0:
            left += 1
            continue
            
        # Find the next occupied seat
        right = left + 1
        while right < len(seats) and seats[right] == 0:
            right += 1
        
        # Calculate available space between occupied seats
        if right < len(seats):  # Found another occupied seat
            availableSpace = right - left - 1
            if availableSpace > maxSpace:
                bestSeat = (left + right) // 2
                maxSpace = availableSpace
        
        left = right if right < len(seats) else left + 1
    
    return bestSeat

# Test cases
'''
print("Test cases:")
print(f"[1, 0, 0, 0, 1, 0, 1] -> {bestSeat([1, 0, 0, 0, 1, 0, 1])}")
print(f"[1, 0, 0, 0, 0, 0, 1] -> {bestSeat([1, 0, 0, 0, 0, 0, 1])}")
print(f"[1, 0, 1, 0, 0, 0, 1] -> {bestSeat([1, 0, 1, 0, 0, 0, 1])}")
print(f"[1, 0, 0, 1] -> {bestSeat([1, 0, 0, 1])}")
print(f"[1, 1, 1, 1] -> {bestSeat([1, 1, 1, 1])}")

'''

'''
Zero Sum Subarrays
you're given a list of integers, write a 
function that returns  a boolean representing whether the list contains a
zero-sum subarray. A zero-sum subarray is any contiguous sequence of numbers in the list that sums to 0.    
'''

def SubArrays(nums):
    sum = set([0])
    currentNumber= 0
    for num in nums:
        currentNumber  += num
        if currentNumber in sum:
            return True
        else:
            sum.add(currentNumber)
    return False

'''
Missing Numbers 
You're given an array of integers representing a list of numbers from 1 to n.where n represents the lenght of nums +2 .
this means that exactly two numbers from the range 1 to n are missing from the array.
Write a function that takes in this list and returns the two missing numbers.
numbers,sorted numerically
'''
def missingNumbers(nums):
    includedNums = set(nums)
    sum = []

    for num in range(1 ,len(nums) +3):
        if num not in includedNums:
            sum.append(num)
    return sum
            
def majorityElement(array):
    # Write your code here.
    answer = None
    count =0
    for num in array : 
        if count == 0: 
            answer = num 
        if num == answer:
            count +=1
            answer = num
        else:
            count -= 1
            answer = num
    return answer
'''
Sweet And savory 
You're given an array of integers representing dishes where negative integers represent 
sweet dishes and positive integers represent savory dishes.
You're also given a target integer representing a desired total dish flavor value.

'''
def sweetAndSavory(dishes,target):
    sweetDishes = sorted([dish for dish in dishes if dish < 0],key=abs)
    savoryDishes = sorted([savory for savory in dishes if savory > 0])
    bestPair = [0,0]
    bestDifference = float('inf')
    sweetIndex, savoryIndex = 0,0
    while sweetIndex < len(sweetDishes) and savoryIndex < len(savoryDishes) :
        currentSum = sweetDishes[sweetIndex] +  savoryDishes[savoryIndex]
        if currentSum <= target :
            currentDifference = target - currentSum
            if currentDifference < bestDifference:                 
              bestDifference = currentDifference
              bestPair = [sweetDishes[sweetIndex], savoryDishes[savoryIndex]]
            savoryIndex += 1       
        else:
            sweetIndex +=1

    return bestPair  

'''


'''


def fourNumberSum(array, targetSum):
    quadruplets = []
    hashtable = {}  # Will store: {pair_sum: [[num1, num2], [num3, num4], ...]}
    
    for i in range(len(array)):
        # Look for existing pairs that complement current pair
        for j in range(i + 1, len(array)):
            current_sum = array[i] + array[j]              # Sum of current pair
            complement = targetSum - current_sum           # What we need from other pair
            
            if complement in hashtable:                    # If complement exists
                for pair in hashtable[complement]:         # For each matching pair
                    # Create quadruplet: [previous_pair] + [current_pair]
                    quadruplets.append(pair + [array[i], array[j]])
        
        # Add all pairs with current element to hashtable for future iterations
        for k in range(0, i):
            pair_sum = array[i] + array[k]                # Sum of this pair
            if pair_sum not in hashtable:
                hashtable[pair_sum] = []
            hashtable[pair_sum].append([array[k], array[i]])  # Store the actual values
    
    return quadruplets

            
def spiralTraverse(array):
    startRow,endRow = 0, len(array)-1 
    startCol,endCol = 0, len(array[0])-1

    result = []

    while startRow <= endRow and startCol <= endCol :
        #going right
        for col in range(startCol,endCol + 1):
            result.append(array[startRow][col])
        # going down 
        for row in range(startRow +1,endRow+1):
            result.append(array[row][endCol])
        # goin down left to rigth
        for col in reversed(range(startCol,endCol)):
            result.append(array[endRow][col])
        # going down to up 
        for row in reversed(range(startRow +1,endRow)):
            result.append(array[row][startCol])
        startRow +=1
        endRow -= 1
        startCol +=1
        endCol -= 1 
    return result 

'''
Write a function that takes in a non-empty array of arbitrary intervals,
merges any overlapping intervals, and returns the 
new non-overlapping intervals in no particular order. 

Each interval interval is an array of two integers, with interval[0] as the start of the interval and 
interval[1] as the end of the interval.

Note that back-to-back intervals aren't considered to be
 overlapping. For example, [1, 5] and [6, 7] aren't overlapping; 
 however, [1 , 6] and [5, 7] are indeed overlapping.
'''
        
def mergeOverlappingIntervals(intervals):
    # Sort intervals by start time - use sorted() to return new list
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    mergedIntervals = []
    currentInterval = sortedIntervals[0]
     # Start from index 1 to avoid duplicate
    for nextInterval in sortedIntervals[1:]: 
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval
        # Check if intervals overlap
        if currentIntervalEnd >= nextIntervalStart:
            # Merge overlapping intervals - extend the end time
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            # No overlap - add current interval to result and move to next
            mergedIntervals.append(currentInterval)
            currentInterval = nextInterval
    
    # Don't forget to add the final interval
    mergedIntervals.append(currentInterval)
    return mergedIntervals



def bestSeat(seats):

    bestSeat = -1
    maxSpace =0 
    left = 0

    while left < len(seats) -1 :
        right = left +1 
        while right < len(seats) and seats[right]== 0:
            right +=1
        availableSpace = left + right -1
        if availableSpace >maxSpace:
            bestSeat = (left +right) // 2
            maxSpace = availableSpace
        left  = right
    return bestSeat

            






    
   
   
    






                                                    
            



   
