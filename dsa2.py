# 1. Finding Prefsum:1
def prefsum(V): 
    N = len(V)
    prefsum = [0]*N
    prefsum[0] = V[0]
    for i in range(1,N):
        prefsum[i]= prefsum[i-1]+V[i]
    return(prefsum)

# 1. Finding Prefsum:2
def prefsum(V):
    N = len(V) 
    prefsum = []
    currsum = 0
    for i in range(0,N):
        currsum = currsum+V[i]
        prefsum.append(currsum)
    return(prefsum)  

def maxsum(A,k):
    s = 0
    e = k-1
    maxsum = float("-inf")
    N = len(A)
    
    while e+1 <= N:
        sum1 = sum(A[s:e+1])
        maxsum = max(maxsum,sum1)
        s += 1
        e += 1

    return maxsum

def maxsum(A,k):
    s = 0
    
    maxsum = float("-inf")
    N = len(A)
    M = prefsum(A)
    while s+k <= N:
        if s ==0:
            sum1 = M[s+k]
        else:
            sum1 = M[s+k]-M[s-1]
        maxsum = max(maxsum,sum1)
        s += 1

    return maxsum 

# 2. Pick from both sides: 1 (The way I solved)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        s = 0
        e = N-B-1
        maxsum = float("-inf")
        prefsum = [0]*N
        prefsum[0] = A[0]
        for i in range(1,N):
            prefsum[i]=prefsum[i-1]+A[i]
        totsum=prefsum[-1]
        if B == N:
            return(totsum)
        while (e<=N-1):
            if s == 0:
                sum1 = prefsum[e]
            else:
                sum1 = prefsum[e] - prefsum[s-1]
            ans = totsum - sum1
            maxsum = max(maxsum,ans)
            s += 1
            e += 1
            
        return(maxsum)

# 2. Pick from both sides: 2 (The ideal solution)

class Solution:
    def solve(self, A, B):
        N = len(A)

        # prefix sum
        pre = [0] * (N + 1)
        for i in range(1, N + 1):
            pre[i] = pre[i - 1] + A[i - 1]

        # suffix sum
        suf = [0] * (N + 1)
        for i in range(1, N + 1):
            suf[i] = suf[i - 1] + A[N - i]

        maxsum = float("-inf")

        # Try all combinations:
        # k from front, B-k from back
        for k in range(B + 1):
            front = pre[k]                    # k front elements
            back  = suf[B - k]                # B-k back elements
            maxsum = max(maxsum, front + back)

        return maxsum

# 3. Find Maximum Sub Array Sum: 1 (Brute Force Method) O(N^2)

class Solution:
    def maxi(A):
        
        maxsum = float("-inf")
        N = len(A)
        for i in range(0,N):
            total = 0
            for j in range(i,N):
                total = total + A[j]
                maxsum = max(maxsum,total)
        return maxsum
    
# 3. Find Maximum Sub Array Sum: 2

# 4. Min steps in infinite grid:

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        steps = 0
        N = len(A)
        for i in range(1,N): 
            diffA = abs(A[i-1]-A[i])
            diffB = abs(B[i-1]-B[i])
            min = max(diffA,diffB)
            
            steps = steps+min
        return steps

# 5. Finding Largest element in an Array 

class Solution:
    def largestel(self, A):
        large = A[0]
        N = len(A)
        for i in range(1,N):
            large = max(large,A[i])
        return large
    
obj = Solution()
arr = [4, 15, 2, 99, 43]

print(obj.largestel(arr))

# 6. Finding Second largest element in an Array: 1(Better than Brute force)

class Solution:
    def seclargestel(self,A):
        large = A[0]
        seclarge = float("-inf")
        N = len(A)
        for i in range(1,N):
            large = max(large,A[i])
        for i in range(0, N):
            if A[i] > seclarge and A[i] != large:
                seclarge = A[i]
        return seclarge
    
obj = Solution()
arr = [4, 15, 2, 99, 43]

print(obj.seclargestel(arr))

# 6. Finding Second largest element in an Array: 2(Optimal)

class Solution:
    def seclargestel(self,A):
        large = float("-inf")
        seclarge = float("-inf")
        N = len(A)
        for i in range(0,N):
            if A[i]>large:
                seclarge = large
                large = A[i]
            elif A[i]>seclarge and A[i]!=large:
                seclarge = A[i]
        return seclarge
    
obj = Solution()
arr = [4, 15, 2, 99, 43]

print(obj.seclargestel(arr))

# 7. Check if the array is sorted or not : 1(That is how I solved)

class Solution:
    def sorted(self,A):
        Conclusion = True
        N =len(A)
        for i in range(1,N-1):
            if A[i-1]>=A[i]:
                Conclusion = False
                break
        return Conclusion
            
obj = Solution()
arr = [4,15, 2, 99, 43]

print(obj.sorted(arr))

# 7. Check if the array is sorted or not : 2(That is how youtuber solved) 

class Solution:
    def sorted(self,A):
        
        N =len(A)
        for i in range(1,N-1):
            if A[i-1]>=A[i]:
                return False
        return True
            
obj = Solution()
arr = [4,15, 2, 99, 43]

print(obj.sorted(arr))

# 8. Remove Duplicates from sorted array[in place]: 1(Brute force)

class Solution:
    def remdup(self, A):
        
        N = len(A)
        freq_map = {}
        for i in range(0,N):
                freq_map[A[i]] = 0
                freq_map.update(freq_map)
        j = 0
        for k in freq_map:
                A[j] = k
                j += 1
        return j
    
obj = Solution()
A = [1,1,1,2,3,4,4,7,9,9,9,10]
print(obj.remdup(A))

# 8. Remove Duplicates from sorted array[in place]: 2(Optimal)
class Solution:
    def remdup(self, A):
        N = len(A)
        i = 0
        if N==1:
            return 1
        for j in range(1,N):
            if A[i] != A[j]:
                i += 1
                A[i]=A[j]
        return i+1
    
# 9. Right Rotate an array by 1 place: 1 (By the use of slicing)

class Solution:
    def rot(self, A):
        N = len(A)
        A[:] = [A[-1]] + A[0:N-1]
        return A
    
# 9. Right Rotate an array by 1 place: 2

class solution:
    def rot(self, A):
        N = len(A)
        temp = A[-1]

        for i in range(N-2,-1,-1):
            A[i+1] = A[i]
        A[0] = temp

        return A
    
# 10. Right Rotate an Array by K places: 1 (Slicing)

class solution:
    def rot(self, A, k):
        N = len(A)
        r = k%N
        A[:] = A[-r:N] + A[0:-r]
        return A
    
# 10. Right Rotate an Array by K places: 2 

class solution:
    def rot(self, A, k):
        N = len(A)
        r = k%N
        for _ in range(0,r):
            e = A.pop()
            A.insert(0,e)
        return A
 
    
# 11. Reversing an Array: 1

    def reverse(A, left, right):
        while left<right:
            A[left],A[right] = A[right],A[left]
            left +=1
            right -=1
        return A
    
# 10. Right Rotate an Array by K places: 3

# revrse last k elements
# reverse remaining element
# reverse whole array

