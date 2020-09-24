class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^a-z]', ' ', paragraph.lower())
        words = [word for word in paragraph.split() if not word in banned]
        
        return Counter(words).most_common(1)[0][0]

    def mostCommonWord2(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^a-z]', ' ', paragraph.lower())
        paragraph = paragraph.split()
        
        for word in banned:
            while word in paragraph:
                paragraph.remove(word)
        
        return Counter(paragraph).most_common(1)[0][0]