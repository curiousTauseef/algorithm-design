class RollingHash:
    def __init__(self, base, text, size):
        self.base = base
        self.text = text
        self.size = size
        self.hashedText = self.encode(text[:size])
        self.counter = 0
    def encode(self, text):
        return sum([ord(char)*self.base**i for i, char in enumerate(reversed(text))])
    def update(self):
        if self.size+self.counter<len(self.text):
            self.hashedText = self.base*(self.hashedText-ord(text[self.counter])*self.base**(self.size-1))+ord(self.text[self.size+self.counter])
            self.counter += 1
        return self.hashedText
    def getHashedText(self):
        return self.hashedText

def rabinkarp(text, pattern):
    size = len(pattern)
    rhash = RollingHash(101, text, size)
    hashedPattern = rhash.encode(pattern)
    for i in range(0, len(text)-size+1):
        if hashedPattern == rhash.getHashedText():
            if text[i:i+size] == pattern:
                return i
        rhash.update()
    return None

print(rabinkarp(text, pattern))

