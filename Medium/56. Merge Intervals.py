class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:

        arr.sort()

        ans = [arr[0]]
        for i in range(1, len(arr)):

        
            if arr[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], arr[i][1])
            else:
                ans.append(arr[i])

        return ans
        