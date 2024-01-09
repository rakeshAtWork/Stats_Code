from heapq import heappop, heappush
import math

def get_dist(x,y):
    return math.sqrt(x**2 + y**2)

def kClosest(points,k):
    n = len(points)
    min_heap = []

    for i in range(n):
        x = points[i][0]
        y = points[i][1]
        heappush(min_heap,(get_dist(x,y),points[i]))

    result = []

    for i in range(k):
        result.append(heappop(min_heap)[1])

    return result

# Driver code

points = [[3,3], [5,-1], [-2, 4]]
k = 2
## function calling
result = kClosest(points, k)
print("K Closest Points to the origin are:",result)
