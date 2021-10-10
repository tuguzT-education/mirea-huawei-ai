class LinReg(object):
    """
    :param theta: list (len + 1)
    """

    def __init__(self, theta):
        self.theta = list(theta)
        self.x = None

    def compute(self, x):
        """
        :param x: list (len)
        :return: sum(theta[i] * x[i]) + theta[len]
        """
        self.x = list(x)
        result = 0
        for i in range(len(self.theta) - 1):
            result += self.x[i] * self.theta[i]
        return result + self.theta[len(self.theta) - 1]

    def passed(self) -> list:
        """
        Возвращает последнее переданное X
        :return: x_last
        """
        return self.x
