import numpy as np
from sklearn.linear_model import LinearRegression


X = np.array([[1], [2], [3], [4]])

y = np.array([100, 150, 200, 250])

model = LinearRegression()

model.fit(X, y)

num_cuartos = input("Ingresa numero dee cuartos para saber que valor va a tener la casa: ")

prediccion = model.predict([[int(num_cuartos)]])
print(f"El valor de una casa con {num_cuartos} cuartos es de: {prediccion[0]}")