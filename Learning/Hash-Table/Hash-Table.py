class HashTable:
    
    def __init__(self):
        self.max = 1000
        self.arr = [None for _ in range(self.max)]
    
    def getHash(self, key):
        sum = 0
        for i in range(len(key)):
            sum += ord(key[i])
        return sum % self.max

    def __setitem__(self, key, value):
        hash = self.getHash(key)
        self.arr[hash] = value
    
    def __getitem__(self, key):
        hash = self.getHash(key)
        return self.arr[hash]
    
    def __delitem__(self, key):
        hash = self.getHash(key)
        self.arr[hash] = None
    

if __name__ == "__main__":
    dictionary = HashTable()
    dictionary["January/16/2023"] = 86500
    print(dictionary["January/16/2023"])
    del dictionary["January/16/2023"]
    print(dictionary["January/16/2023"])
