class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        answer = 0
        
        arr = self.divide(0, len(instructions), instructions)
        
        for i in range(len(arr)):
            answer += min(arr[i][1][0], arr[i][1][1])

        return answer % (10**9 + 7)
    
    def divide(self,l, r, arr):
        if l + 1 == r:
            return [[arr[l], (0, 0)]]
        
        mid = l + ( r -l)//2
        left = self.divide(l, mid, arr)
        right = self.divide(mid, r, arr)
        return self.conquer(left, right)
    
    def conquer(self, left, right):
        p1, p2 = 0, 0
        l, m, r = 0, 0, 0
        len_left = len(left)
        len_right = len(right)
        merge = []
        while p1 < len_left and p2 < len_right:
            if left[p1][0] < right[p2][0]:
                merge.append(left[p1])
                l += 1
                p1 += 1
            elif left[p1][0] == right[p2][0]:
                merge.append(left[p1])
                m += 1
                p1 += 1
            else:
        
                r = len_left - p1
                right[p2][1]= (l + right[p2][1][0], r + right[p2][1][1])
                merge.append(right[p2])
                p2 += 1
                if p1 - 1 >= 0 and p2 < len_right and right[p2][0] != left[p1 - 1][0]:
                    l += m
                    m = 0
        
        while p2 < len_right:
            if p1 - 1 >= 0 and right[p2][0] != left[p1 - 1][0]:
                l += m
                m = 0
        
            right[p2][1] = (l + right[p2][1][0], right[p2][1][1])
            merge.append(right[p2])
            p2 += 1
        merge.extend(left[p1:])
        merge.extend(right[p2:])
      

                
        return merge
    
