def bin(num):

    c=0

    while(num>1):
        if num%2==1:
            
            c+=1

            
        num//=2
    
    c+=1
    return c
def isPrime(num):
    if num**(0.5)%(int(num**0.5))==0:
        return False
    for i in range(2,int(num**(0.5)+1)):
        if num%i==0:
            return False
    return True


class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        c=0
        for num in range(left,right+1):
            if isPrime(bin(num)):
                c+=1
        return c