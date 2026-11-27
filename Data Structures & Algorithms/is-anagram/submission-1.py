class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    

        alph = "abcdefghijklmnopqrstuvwxyz"
            
        cnt_1: [str, dict] = {}
        cnt_2: [str, dict] = {}



        for ch in s:
            cnt_1[ch] = cnt_1.get(ch, 0) + 1
            
        for ch in t:
            cnt_2[ch] = cnt_2.get(ch, 0) + 1

        print(sorted(cnt_1), sorted(cnt_2))
        print(cnt_1, cnt_2)
        print(cnt_1 == cnt_2)

        return cnt_1 == cnt_2