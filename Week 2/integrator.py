import numpy as np

class Integrator:
    def __init__(self, xMin, xMax, N):
        self._integ = 0
        self._xMin = xMin
        self._xMax = xMax
        self._n = N
        
    def integrate(self):

        deltaX = (self._xMax - self._xMin) / self._n

        x = np.arange(self._xMin, self._xMax, deltaX)

        f = (np.power(x, 2)) * np.exp(-x) * np.sin(x)

        self._integ = sum(f*deltaX)
        
    def show(self):
        print(round((self._integ), 5))


examp = Integrator(1, 3, 200000)
examp.integrate()
examp.show()
