class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        result = sorted(points, key = lambda x: x[0]**2 + x[1]**2)
        return result[:k]
#         for i in range(len(points)):
        
#             answer=pow(points[i][0], 2) + pow(points[i][1], 2)
#             distance.append(answer)
        
#         for i in range(len(points)):
#             for j in range(i+1, len(points)):
#                 if distance[i] > distance[j]:
#                     distance[i], distance[j] = distance[j], distance[i]
#                     points[i], points[j] = points[j], points[i]
            
            
#             print(answer)
#             if arranged and answer
#             a = str(points[i])
#             dictionary[a]=answer
#             print(dictionary)
#         temp = list(dictionary)    
#         for key, value in dictionary.items():
#             if dictionary[key] > dictionary[temp[temp.index(test_key) + 1]]:
                
#         arranged = sorted(dictionary.values())
        
        
            
    
        
