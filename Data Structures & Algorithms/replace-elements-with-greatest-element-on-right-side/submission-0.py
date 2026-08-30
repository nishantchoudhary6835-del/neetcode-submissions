class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            greatest=arr[i+1]

            for j in range(i+1,len(arr)):
                if arr[j]>greatest:
                    greatest=arr[j]

            arr[i]=greatest
        arr[-1]=-1
        return arr        