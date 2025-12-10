import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])

y = np.array([2, 4, 6, 8, 10])

modelo = LinearRegression()

print("Entrenando el cerebro......")
modelo.fit(X, y)

prediccion = modelo.predict([[20]])
print(f"Si la entrada es 20, la prediccion es: {prediccion[0]}")