#!/usr/bin/python
import os
from glob import glob
from os.path import join
from subprocess import call
import sys

for pap in glob(join(sys.argv[1], 'paper*md')):
    print 'Word count is: '
    call(['wc', '-w', pap])

    print 'Running spell-check: '
    call(['ispell', pap])

    print 'making markdown'
    call(['./make-markdown', os.path.splitext(pap)[0]])

