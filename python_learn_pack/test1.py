#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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