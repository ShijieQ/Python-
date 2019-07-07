# GetPatameter.py
# author: ShijieQ   email: ShijieQ@outlook.com
# created 2019-06-16T18:30:07.950Z+08:00

import math
import system

while True:
    n = input()
    n = int(n)
    b = []
    x_ = float()
    s_2 = float()
    for i in range(0, n):
        temp = input()
        temp = float(temp)
        b.append(temp)
        x_ += b[i]
    x_ /= n
    x_ = float(int(x_*1000))/1000
    for i in range(0, n):
        s_2 = (b[i] - x_)*(b[i] - x_)
    s_2 /= n - 1
    s_2 = float(int(s_2*10000000))/10000000
    s = math.sqrt(s_2)
    print("X_ = ", x_)
    print("x_2 = ", s_2)
    print("s = ", s)


# ((6.683 - 6.678)*(6.683 - 6.678) + (6.681 - 6.678)*(6.681 - 6.678) + (6.676 - 6.678)*(6.676 - 6.678) + (6.679 - 6.678)*(6.679 - 6.678) + (6.672 - 6.678)*(6.672 - 6.678))/5