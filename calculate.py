import circle
import square
import triangle


figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	"""
	Вычисляет периметр или площадь заданной фигуры.

	Args:
	fig (str): название фигуры ("круг" или "квадрат" или "треугольник").
	func (str): функция для вычисления ("периметр" или "площадь").
	size (list):список размеров фигуры. 
				Для круга он содержит радиус.
				Для квадрата он содержит длину его стороны.
				Для треугольника он содержит длины трех его строн.

	Returns:
	Выводит результат на консоль.

	"""
	assert fig in figs 
	'''Недопустимое название фигуры'''
	assert func in funcs 
	'''Недопустимое название функции'''

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



