class MedianOfAStream():
    def __init__(self):
        self.arr = []
    
    def insert(self, number):
        return self.arr.append(number)
    
    def findMedian(self):
        self.arr.sort()
        n = len(self.arr)
        if n % 2 != 0:
            middle = int(round(n / 2) - 1)
            return self.arr[middle]
        else:
            middle = int(round(n/2))
            return (self.arr[middle]+ self.arr[middle-1]) / 2




if __name__ == "__main__":
    l = MedianOfAStream()
    l.insert(5)
    l.insert(3)
    l.insert(2)
    l.insert(1)
    print(l.findMedian())