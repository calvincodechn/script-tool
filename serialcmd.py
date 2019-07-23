#!/usr/bin/python3

import os
import sys
import getopt

def cmd_execute(str):
    print(">>>", str)
    ret = os.system(str)
    if (ret != 0):
        print("Error: ", str)

if __name__ == "__main__":
    cmd = ''
    range_para = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:r:", ["cmd=","range_para="])
        for opt, arg in opts:
            if opt == '-h':
                print ('serial.py -c <cmd> -r <range parameter>')
                print ('  eg serial.py -c "echo ?" -r (1, 5)')
                sys.exit()
            elif opt in ("-c", "--ifile"):
                cmd = arg
            elif opt in ("-r", "--ofile"):
                range_para = eval(arg)

        if type(range_para) == type(()):
            for variable in range(*range_para):
                cmd_execute(cmd.replace('?', str(variable)))
        elif type(range_para) == type([]):
            for variable in range_para:
                cmd_execute(cmd.replace('?', str(variable)))
        else:
            pass
        
    except getopt.GetoptError:
        print ('serial.py -c <cmd> -r <range parameter>')
        print ('  eg serial.py -c "echo ?" -r (1, 5)')
        sys.exit(2)
