'''line sorting'''
def lines(vare):
    '''lines'''
    list1 = []
    def length(var):
        '''length'''
        return len(var)
    for _ in range(vare):
        list1.append(input())
    list1.sort(key=length)
    for i in list1:
        print(i)
lines(int(input()))
