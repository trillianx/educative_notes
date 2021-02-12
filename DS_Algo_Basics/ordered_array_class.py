class OrderedArray():
    def __init__(self):
        self.list = []

    def getSize(self):
        return len(self.list)

    def insert_oa(self, data):
        self.list.append(data)
        self.list.sort()

    def search(self, data):
        for index, v in enumerate(self.list):
            print(v)
            if v == data:
                return index
            elif v > data:
                return False
        return False



    

if __name__ == "__main__":
    a = OrderedArray()

    a.insert_oa(2)
    a.insert_oa(3)
    a.insert_oa(1)
    a.insert_oa(4)
    a.insert_oa(-1)
    a.insert_oa(105)
    a.insert_oa(202)
    a.insert_oa(325)
    #print(a.list)
    #print(a.search(3))
    print(a.search(4))
