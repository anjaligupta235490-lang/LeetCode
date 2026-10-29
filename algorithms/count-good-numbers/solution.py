class MyHashSet(object):

    def __init__(self):
        #self.data = [False]*1000001
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
        
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        #self.data[key] = True
        index = key% self.size
        if key not  in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """

       # self.data[key] = False
        index = key% self.size
        if key in self.buckets[index]:
            self.buckets[index].remove(key)
            
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        # return self.data[key]
        index = key% self.size
        return key in self.buckets[index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)