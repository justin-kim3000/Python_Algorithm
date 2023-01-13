# package(패키지): 연관성이 있는 파일 모음
# module(모듈) : 연관성이 있는 함수들 모음

import aboutPython_calcu as cal

res = cal.plus(10,20)

print("덧샘 결과 : ",res)

from aboutPython_calcu import minus, mulit
print("뺄샘 결과:",minus(10,2))
print("뺄샘 결과:",mulit(10,2))

# 모든 모듈의 내용을 import 권장x
# from aboutPython_calcu import *

####################################
# 패키지
from mypackage import aboutPython_calcu

from mypackage import module1, module2
module2.show_mo_info()
module1.show_mo_info()