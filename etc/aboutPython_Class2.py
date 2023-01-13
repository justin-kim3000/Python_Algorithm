class MyCount:
    count = 0
    def __init__(self) -> None:
        self.__count = 0
        self.__count += 1
        print('instance 변수 : ',self.__count)
        
    @classmethod
    def print_count(cls):
        cls.count += 1
        print('class 변수 : ', cls.count)

if __name__ == '__main__':
    for i in range(5):
        MyCount()
        MyCount.print_count()