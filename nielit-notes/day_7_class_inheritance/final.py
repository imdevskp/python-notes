import sys
open(sys.argv[1], 'w+').write(''.join([str(i)+'x'+str(int(sys.argv[2]))+'='+str(i*int(sys.argv[2]))+'\n' for i in range(1, 11)]))
