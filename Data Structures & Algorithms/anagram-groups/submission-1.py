class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charList = {}
        for i in range(0, len(strs)):
            word = ''.join(sorted(strs[i]))
            print("word", word)
            if word not in charList.keys():
                print(charList.keys())
                charList[word] = [strs[i]]
            else:
                charList[word].append(strs[i])
        return charList.values()
        