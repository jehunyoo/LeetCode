class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for s in strs:
            anagrams[''.join(sorted(s))].append(s)
        
        return list(anagrams.values())


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        std = []
        
        for s in strs:
            ss = sorted(s)
            if ss in std:
                anagrams[std.index(ss)].append(s)
            else:
                std.append(ss)
                anagrams.append([s])
        return anagrams
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for word in strs:
            groups[frozenset(collections.Counter(word).most_common())].append(word)
        
        return list(groups.values)