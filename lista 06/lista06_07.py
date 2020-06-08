import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2*np.pi,2*np.pi,60)
plt.subplot(2,2,1)
plt.plot(x,np.sin(x),'red')
plt.title('função seno(x)')
plt.subplot(2,2,2)
plt.bar(x,np.cos(x))
plt.title('função cos(x)')
plt.subplot(2,2,3)
plt.scatter(x,np.tan(x))
plt.title('função tg(x)')
plt.ylabel('valor de tg(x)')
plt.xlabel('valor de x')
plt.show()
