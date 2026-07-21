from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict(zip( "abcdefghijklmnopqrstuvwxyz",
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]))

        res = []
        hashmap = {}

        for s in strs:
            length = len(s)
            temp = 1
            for i in range(length):
                temp *= map[s[i]]
            if not temp in hashmap:
                hashmap[temp] = []
            hashmap[temp].append(s)
        return list(hashmap.values())

    """
    map = dict(zip(
    'abcdefghijklmnopqrstuvwxyz',
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
))
        resmap = {}
        reslist = []
        for str in strs:
            m = 1
            for i in range(len(str)):
                m *= map[str[i]]
            if not m in resmap:
                resmap[m] = []
            resmap[m].append(str)
        # print(resmap.values())
        return [j for j in resmap.values()]
    """
