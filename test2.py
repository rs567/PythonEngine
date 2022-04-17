
class apple:
    def orange(x,y,z):
        return x + y + z
        
if __name__ == '__main__':
    x,y,z = 1,1,1
    apple.orange(x,y,z)

import numpy as np

a = np.array([1,1,1])
b = np.array([1,1,1])

c =np.subtract(a,b)
print(a-b.T)