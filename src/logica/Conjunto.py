class Conjunto:
    def __int__(self, conjunto):
        self.__conjunto = conjunto
    def promedio (self):
        if len(self.__conjunto)==1:
            return (self.__conjunto[0])
        else:
            return None
