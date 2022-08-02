import heapq
num = [5, 3, 2, 4, 1]
heapq.heapify[num]
# print(num) > none 
# why? heap is destructive code
# 원본을 훼손해서 없음 

heapq.heappop(num)
# 최소값 빼면 알아서 2가 맨 앞으로 온다. 
heapq.heappush(num, 10) #걍 알아서 맨뒤에 들어감
heapq.heappush(num, 0) #자동으로 맨 앞에 들어감 
# 트리모양으로 갈라지는 중구난방인데 그 안에서 나름 규치있음 
#랜덤아님 
