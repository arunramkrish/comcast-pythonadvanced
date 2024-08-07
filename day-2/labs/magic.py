class MyList:
    def __init__(self):
        self.items = {}

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        if key == 'id':
            raise Exception("id cant be deleted")
        del self.items[key]

my_list = MyList()
my_list['id'] = 1234
my_list['a'] = 1
print(my_list['a'])  # Output: 1
del my_list['a']
del my_list['id']
