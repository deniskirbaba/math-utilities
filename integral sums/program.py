from math import sin, cos, e, pi
from matplotlib import pyplot
import time
import numpy

colorsArray = ['r', 'b', 'y', 'b', 'g'] # is necessary for coloring various representations of integral sums

def UserInput():

	function = input("Enter function (available: x, 3**x, sinx, cosx, x**2, e**x, 2**x, x**3, e**-x, 4**-x, cospix, sinpix): ")
	a, b = input("Enter integration boundaries (2 numbers separated by a space): ").split()
	a, b = float(a), float(b)
	n = int(input("Enter number of split points: "))
	choosingMethods = input("Enter point choosing methods. You can select several options at the same time, separate the input with spaces (left, right, middle, inf, sup): ").split()

	return function, a, b, n, choosingMethods

def ApplyFunction(function, argument):

	if function == "sinx":
		return sin(argument)

	elif function == 'x':
		return argument

	elif function == "3**x":
		return 3 ** argument

	elif function == "2**x":
		return 2 ** argument

	elif function == "cosx":
		return cos(argument)

	elif function == "x**2":
		return argument ** 2

	elif function == "x**3":
		return argument ** 3

	elif function == "e**x":
		return e ** argument

	elif function == "e**-x":
		return e ** (-argument)

	elif function == "4**-x":
		return 4 ** (-argument)

	elif function == "cospix":
		return cos(pi * argument)

	elif function == "sinpix":
		return sin(pi * argument)

def ChoosePoint(choosingMethod, a, b, function):

	if choosingMethod == "left":
		return a

	elif choosingMethod == "right":
		return b

	elif choosingMethod == "middle":
		return (b + a) / 2

	elif choosingMethod == "inf":
		return InfSup(a, b, function, True)

	elif choosingMethod == "sup":
		return InfSup(a, b, function, False)

def InfSup(a, b, function, infFlag):

	n = 5
	dx = (b - a) / (n + 1)

	resultArgument = a
	resultValue = ApplyFunction(function, a)

	for i in range(n):
		argument = a + (i + 1) * dx
		value = ApplyFunction(function, argument)
		if (value < resultValue) == infFlag:
			resultArgument = argument
			resultValue = value

	return resultArgument

def IntegralSumCalculation(function, a, b, n, choosingMethods):

	start_time = time.time()

	numberOfChoosingMethods = len(choosingMethods)
	integralSum = [0]*numberOfChoosingMethods

	dx = (b - a) / (n + 1)
	yPrev = [0]*numberOfChoosingMethods

	for i in range(n + 1):

		print("Calculation of the %d-th term." % (i + 1))

		for j in range(numberOfChoosingMethods):

			xValue = ChoosePoint(choosingMethods[j], a + dx * i, a + dx * (i + 1), function)
			yValue = ApplyFunction(function, xValue)
			integralSum[j] += yValue * dx

			# plotting integral sum
			if i != 0:
				pyplot.plot([a + dx * i, a + dx * i], [yPrev[j], yValue], colorsArray[j])
			else:
				pyplot.plot([a, a], [ApplyFunction(function, a), yValue], colorsArray[j])

			pyplot.plot([a + dx * i, a + dx * (i + 1)], [yValue, yValue], colorsArray[j])

			yPrev[j] = yValue

	print("Time of calculating the integral sums: %s seconds." % (time.time() - start_time))

	for i in range(numberOfChoosingMethods):
		print("Integral sum (%s):" % choosingMethods[i], integralSum[i])

def Plot(a, b, n, function):


	# plotting real function graph
	xValues = numpy.linspace(a, b, n * 10)
	yValues = []
	for i in xValues:
		yValues.append(ApplyFunction(function, i))

	pyplot.plot(xValues, yValues, 'm')

	pyplot.xlabel("oX")
	pyplot.ylabel("oY")
	pyplot.show()

def main():

	function, a, b, n, choosingMethods = UserInput()
	IntegralSumCalculation(function, a, b, n, choosingMethods)
	Plot(a, b, n, function)

if __name__ == "__main__":
	main()