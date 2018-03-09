class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = -1
        i = 0
        j = len(height)-1
        while(i<j):
            if((j-i)*min(height[i],height[j])>max):
                max = (j-i)*min(height[i],height[j])
            if(height[i]>height[j]):
                j = j-1
            else:
                i = i+1
        return max
    def min(self ,a ,b):
        if(a<b):
            return a
        else:
            return b
