class status:
    def __init__(self, answer: str, word: str):
        self.isPresent=[]
        self.isCorrect=[]
        for i in range(len(answer)):
            if word[i] in answer:
                self.isPresent.append(True)
            else:
                self.isPresent.append(False)
            
            if word[i]==answer[i]:
                self.isCorrect.append(True)
            else:
                self.isCorrect.append(False)
