

def heapify(arr,n,i):
    largest=i
    l=2*i+(1)
    r=2*i+(2)

    if l<n and arr[l]>arr[largest]:
        largest=l
    if r<n  and arr[r]>arr[largest]:
        largest=r
    
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def heapsort(arr,n):
    #build max heap
    result=[]
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)       #[50, 40, 19, 29, 30, 18]


    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]   #sabse bada sabse end me
        result.append(i)
        heapify(arr,i,0)
    print(result)
arr=[50,30,18,29,40,19]
heapsort(arr,len(arr))
print(arr)