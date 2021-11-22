import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X=np.array([1,15,30,45,50,70,80,90,120])
y=np.array([2,10,90,110,130,160,150,200,220])

linreg=LinearRegression()

X=X.reshape(-1,1)

linreg.fit(X,y)
y_pred=linreg.predict(X)

plt.scatter(X,y)
plt.plot(X,y_pred,color='red')
plt.show()

print(linreg.coef_)
#1.9224471]

print(linreg.intercept_)
#12.09488938861017

# y=mx +c , so y=1.9x + 12.09
