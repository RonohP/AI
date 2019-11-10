import numpy
import random
import os

# learning rate
lr = 1

# value of bias
bias = 0

# weights generated in a list
# 3 weights ~ 2 neurons and 1 bias
weights = [random.random(), random.random(), random.random()]


def perceptron(input1, input2, output):
    # output_p is the output given by the perceptron
    output_p = input1 * weights[0] + input2 * weights[1] + bias * weights[2]

    # activation function takes back all the values to exactly 0 or 1
    if output_p > 0:
        pass
    else:
        output_p = 0
        error = output - output_p
        weights[0] += error * input1 * lr
        weights[1] += error * input2 * lr
        weights[2] += error * bias * lr


def main():
    # a loop for repeating every situation several times
    # learning stage
    for i in range(50):
        perceptron(1, 1, 1)  # True or true
        perceptron(1, 0, 1)  # True or false
        perceptron(0, 1, 1)  # False or true
        perceptron(0, 0, 0)  # False or false
        perceptron(3, 5, 9)  # False or false

    # enter values prompt
    print('Enter x: ')
    x = int(input())
    print('Enter y: ')
    y = int(input())
    output_p = x * weights[0] + y * weights[1] + bias * weights[2]

    # activation function
    # testing phase
    # if output_p > 0:
    #     output_p = 1
    # else:
    #     output_p = 0
    print('\n', x, ' or ', y, 'is : ', output_p)

    # output_p = 1/(1+numpy.exp(-output_p))   # sigmoid function


if __name__ == '__main__':
    main()
