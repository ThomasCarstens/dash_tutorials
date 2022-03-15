#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

#sys.stderr.write(str(lines))
debris = str(lines[1])
orbite = int(lines[0])
#sys.stderr.write(str(orbite))
chars = [ char for char in debris]
#sys.stderr.write(str(chars))

x=[]
y=[]
X = set()
Y = set()
count = 0
for i in range(len(chars)):
    x=[]
    y=[]
    divisor1 = i
    divisor2 = divisor1 + orbite/2 #unless orbite is odd.
    #sys.stderr.write('1 is'+str(divisor1%len(chars)))
    #sys.stderr.write('2 is'+str(divisor2%len(chars)))
    x = chars[int(divisor1%len(chars)):int(divisor2%len(chars))]
    y = chars[:int(divisor1%len(chars))] 
    for char in (chars[int(divisor2%len(chars)):]):
        y.append(char)
    #sys.stderr.write(str(x)+'and'+str(y))
    for i in x:
        X.add(i)
    for j in y:
        Y.add(j)
    # X = set(x) 
    # Y = set(y)
    if X == Y:
        sys.stderr.write('works.'+str(x)+'and'+str(y))
        count+=1

print(count)