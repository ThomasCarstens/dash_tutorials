                if lines[i][int(good_index)+1] != '#':
                    sys.stderr.write('nothing at '+str(i))



    
    chars = [char for char in line]
    #sys.stderr.write(str(chars))
    if chars.count('.') == 1:
        found = 1
        #sys.stderr.write(str(chars))
        row = lines.index(str(line))
        #sys.stderr.write('row is'+str(row))
        good_index = int(chars.index('.'))
        #sys.stderr.write(str(good_index))
        #sys.stderr.write('index is'+ str(good_index))
        
        above =[]
        #if row !=0:
        for i in range(row+3):
            #sys.stderr.write('i is'+str(i))
            each = lines[i][int(good_index)]
            above.append(each)
        sys.stderr.write('WE HAVE'+str(above))
        
        if '#' in above[:-3]:
            print('NOPE')
            break
        else:
            if ('#' not in above[-1:] and row > 1) or ('#' not in above[-2:] and row > 0) or ('#' not in above[-3:]):
                    print('BOOM '+str(int(good_index +1)))
                    break
                    
            else:
                print('NOPE')
                break
if found == 0:
    print('NOPE')