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

