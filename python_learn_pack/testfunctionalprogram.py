#this filel focus to map/reduce
from functools import reduce


#map

def mapfunc(x):
	return x*x


def testmap():

	print('start test map')
	l = [x for x in range(1,10)]
	print(l)

	mapl = map(mapfunc,l)
	print(list(mapl))


	print(list(map(str,[x for x in range(1,10)])))

#reduce

def add(x,y):
	return x+y

def collect_to_int(x,y):
	return x*10+y

def testreduce():
	print('start test reduce')
	l = [x for x in range(1,100)]
	print(reduce(add,l))

	l = [1,3,5,7,4]
	print(reduce(collect_to_int,l))








if __name__ == '__main__':
	testmap()
	testreduce()