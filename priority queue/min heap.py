def heapify(arr,n,i):
    swaps=[]
    smallest=i
    l=2*i+(1)
    r=2*i+(2)

    if l<n and arr[l]<arr[smallest]:
        smallest=l
    if r<n  and arr[r]<arr[smallest]:
        smallest=r
    
    if smallest!=i:
        swaps.append(i)
        arr[i],arr[smallest]=arr[smallest],arr[i]
        heapify(arr,n,smallest)
        print(arr)
arr=[5,4,3,2,1]
n=len(arr)
def heapsort(arr,n):
    #build max heap
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)  
heapsort(arr,n)

# print(len(values))
# for i, j in values:
#         print(i, j) 

print(arr)