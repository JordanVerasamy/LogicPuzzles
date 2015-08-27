from random import randint

def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b

fib_list = list(fib(30))

list_of_shots = []

x = 1
while x < 30:
	for i in range(x, 0, -1):
		# print "{}+f({})".format(x, i)
		# print "{}-f({})".format(x, i)
		# print "-{}+f({})".format(x, i)
		# print "-{}-f({})".format(x, i)
		list_of_shots.append(x+fib_list[i])
		list_of_shots.append(x-fib_list[i])
		list_of_shots.append(-x+fib_list[i])
		list_of_shots.append(-x-fib_list[i])
	x += 1

for ship in xrange(100):
	hit = False
	position = randint(-50,50)
	speed = randint(-50,50)
	for turn in xrange(5000):
		if position + speed * turn == list_of_shots[turn]:
			print "Hit!"
			hit = True
			break
	if not hit:
		print "Miss!"