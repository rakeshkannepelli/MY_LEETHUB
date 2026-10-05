class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum=0
        for word in sentences:
            words=len(word.split())

            maximum=max(words, maximum)
        return maximum

            
        