import heapq

numbers = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]

heap = []
# heapq.heapify(heap)을 안해도 
# 연산 가능 
for number in numbers :
    if number != 0:
        heapq.heappush(heap, number)
    else:
        if len(heap):
            #이게 정수이면 
            #반대는 if not len(heap) 이런식으로 표현 가능
            print(0)
        else:
            print(heapq.heappop(heap)) 
        # 없는 경우

# print(numbers)
# [0, 0, 0, 0, 2, 12345678, 0, 1, 32]

#