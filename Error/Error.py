class Error(object):
    def printLine(self, num = 1):
        if(num == 0):
            num = 1
        for i in range(num):
            print('-------------------------------------------')
