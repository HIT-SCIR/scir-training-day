import numpy as np


class relu:
    def __init__(self):
        pass

    def forward(self, inputs):
        return inputs * (inputs > 0)

    def backward(self, inputs, outputs, fgrad):
        return (inputs > 0) * fgrad


class softmax:
    def __init__(self):
        pass

    def forward(self, inputs):
        e_x = np.exp(inputs - np.max(inputs, axis=1).reshape(len(inputs), -1))
        return e_x / e_x.sum(axis=1).reshape(len(e_x), -1)

    def backward(self, inputs, outputs, fgrad):
        grad = -np.array([np.sum(outputs * fgrad, axis=1)]).transpose() \
                                                        * outputs
        grad = grad + outputs * fgrad
        return grad
