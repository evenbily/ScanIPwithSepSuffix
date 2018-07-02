#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
import sys
import ipaddr

reload(sys)
sys.setdefaultencoding('utf-8')

fn = 'china_ip_list.txt'
ips = 'ips.txt'

def parser():
    f = open(fn,'r+')
    f_result = open(ips,'w+')
    print "start write\n"
    for line in f:
        #print line.strip()
        ipNet = ipaddr.IPv4Network(line.strip())
        #print str(ipNet)
        for ip in ipNet:
            strip = str(ip)
            #print strip
            if strip.endswith('.250'):
                f_result.writelines(strip+"\n")
                f_result.flush()
                #print strip
    print "done\n"
    f.close()
    f_result.close()

if __name__ == '__main__':
	parser()
