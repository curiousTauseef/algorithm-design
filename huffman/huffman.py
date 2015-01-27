from heapq import heappush, heappop, heapify
import collections
import struct

class Compression():
    def __init__(self, text):
        self.text = text
        self.frequencies = self.calculateFrequencies()
        self.mapping = self.generateMapping()

    def calculateFrequencies(self):
        frequencies = collections.Counter(self.text)
        return frequencies

    def generateMapping(self):
        heap = [[frequency, [char, ""]] for char, frequency in self.frequencies.items()]
        heapify(heap)
        while len(heap) > 1:
            low = heappop(heap)
            high = heappop(heap)
            for pair in low[1:]:
                pair[1] = '0' + pair[1]
            for pair in high[1:]:
                pair[1] = '1' + pair[1]
            heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
        mapping = dict(heappop(heap)[1:])
        return mapping
        
    def encode(self, text):
        encodedText = ''.join([self.mapping[char] for char in text])
        return encodedText

    def decode(self, encodedText):
        reversedMapping = self.reverse(self.mapping)
        translation = []
        i = 0
        substring = ""
        while (i < len(encodedText)):
            substring += encodedText[i]
            i += 1
            if (substring in reversedMapping.keys()):
                translation.append(reversedMapping[substring])
                substring = ""
        return "".join(translation)
 
    def reverse(self, mapping):
        reversedMapping = {v: k for k, v in mapping.items()}
        return reversedMapping

class UnigramCompression(Compression):
    pass

class BigramCompression(Compression):
    def calculateFrequencies(self):
        frequencies = collections.Counter(zip(self.text, self.text[1:]))
        return frequencies

    def encode(self, text):
        encodedText = ''.join([self.mapping[char1, char2] for char1, char2 in self.pairwise(text)])
        return encodedText

    def pairwise(self, iterable):
        iterator = iter(iterable)
        return zip(iterator, iterator)

    def decode(self, encodedText):
        reversedMapping = self.reverse(self.mapping)
        translation = []
        i = 0
        substring = ""
        while (i < len(encodedText)):
            substring += encodedText[i]
            i += 1
            if substring in reversedMapping.keys():
                translation.append("".join(reversedMapping[substring]))
                substring = ""
        return "".join(translation)

def getCompressionCoefficient(original, encoded):
    coefficient = len(original)*8/len(encoded)
    return coefficient




