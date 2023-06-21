class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        answer = []
        task = []
        for index in range(len(tasks)):
            enq, time = tasks[index]
            task.append((enq, time, index))
        heapq.heapify(task)
        # print(task)

        i = 0
        enqueTime = 0
        while task:
            if heap:
                time, index = heapq.heappop(heap)
                enqueTime += time

                # print(time, index, enqueTime, heap)
                answer.append(index)
                
           
            
            if task and not heap:
                enq, time, index = heapq.heappop(task)
                enqueTime = max(enqueTime, enq)
                heapq.heappush(heap, (time, index))
    
            while i < len(task) and task[0][0] <= enqueTime:
                enq, time, index = heapq.heappop(task)
                heapq.heappush(heap, (time, index))
                
            # print(heap)
            
                
               
        while heap:
            time, index = heapq.heappop(heap)
            answer.append(index)
        
        
        return answer
           
