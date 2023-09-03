# Import the random module
import random
import math

# Define the sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + math.exp(-x))  # Using e as an approximation

def sigmoid_derivative(x):
    return x * (1 - x)

# Define the neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights with random values
        self.weights_input_hidden = []
        for _ in range(input_size):
            self.weights_input_hidden.append([2 * (0.5 - random.random()) for _ in range(hidden_size)])
        
        self.weights_hidden_output = []
        for _ in range(hidden_size):
            self.weights_hidden_output.append([2 * (0.5 - random.random()) for _ in range(output_size)])
        
        # Initialize biases with zeros
        self.bias_hidden = [0] * hidden_size
        self.bias_output = [0] * output_size

    def forward(self, inputs):
        # Perform forward propagation
        self.hidden_layer_input = [0] * len(self.weights_input_hidden[0])
        self.hidden_layer_output = [0] * len(self.weights_input_hidden[0])
        self.output_layer_input = [0] * len(self.weights_hidden_output[0])
        self.output_layer_output = [0] * len(self.weights_hidden_output[0])

        for j in range(len(self.weights_input_hidden[0])):
            for i in range(len(inputs)):
                self.hidden_layer_input[j] += inputs[i] * self.weights_input_hidden[i][j]
            self.hidden_layer_output[j] = sigmoid(self.hidden_layer_input[j])

        for j in range(len(self.weights_hidden_output[0])):
            for i in range(len(self.hidden_layer_output)):
                self.output_layer_input[j] += self.hidden_layer_output[i] * self.weights_hidden_output[i][j]
            self.output_layer_output[j] = sigmoid(self.output_layer_input[j])

        return self.output_layer_output

    def backward(self, inputs, targets, learning_rate):
        # Perform backward propagation and update weights
        output_error = [targets[i] - self.output_layer_output[i] for i in range(len(targets))]
        output_delta = [output_error[i] * sigmoid_derivative(self.output_layer_output[i]) for i in range(len(output_error))]

        hidden_layer_error = [0] * len(self.hidden_layer_output)
        hidden_layer_delta = [0] * len(self.hidden_layer_output)

        for j in range(len(self.weights_hidden_output[0])):
            for i in range(len(self.hidden_layer_output)):
                hidden_layer_error[i] += output_delta[j] * self.weights_hidden_output[i][j]
                hidden_layer_delta[i] = hidden_layer_error[i] * sigmoid_derivative(self.hidden_layer_output[i])

        for i in range(len(inputs)):
            for j in range(len(self.hidden_layer_output)):
                self.weights_input_hidden[i][j] += inputs[i] * hidden_layer_delta[j] * learning_rate

        for i in range(len(self.hidden_layer_output)):
            for j in range(len(self.weights_hidden_output[0])):
                self.weights_hidden_output[i][j] += self.hidden_layer_output[i] * output_delta[j] * learning_rate

    def train(self, training_data, targets, epochs, learning_rate):
        for epoch in range(epochs):
            for i, inputs in enumerate(training_data):
                targets_single = targets[i]
                self.forward(inputs)
                self.backward(inputs, targets_single, learning_rate)

    def predict(self, inputs):
        return self.forward(inputs)

# Define the XOR problem dataset
training_data = [[0, 0], [0, 1], [1, 0], [1, 1]]
targets = [[0], [1], [1], [0]]

# Create and train the neural network
input_size = 2
hidden_size = 4
output_size = 1
learning_rate = 0.1
epochs = 10000

# Set a seed for reproducibility
random.seed(42)

nn = NeuralNetwork(input_size, hidden_size, output_size)
nn.train(training_data, targets, epochs, learning_rate)

# Test the trained neural network
for inputs in training_data:
    prediction = nn.predict(inputs)
    print(f"Input: {inputs}, Predicted Output: {prediction[0]}")
