#Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of numbers contained in that array. 
#The first number in the output array should be the first number in the range while the second number should be the last number in the range.
#Arange of numbers is defined as a set of numbers that come right after each other in the set of real integers. 
#For instance, the output array (2,6]represents the range (2,3,4,5,6), which isarange of length 5.
#Note that numbers do not need to be ordered or adjacent in the array in order to form a range. Assume that there will only be one largest range.
#Sample input: [1, 11,3,0,15,5,2,4,10,7,12,6] 
#Sample output: (0,7)


def largestRange(array):

    numbers ={x:0 for x in array}
    left = right = 0
    for number in array :
        if numbers[number] == 0 :
            left_count = number - 1
            right_count = number + 1


            while left_count in numbers:
                numbers[left_count] = 1
                left_count -= 1
            left_count += 1

            
            while right_count in numbers:
                numbers[right_count] = 1
                left_count += 1
            right_count -= 1

            if (right-left) <=(right_count-left_count):
                right = right_count
                left = left_count
    return[left, right]