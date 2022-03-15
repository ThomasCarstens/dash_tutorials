#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

#détermine si le jeu est en situation dans laquelle un Tetris pourrait se produire si l'on y ajoutait une unique pièce bien placée.
lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

sys.stderr.write('HELLO'+str(lines))
found = 0
above =[]
bingo = []
bingo_col = []
for line in lines:
    chars = [char for char in line]
    if chars.count('.') == 1:
        found = 1
        bingo.append(lines.index(line))
        bingo_col.append(chars.index('.'))

if len(bingo) > 3:
    sys.stderr.write('its a bingo'+str(bingo)) 
    if bingo_col.count(bingo_col[0]) == 4:
        sys.stderr.write('AT INDEX'+str(bingo_col[0])) 
        column = bingo_col[0]
        top_row = bingo[0]
if len(bingo) < 3:
    # fail
    print('NOPE')

if found == 0:
    # fail
    print('NOPE')
    
above = []
#looking above
if top_row == 0:
    pass
    #works.
    print('BOOM '+str(column+1))
else:
    for line in lines [:top_row]:
        chars = [char for char in line]
        above.append(chars[column])
    if '#' in above:
        #fail
        print('NOPE')
    else:
        #works
        print('BOOM '+str(column+1))
