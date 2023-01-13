# # 클래스 - 객체지향 프로그래밍
# class Car1:
#     def carInfoShow(self):
#         print('회사:', "현대")
#         print('모델:', "그랜저")
#         print('색상:', "회색")
#         print('가격:', "4천만원")
        
# if __name__ == "__main__":
#         ca = Car1()
#         ca.carInfoShow()
        
# class Car2:
#     def __init__(self): # 생성자 역할
#          self.company = '현대'  # public 인스턴스 변수선언
#          self.model = '그랜저'
#          self.color = '흰색'
#          self.price = '4천만원'

# if __name__ == "__main__":
#         ca = Car2()
#         print("회사: ",ca.company)
#         print("모델: ",ca.model)


# # private를 캡슐화를 사용해서 나타냄
# class Car3:
#     def __init__(self):
#         self.__company = '현대' # private
#         self.__model = '그랜저'
#         self.__color = '흰색'
#         self.__price = '4천만원'

#     def carInfoShow(self):
#         print('회사:', self.__company)
#         print('모델:', self.__model)
#         print('색상:', self.__color)
#         print('가격:', self.__price)
        
        
# if __name__ == "__main__":
#     ca = Car3()
#     ca.carInfoShow()


# # 매개변수를 가지는 클래스
# class Car4:
#     def __init__(self,com,mod,col,pri):
#         self.__company = com
#         self.__model = mod
#         self.__color = col
#         self.__price = pri

#     def carInfoShow(self):
#         print('회사:', self.__company)
#         print('모델:', self.__model)
#         print('색상:', self.__color)
#         print('가격:', self.__price)
        
        
# if __name__ == "__main__":
#     ca = Car4("d","ds","asd","dd")
#     ca.carInfoShow()
    
# default 값 추가
class Car_ex:
    def __init__(self,com="a",mod="b",col="c",pri="d"):
        self.__company = com
        self.__model = mod
        self.__color = col
        self.__price = pri

    def carInfoShow(self):
        print('회사:', self.__company)
        print('모델:', self.__model)
        print('색상:', self.__color)
        print('가격:', self.__price)
        
    def setModel(self, model):
        self.__model  =  model
    
    def getModel(self):
        return self.__model
        
if __name__ == "__main__":
    ca = Car_ex("d","ds","asd","dd")
    ca.carInfoShow()
    
    
    
# class MyCount:
#     count = 0
#     def __init__(self) -> None:
#         self.__count = 0
#         self.__count += 1
#         print('instance 변수 : ',self.__count)
        
#     @classmethod
#     def print_count(cls):
#         cls.count += 1
#         print('class 변수 : ', cls.count)

# if __name__ == '__main__':
#     for i in range(5):
#         MyCount()
#         MyCount.print_count()
        
        
# class Car6:
#     def __init__(self,com="a",mod="b",col="c",pri="d"):
#         self.__company = com
#         self.__model = mod
#         self.__color = col
#         self.__price = pri
        

#     def carInfoShow(self):
#         print('회사:', self.__company)
#         print('모델:', self.__model)
#         print('색상:', self.__color)
#         print('가격:', self.__price)
        
#     def setModel(self, model):
#         self.__model  =  model
    
#     def getModel(self):
#         return self.__model


# # class 상속
# class Truck(Car6):
#     def __init__(self, com="a", mod="b", col="c", pri="d", ton='to'):
#         super().__init__(com, mod, col, pri)
#         self.__ton = ton
        
#     def showCarInfo(self):
#         super().carInfoShow()
#         print("최대적재량: ", self.__ton)
        
# class Suv(Car6):
#     def __init__(self, com="a", mod="b", col="c", pri="d", engine='to'):
#         super().__init__(com, mod, col, pri)
#         self.__engine = engine
        
#     # 재정의 (오버라이딩) : overriding
#     def showCarInfo(self):
#         super().carInfoShow()
#         print("엔진: ", self.__engine)
        
        
# if __name__ == '__main__':
#     tr = Truck('현대','2.5트럭','파랑','4천만원','2.5톤')
#     tr.showCarInfo()

#     su = Suv('현대','투싼','블랙','2천만원','디젤')
#     su.showCarInfo()
    
# 추상클래스 - 설계도면 역할
# 주의:abstractmethod 는 반드시 오버라이딩 해야됨
from abc import *
class Person(metaclass=ABCMeta):
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def work(self):
        pass
    
class Student(Person):
    def speak(self):
        print("질문하다")
    def work(self):
        print("공부하다")
        
class Teacher(Person):
    def speak(self):
        print("설명하다")
    def work(self):
        print("강의하다")
        
if __name__ == "__main__":
    obj = [Student(),Teacher()]
    for n in obj:
        n.speak();n.work()