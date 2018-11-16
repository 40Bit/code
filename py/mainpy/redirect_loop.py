a = ['a', 'b', "c", "d", "e", "f", "g"]
for i in range(0, len(a)):
	c = a[i]
	d = a[i+1]
	l = open(c+".html", "w")
	l.write('<head><meta' + d +'.html'+'></head>')
	l.close()
