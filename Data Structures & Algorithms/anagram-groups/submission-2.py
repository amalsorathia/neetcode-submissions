class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #check if two words are anagrams of each other
        # first check if len is equal
        # if it is then iterate over a word and put each char in hashmap
        # if even one of the words added to hashmap is not in other word
        # return false
        # make a hashamp of random index to list of words where each random index
        # represents a list of words that are anagrams of each other
        charList = defaultdict(list)
        for word in strs:
            charWord = sorted(list(word))
            print(charWord)
            if tuple(charWord) not in charList.keys():
                charList[tuple(charWord)] = [word]
            else:
                charList[tuple(charWord)].append(word)
        return charList.values()
        