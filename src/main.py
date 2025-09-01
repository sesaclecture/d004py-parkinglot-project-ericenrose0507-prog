import numpy as np
import datetime
from parkmodule import *


# 입차기능

while True:

    #입차
    car_number = input("[입차]차량번호를 입력해주세요")
    if car_number == 'q' :
        break
    incar(car_number)


    #출차
    out_number = input('[출차]차량번호를 입력해주세요')
    if out_number == 'q':
        break
    outcar(out_number)

    #종료
    O = input("프로그램을 종료하고싶다면 'q'를 입력해주세요")
    if O == 'q':
        break