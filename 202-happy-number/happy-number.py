class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=set()
        while(n>1):
            if n in seen:
                return False
            seen.add(n)
            len1=len(str(n))
            a=[]
            while(len1>0):
                d=10**(len1-1)
                a.append(n//d)
                n=n%d
                len1=len1-1
            sum=0
            for i in a:
                sum=sum+i**2
            n=sum
        if n == 1:
            return True
