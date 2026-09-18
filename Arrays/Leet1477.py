class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)

        i=0
        j=0
        currsum = 0
        preSum =[float("inf")] * n
        bestMinLen= float("inf")
        result = float("inf")
        while (j<n):
            
            currsum += arr[j]
            while (i<j and currsum>target):
                currsum-=arr[i]
                i=i+1
               
            if (currsum==target):
                length = j-i+1
                #print(length)
                if i>0 and preSum[i-1]!=float("inf"):
                    result= min(result, length+preSum[i-1])
                
                bestMinLen=min(bestMinLen, length)
            
            preSum[j]=bestMinLen
            j=j+1
        
        if result == float("inf"):
            return -1

        
        return result