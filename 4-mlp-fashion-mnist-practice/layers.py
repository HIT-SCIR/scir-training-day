import numpy as np
from activation import relu, softmax


class FullyConnected:
    def __init__(self, dim_in, dim_out, batch_size, activation):
        # initialization according to He et al.(2015)
        self.W = np.random.randn(dim_in, dim_out).astype(np.float32) \
                 * np.sqrt(2.0/(dim_in))
        self.b = np.zeros([dim_out]).astype(np.float32)
        self.batch_size = batch_size
        self.activation = activation
        self.v_b = np.zeros([dim_out])
        self.v_W = np.zeros([dim_in, dim_out])

    def forward(self, inputs):
        self.inputs = inputs
        outputs = np.dot(inputs, self.W) + self.b
        self.outputs = outputs
        outputs = self.activation.forward(outputs)
        self.outputs_act = outputs
        return outputs

    def backward(self, grad):
        activ_grad = self.activation.backward(self.outputs,
                                              self.outputs_act, grad)
        self.grad_b = np.mean(activ_grad, axis=0)
        self.grad_W = np.dot(self.inputs.transpose(),
                             activ_grad) / len(self.inputs)
        grad_inputs = np.dot(activ_grad, self.W.transpose())
        return grad_inputs

    def update(self, lr, momentum):
        self.v_b = momentum * self.v_b + lr * self.grad_b
        self.v_W = momentum * self.v_W + lr * self.grad_W
        self.W = self.W - self.v_W
        self.b = self.b - self.v_b
