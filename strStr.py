class Solution(object):
    def strStr(self, haystack, needle):
        l = len(needle)
        if l == 0:
            return 0
            
        prefix = [0] * l
        for i in range(1, l):
            j = prefix[i - 1]
            while j > 0 and needle[i] != needle[j]:
                j = prefix[j - 1]
            if needle[i] == needle[j]:
                j += 1
            prefix[i] = j
        
        hl = len(haystack)
            
        m = 0 #index of match in haystack
        i = 0 #current index in needle
        
        while m + i < hl:
            #print m,i
            if haystack[m + i] == needle[i]:
                i += 1
                if i == l:
                    return m
            else:
                if i > 0:
                    m += (i - prefix[i - 1])
                    i = prefix[i - 1]
                else :
                    i = 0
                    m += 1
                    
        return -1
