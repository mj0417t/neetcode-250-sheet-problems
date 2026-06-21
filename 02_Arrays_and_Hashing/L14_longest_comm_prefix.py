class TrieNode:
    def __init__(self):
        self.children = {}
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self, word: str)->None:
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
    def lcp(self, word:str, prefixLen:int)->int:
        node=self.root
        for i in range(min(len(word),prefixLen)):
            if word[i] not in node.children:
                return i
            node=node.children[word[i]]
        return min(len(word),prefixLen)




class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # lcp=strs[0]
        # for i in range(1,len(strs)):
        #     if lcp=='':
        #         return lcp
        #     for j in range(len(strs[i])):
        #         if lcp[j]!=strs[i][j]:
        #             lcp=lcp[:j]
        #             break
        # return lcp
        if len(strs)==1:
            return strs[0]
        mini=0
        for i in range(len(strs)):
            if len(strs[mini])>len(strs[i]):
                mini=i

        trie=Trie()
        trie.insert(strs[mini])

        prefixLen=len(strs[mini])

        for i in range(len(strs)):
            prefixLen=trie.lcp(strs[i],prefixLen)
        return strs[mini][:prefixLen]
        
if __name__=='__main__':
    s=Solution()
    strs=["car","cir"]
    print(s.longestCommonPrefix(strs))