class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        agmap=defaultdict(list)
        for i in strs:
            x="".join(sorted(i))
            agmap[x].append(i)
        return list(agmap.values())