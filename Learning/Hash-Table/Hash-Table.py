class HashTable:
    
    def __init__(self):
        self.max = 10
        self.arr = [[] for _ in range(self.max)]
    
    def getHash(self, key):
        sum = 0
        for i in range(len(key)):
            sum += ord(key[i])
        return sum % self.max

    def __setitem__(self, key, value):
        hash = self.getHash(key)
        
        found = False
        for i, pair in enumerate(self.arr[hash]):
            if len(pair) == 2 and pair[0] == key:
                self.arr[hash][i] = (key, value)
                found = True
                break
        
        if not found:
            self.arr[hash].append((key, value))
    
    def __getitem__(self, key):
        hash = self.getHash(key)
        for pair in self.arr[hash]:
            if len(pair) == 2 and pair[0] == key:
                return pair[1]

    def __delitem__(self, key):
        hash = self.getHash(key)
        for i, pair in enumerate(self.arr[hash]):
            if pair[0] == key:
                del self.arr[hash][i]
    

if __name__ == "__main__":
    
    dictionary = HashTable()
    
    dictionary["January/16/2023"] = 86500
    dictionary["January/16/2023"] = 100000
    dictionary["January/17/2023"] = 90000
    dictionary["January/17/2023"] = 80000
    dictionary["January/18/1023"] = 50000

    print(dictionary.arr)
    print(dictionary["January/16/2023"])
    print(dictionary["January/17/2023"])
    print(dictionary["January/18/1023"])
    print(dictionary["Whatever"])
    
    del dictionary["January/18/1023"]
    print(dictionary["January/18/1023"])    # -> None
