class Card:
    def __init__(self, kind: str, suite: str):
        self.kind = kind
        self.suite = suite
    
        if self.kind in ["Jack", "Queen", "King"]:
            self.val = 10
        elif self.kind == "Ace":
            self.val = 11
        else:
            if int(self.kind) in range(1,10):
                self.val = int(self.kind)
    def val(self):
            return self.val
    
    def __str__(self):
        return f"{self.kind} of {self.suite}"

    def __repr__(self):
        return f"Card(\"{self.kind}\", \"{self.suite}\")"
        
