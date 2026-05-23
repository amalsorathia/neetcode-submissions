class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #check if two words are anagrams of each other
        # sort each string 
        # add to hashmap as list if not present
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
        