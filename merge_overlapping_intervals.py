def mergeOverlappingIntervals(intervals):
    print(intervals) 
    # Write your code here.
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    print (sortedIntervals)
    #return [[]]


intervals = [
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10]
]
mergeOverlappingIntervals(intervals)
# sort by starting time of intervals
# iterate thru array and compare adjanct arrays
# to merge interval: taking starting value of first array, and max of second/
