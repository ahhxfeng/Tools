#! /usr/bin/env python

import os 

"""
Try to scan and list all hostname in the local net

dependency samba-common-bin and arp-scan

make sure you have installed
"""


def shellrun(cmd):
    a = os.popen(cmd)
    b = a.read()
    c = b.split('\n')
    return c

def cutarpresult(lst):
    a = []
    b = []
    for line in lst[2:]:
        if line != '':
            a.append(line)
        else:
            break
    for line in a:
        b.append(line.split('\t')[0])
    return b

def commandmaker(ip):
    return 'nmblookup -A ' + ip

def getrst(iplist):
    rst = []
    for ip in iplist:
        rst.append(shellrun(commandmaker(ip)))
    return rst

def washrst(rst):
    rtn = []
    for line in rst:
        if line[1].split(' ')[1] != 'reply':
            rtn.append(line[:-1])
    return rtn

def main():
    # interface can check by ifconfig
    interface = input('which interface to use: ')
    iplist = cutarpresult(shellrun('arp-scan -I ' + interface + ' -l'))
    for rs in washrst(getrst(iplist)):
        for line in rs:
            print(line)

if __name__ == '__main__':
    main()
