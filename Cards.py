class Card:
    def __init__(self, kind: str, suite: str):
        self.kind = kind
        self.suite = suite
        try:
            if int(self.kind) in range(1,10):
                self.val = int(self.kind)
        except:
            if self.kind in ["Jack", "Queen", "King"]:
                self.val = 10
            elif self.kind == "Ace":
                self.val = 1
            else:
                raise ValueError
    
    def __str__(self):
        return f"{self.kind} of {self.suite}"

    def __repr__(self):
        return f"Card(\"{self.kind}\", \"{self.suite}\")"
        
