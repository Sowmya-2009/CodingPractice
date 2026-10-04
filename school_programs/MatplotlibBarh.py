import matplotlib.pyplot as plt
import numpy as np
objects=('python','c++','java','perl','scala','lisp')
y_pos=np.arange(len(objects))
performance=[10,8,6,4,2,1]
plt.barh(y_pos , performance, color='r')
plt.xlabel('usage')
plt.title('programming language')
plt.show()