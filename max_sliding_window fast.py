# python3
import collections

def max_sliding_window_naive(arr, n,k):
    res=[]
    dq=collections.deque()
    r=l=0

    while r<len(arr):
        while dq and arr[dq[-1]]<arr[r]:#if smaller value exist:
               
            dq.pop()
        dq.append(r)
        
        #if left is out of bound
        if l>dq[0]:
            dq.popleft()
        if (r+1) >=k:
            res.append(arr[dq[0]])
            l+=1
        r+=1
    return res
if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence,n, window_size))

