class Solution:
    # binary search
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        content = 0
        for cookie in s:
            index = bisect.bisect_right(g, cookie)
            if index > content:
                content += 1
        
        return content

    # greedy algorithm
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        content = 0
        child, cookie = 0, 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                content += 1
                child += 1
            cookie += 1
        
        return content
    
    # greedy algorithm, slower
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_counter = collections.Counter(g)
        s_counter = collections.Counter(s)
        g_sort = sorted(g_counter.keys())
        s_sort = sorted(s_counter.keys())
        content = 0
        
        i, j = 0, 0
        while i < len(g_sort) and j < len(s_sort):
            greed = g_sort[i]
            size = s_sort[j]
            
            if size < greed:
                j += 1
            else:
                ng = g_counter[greed] # number of 'greed'
                ns = s_counter[size] # number of 'size'
                if ns > ng:
                    content += ng
                    g_counter[greed] -= ng
                    s_counter[size] -= ng
                    i += 1
                else:
                    content += ns
                    g_counter[greed] -= ns
                    s_counter[size] -= ns
                    j += 1
        
        return content