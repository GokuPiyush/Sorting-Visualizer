import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import math

n = 100
a = [x+1 for x in range(n)]
random.shuffle(a)

def selection_sort(a):
	for i in range(len(a)):
		min_value, min_index = a[i], i
		for j in range(i+1, len(a)):
			if min_value > a[j]:
				min_value, min_index = a[j], j
		a[i], a[min_index] = a[min_index], a[i]
		yield a

def bubble_sort(a):
	for i in range(len(a)-1):
		for j in range(len(a)-i-1):
			if a[j]>a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				yield a

def insertion_sort(a):
	for i in range(1, len(a)):
		j, key = i-1, a[i]
		while j>=0 and key<a[j]:
			a[j+1] = a[j]
			yield
			j -= 1
		a[j+1] = key
		yield a

def merge_sort(a, l=0, r=n-1):
	if l>=r:
		return

	m = (l+r)//2
	yield from merge_sort(a, l, m)
	yield from merge_sort(a, m+1, r)

	li, i, j = [], l, m+1
	while i<=m and j<=r:
		if a[i]<a[j]:
			li.append(a[i])
			i += 1
		else:
			li.append(a[j])
			j += 1
	while i<=m:
		li.append(a[i])
		i += 1
	while j<=r:
		li.append(a[j])
		j += 1
	
	count = l
	for it in li:
		a[count] = it
		count += 1
		yield a

def quick_sort(a, l=0, r=n-1):
	if l>=r:
		return
	
	p, i, j = l, l+1, r
	while(i<=j):
		while(i<=r and a[p] > a[i]):
			i += 1
		while(j>=l and a[p] < a[j]):
			j -= 1
		if i<j:
			a[i], a[j] = a[j], a[i]
			yield a
	a[p], a[j] = a[j], a[p]
	yield a
	p = j

	yield from quick_sort(a, l, p-1)
	yield from quick_sort(a, p+1, r)


dispatch = {'s': 'selection_sort(a)', 'b': 'bubble_sort(a)', 'i': 'insertion_sort(a)', 'm': 'merge_sort(a)', 'q': 'quick_sort(a)'}
while(True):
	ch = input("Enter the initial character of sorting algorithm to be visualized: ")
	try:
		gen = eval(dispatch[ch])
		fig, ax = plt.subplots()
		rects = ax.bar([x+1 for x in range(n)], a)

		def animate(gen, a, rects):
			for rect,val in zip(rects, a):
				rect.set_height(val)
		ani = FuncAnimation(fig, func=animate, fargs=(a,rects), frames=gen, interval=1, repeat=False)
		plt.show()
		random.shuffle(a)
	except:
		if ch == 'exit':
			print('OK! See you soon..')
			break
		print('Bad parameters..')