# iterator concept in python

class reverse_iter:
    def __init__(self,list_to_reverse):
        self.list_to_reverse = list_to_reverse
        self.index_num = len(self.list_to_reverse)
    
    # iter magic function
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index_num > 0:
            self.index_num -= 1
            return self.list_to_reverse[self.index_num]
        else:
            raise StopIteration

list_to_reverse = [1,2,3,4,5,6,12]
values = reverse_iter(list_to_reverse)

for i in values:
    print(i)