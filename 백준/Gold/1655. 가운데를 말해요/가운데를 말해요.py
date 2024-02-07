import heapq
import sys

min_heap = [] 
max_heap = []  

def add_number(num):
    """
    minheap을 이용해 maxheap 사용.
    maxheap이 minheap과 같거나 하나만 더 길게 설정하여 중앙값 계산
    그렇게 해서 홀 수개이거나 짝수 개든 maxheap출력하면 된다.
    """
    if not max_heap or num <= -max_heap[0]:
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    elif len(max_heap) > len(min_heap)+ 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    add_number(num)
    print(-max_heap[0])
