import numpy
import random
import os

# learning rate
lr = 1

# value of bias
bias = 0

# weights generated in a list
# 3 weights ~ 3 neurons and 1 bias
weights = [random.random(), random.random(), random.random(), random.random()]


def perceptron(input1, input2, input3, output):
    # output_p is the output given by the perceptron
    output_p = input1 * weights[0] + input2 * weights[1] + input3 * weights[2] + bias * weights[3]

    # activation function takes back all the values to exactly 0 or 1
    if output_p > 0:
        pass
    else:
        output_p = 0
        error = output - output_p
        weights[0] += error * input1 * lr
        weights[1] += error * input2 * lr
        weights[2] += error * input3 * lr
        weights[3] += error * bias * lr


def main():
    # a loop for repeating every situation several times
    # learning stage
    for i in range(50):
        perceptron(30, 40, 50, 20)  # Epoch1
        perceptron(40, 50, 20, 15)  # Epoch2
        perceptron(50, 20, 15, 60)  # Epoch3
        perceptron(20, 15, 60, 70)  # Epoch4
        perceptron(15, 60, 70, 50)  # Epoch5
        perceptron(60, 70, 50, 40)  # Epoch6

    # enter values prompt
    print('Enter x: ')
    x = int(input())
    print('Enter y: ')
    y = int(input())
    print('Enter z')
    z = int(input())
    output_p = x * weights[0] + y * weights[1] + z * weights[2] + bias * weights[3]

    # activation function
    # testing phase
    # if output_p > 0:
    #   output_p = 1
    # else:
    #   output_p = 0
    print('\n', x, ',', y, 'or', z, 'is : ', output_p)

    #


if __name__ == '__main__':
    main()
