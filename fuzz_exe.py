#!/usr/bin/python

from subprocess import *
import time

def interact(password):
p = Popen( ["Robots.exe"], stdin=PIPE, stdout=PIPE )
p.stdin.write("admin\n")
p.stdin.write(password + "\n")
p.stdin.write("-1\n")
output = p.stdout.read()
return output

file = open('rockyou.txt', 'r')
lines = file.readlines()

output = ''
out = open('fuzz_out.txt', 'a')

for password in lines:
boom = interact(password)
output += "\n\n" + password + "\n" + boom
out.write(output)
time.sleep(0.05)

out.close()
file.close()

