from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        total_same = ""
        data =zip(*strs)
        for i in data:
            if len(set(i)) == 1:
                total_same += i[0]
            else:
                break
        return total_same
if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
    print(s.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
    print(s.longestCommonPrefix([""]))                         # Output: ""
    print(s.longestCommonPrefix(["a"]))                        # Output: "a"
    print(s.longestCommonPrefix(["ab", "a"]))                  # Output: "a"

