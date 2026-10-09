class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            self.data.append([key, value])
        else:
            for i in range(len(self.data)):
                if self.data[i][0] == key:
                    self.data[i][1] = value

    def get(self, key: int) -> int:
        for i in range(len(self.data)):
                if self.data[i][0] == key:
                    return self.data[i][1]
        return -1

    def remove(self, key: int) -> None:
        if self.get(key) == -1: return
        for i in range(len(self.data)):
                if self.data[i][0] == key:
                    self.data.pop(i)
                    return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)