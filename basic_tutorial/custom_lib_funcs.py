# this function returns the longest word length in an array
def longestStrLengthInArray(arr): 
    if (not arr) or (not isinstance(arr, list)):
        return 0
    else:
        sortedStrArr = sorted(arr, key=len)
        return len(sortedStrArr[-1])

