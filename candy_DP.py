class Solution(object):
    def candy(self, ratings):
        
        if len(ratings) < 1:
            return 1
        
        size = len(ratings)
            
        g_l = [0] * size
        g_r = [0] * size
        
        for i in range(1, size):
            if ratings[i] > ratings[i-1]:
                g_l[i] = g_l[i - 1] + 1
                
                
        for i in range(size - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                g_r[i] = g_r[i + 1] + 1
                
        res = 0
        
        for i in range(0, size):
            #print(str(i) + " : " + str(g_l[i]) + ' ' + str(g_r[i])) 
            res += max(g_l[i], g_r[i]) + 1
            
        return res
            
                
           
        
