import requests
import random
import numpy as np
from linreg import LinReg

if __name__ == '__main__':
    # ids = [random.randint(10000000, 99999999) for i in range(100)]
    # salaries = []
    # for id in ids:
    #     dict_manager = requests.get(url=f"https://api.hh.ru/vacancies/{id}").json()
    #     if "salary" in dict_manager:
    #         salary = dict_manager["salary"]
    #         if salary is not None:
    #             salaries.append(salary)
    #             print(salary)
    np.random.seed(123)
    X_rand = np.random.randn(3 * 15).reshape((15, 3))
    Y = X_rand[:, 2].reshape((1, 15))
    X = np.ones((15, 3))
    X[:, :2] = X_rand[:, :2]
    theta = np.linalg.pinv(X.T @ X) @ X.T @ Y.T

    linreg = LinReg(theta[:, 0])
    for i, x in enumerate(X):
        print(linreg.compute(X[i]), (X @ theta)[i][0])
        assert round(linreg.compute(X[i]), 5) == round((X @ theta)[i][0], 5)
