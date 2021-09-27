class Card:
    def __init__(self, kind: str, suite: str):
        self.kind = kind.lower
        self.suite = suite.lower()
        if int(self.kind) in range(1,10):
            self.val = int(self.kind)
        elif self.val in ["jack", "j", "queen", "q", "king", "k"]:
            self.val = 10
        elif self.kind in ["ace", "a"]:
            self.val = 1

    def getValue(self):
        return self.val  
    
    def __str__(self):
        return f"{self.val} of {self.suite}"

    def __repr__(self):
        return f"Card({self.val}, {self.suite}"
        
