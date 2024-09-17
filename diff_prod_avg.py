'''
    CS 5001
    Lab 1
    Exercise 3
    Name: Yike Li
'''

'''
Replace the # YOUR CODE HERE markers below with
code that will calculate the correct values for
difference, product, and average. Complete the
print statements to output correctly formatted  
results.

Note: the code below is not syntactically correct and will not run until
you replace the # YOUR CODE HERE with the correct solution.
'''


def main():
    x = 5
    y = 10

    # Assign values to the variables below to calculate the difference, product, and average of the values in x and y.
    difference = x - y
    product = x * y
    average = (x + y) / 2

    str_difference = "The difference between x and y is " + str(difference) + "."
    str_product = "The product of x and y is " + str(product) + "."
    str_average = "The average of x and y is " + str(average) + "."
    print (str_difference)
    print (str_product)
    print (str_average)

if __name__ == '__main__':
    main()

