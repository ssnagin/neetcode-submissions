from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for str_ in strs:
            
            key = "".join(sorted(str_))
            
            groups[key].append(str_)

        return list(groups.values())