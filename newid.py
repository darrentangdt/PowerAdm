#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Power Adm
# newid.py
#
# Copyright (c) 2014 Kairo Araujo
#
# This program was created to help in managing vhost devices and its hdisks
# in PowerVM (vios) servers. It was created for personal use. There are no
# guarantees of the author. Use at your own risk.
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Important:
# IBM, PowerVM (a.k.a. vios) are registered trademarks of IBM Corporation in
# the United States, other countries, or both.
#
# Imports
###############################################################################################
import time
import os.path
from globalvar import *
from config import *

# get a next free id on systems
class newId:
    def __init__(self, newid):
        self.newid = newid

    def mkId(self):
        ids = []
        systems_keys = list(systems.keys())
        systems_length = (len(systems.keys()))-1
        count = 0
        while count <= systems_length:
            # // simulation
            #os.system('cat simulation/%s >> tmp/ids_%s' % (systems_keys[count], timestr))
            # // simulation
            os.system('ssh -l poweradm %s lssyscfg -m %s -r lpar -F lpar_id >> tmp/ids_%s'
                      % (hmcserver, systems_keys[count], timestr))
            os.system('cat data/reserved_ids >> tmp/ids_%s' % (timestr))
            if os.path.isfile('tmp/reserved_ids_%s' % (timestr)):
                os.system('cat tmp/reserved_ids_%s >> tmp/ids_%s' % (timestr, timestr))
            count += 1
        fileids = open('tmp/ids_%s' % (timestr), 'r')
        ids = fileids.readlines()
        ids.sort(key=int)
        lastid = len(ids)-1
        self.newid = int(ids[lastid])+1
        if self.newid < 10:
            self.newid = ('0%s' % (self.newid))
        fileids.close()
        os.system('rm tmp/ids_%s' % (timestr))

    def getId(self):
        return self.newid
