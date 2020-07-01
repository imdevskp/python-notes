import sys

fo, n = open(sys.argv[1], 'w+'), int(sys.argv[2])

fo.write(''.join([str(i)+'x'+str(int(sys.argv[2]))+'='+str(i*int(sys.argv[2]))+'\n' for i in range(1, 11)]))

