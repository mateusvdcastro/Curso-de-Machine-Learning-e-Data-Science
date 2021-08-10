import numpy as np

# save activations and derivates
# implement backpropagation
# implement gradient descent
# implement train
# train our net with some dummy dataset
# make some predictions


class MLP:
    def __init__(self, num_inputs=3, num_hidden=[3, 5], num_outputs=2):
        # num_hidden=[3, 5] -> this mean that we have 2 hidden layers, the first
        # contain 3 neurons and the secound contain 5 neurons;
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs

        layers = [num_inputs] + num_hidden + [num_outputs]

        # initiate random weights
        weights = []
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i], layers[i+1])  # creating random arrays with 2 dimensions
            weights.append(w)
        self.weights = weights

        activations = []
        for i in range(len(layers)):
            a = np.zeros(layers[i])
            activations.append(a)
        self.activations = activations

        derivatives = []
        for i in range(len(layers)-1):
            d = np.zeros((layers[i], layers[i+1]))
            derivatives.append(d)
        self.derivatives = derivatives

    def forward_propagate(self, inputs):  # propagation left-to-right
        """
        Computes forward propagation of the network based on input signals.

        :arg inputs: (ndarray): Input signals
        :return: activations (ndarray): Output values
        """
        activations = inputs
        self.activations[0] = activations

        for i, w in enumerate(self.weights):
            # calculate net inputs
            net_inputs = np.dot(activations, w)  # dot() makes the dot product (produto escalar) entre matrizes ou vetores

            # calculate the activations
            activations = self._sigmoid(net_inputs)
            self.activations[i+1] = activations
            # Why activations[i+1]?
            # a_3 = sigmoid(h_3)
            # h_3 = a_3 * W_2

        return activations

    def back_propagate(self, error, verbose=False):
        # Note: error == (y - a[i+1])

        # dE/dW_i = (y - a[i+1])s'(h_[i+1]))a_i        y  is the real value and a the value predicted
        # s'(h_[i+1]) = s(h_[i+1])(1-s(h_[i+1]))
        # s (h_[i+1]) = a_[i+1]

        # dE/dW_[i-1] = (y - a[i+1])s'(h_[i+1]))W_i s'(h_i) a_[i-1]

        for i in reversed(range(len(self.derivatives))):
            activations = self.activations[i+1]
            delta = error*self._sigmoid_derivative(activations)  # delta = s(h_[i+1])(1-s(h_[i+1]))
            delta_reshaped = delta.reshape(delta.shape[0], -1).T  # ndarray([0.1, 0.2]) --> ndarray([[0.1, 0.2]]) and transpose .T
            current_activations = self.activations[i]  # ndarray([0.1, 0.2]) --> ndarray([0.1], [0.2])
            current_activations_reshaped = current_activations.reshape(current_activations.shape[0], -1)
            self.derivatives[i] = np.dot(current_activations_reshaped, delta_reshaped)
            error = np.dot(delta, self.weights[i].T)  # error == (y - a[i+1])s'(h_[i+1]))W_i
            if verbose:
                print(f"Derivatives for W{i}: {self.derivatives}")
        return error

    def _sigmoid_derivative(self, x):
        return x * (1.0 - x)

    def _sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))


if __name__ == "__main__":
    # create an MLP
    mlp = MLP(2, [5], 1)  # 2 inputs, one hidden layer with 5 neurons, 1 output

    # create dummy data
    inputs = np.array([0.1, 0.2])  # the neural network must sum inputs and arrive in target
    target = np.array([0.3])

    # forward propagation
    output = mlp.forward_propagate(inputs)

    # calculate error
    error = target - output

    # back propagation
    mlp.back_propagate(error, verbose=True)
