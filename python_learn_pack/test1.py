#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable
import os

def returnfunc(str):
	return str

def floordiv(a,b):
	return a//b

def testlist():
	print('start test list')
	classmates = ['Michael', 'Bob', 'Tracy']
	print('classmates list lenght is',len(classmates))
	print('classmates[0]=',classmates[0])
	print('the last classmate is',classmates[-1])
	print('append admin to calssmate')
	classmates.append('admin')
	print(classmates)
	print('delete last element')
	classmates.pop()
	print(classmates)
	print('delete the second element')
	classmates.pop(1)
	print(classmates)
	print('replace second element with sarah')
	classmates[1] = 'sarah'
	print(classmates)

	print('\n======================\n')
	print('list can store diff type of element')
	l=['apple',12,True]
	print(l)

	print('list can sotre list')
	s = ['asp','python','c#',l]
	print(s)
	print('len(s) = ',len(s))
	print('len(s[3])=',len(s[3]))

def testtuple():
	print('start test tuple [it cant be modified]')
	classmates = ('Michael','Bob','Tracy')
	print(calssmates)

	print('remember if u want define a tuple that have only one element')
	print('the define is like this t=(1,) add a common to eliminate ambiguity')

def testdict():
	print('start test dict')
	dic = {'Michael':95,'Bob':75,'Tracy':89}
	print(dic)
	print(dic['Michael'])
	print('test print not exist item will conduct error')
	print('add a new item to dict')

	dic['ad'] =100
	print(dic)
	print(dic['ad'])


	print(('test' in dic))
	print(('Michael' in dic))

	print(dic.get('test',-1232))
	print(dic.get('Michael',-12))

	print(dic.pop('Michael'))


def testset():
	s=set([12,12,3,43,54,64,232,43,54,232,232,3,3,])
	print('start test set')
	print(s)

	s.add(13)
	s.add(12)
	print(s)

	s.remove(3)
	print(s)


def testfunctiontypecheck(a):
	if not isinstance(a,(int,float)):
		raise TypeError('bad operadn type')
	else:
		print('type check pass')

def testfuncreturnmultivalue(x,y):
	return y,x

def testslice():
	print('start test slice')
	s = ['michael','sarah','tracy','jack']
	print(s[0:3])
	print(s[2:4])

	l=list(range(100))
	print(l)
	print(l[:10])

def testiterate(val):
	return isinstance(val,Iterable)

def testlistgenerator():
	print('start test list generator')

	print([x*x for x in range(1,11)])

	print([x*x/2 for x in range(1,11) if x%2 == 0])

	print([a+b for a in 'abc' for b in 'def'])

	print([d for d in os.listdir('.')])

	s = {'a':100,'b':10,'c':132}

	print([('%s = %d'%(k,v)) for k,v in s.items()])

def generatordemo():#the generator like corutine 
	print('first step of generator')
	yield(1)
	print('second step of generator')
	yield(2)
	print('third step of generator')
	yield(3)

def triangles():
	layer_p = [1]
	layer_c = [1]
	layer_i = 1

	while True:
		yield layer_c
		layer_p = [x for x in layer_c]
		for i in range(0,len(layer_p)-1):
			layer_c[i+1] = layer_p[i]+layer_p[i+1]

		layer_c.append(1)


def testgnerator():
	g = (x*x for x in range(1,11))
	print(next(g))
	print(next(g))#the next func use few

	for dat in g:
		print(dat)

	o = generatordemo()
	print(next(o))
	print(next(o))

	tr = triangles()
	print(next(tr))
	print(next(tr))
	print(next(tr))
	print(next(tr))
	print(next(tr))
	print(next(tr))
	print(next(tr))
	print(next(tr))


def functional_add(x,y,f):
	return f(x)+f(y)

def testfunctional():

	print(functional_add(1,-2,abs))


if __name__ == '__main__':
	print('start learn python')

	print('test input func')
	print('please input a name')
	name = input()
	print('you name is \'%s\'' % name)

	print('start test string assignment')
	a = 'ABC'
	b = a
	a = 'XYZ'
	print('a =',a)
	print('b =',b)

	testlist() 

	testdict()

	testset()

	testfunctiontypecheck(True)
	#testfunctiontypecheck('a')
	testfunctiontypecheck(100)

	testslice()

	testlistgenerator()

	testgnerator()

	testfunctional()