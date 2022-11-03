# python3


def max_sliding_window_naive(arr, n,k):
    windows=(n-k)+1
    res=[]
    for i in range(windows):
        m=0
        for j in range(i,i+k):
            m=max(m,arr[j])
        res.append(m)
    return res

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence,n, window_size))

