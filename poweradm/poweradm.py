#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Power Adm
# main.py
#
# Copyright (c) 2014 Kairo Araujo
#
# It was created for personal use. There are no guarantees of the author.
# Use at your own risk.
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
from config import *
from createlparconf import *
from findchange import *
from execchange import *
from nimmain import *
from nimclear import *
import os

def main_poweradm():

    os.system('clear')
    print ("\n\n[ Power Adm ]\n[ Version: %s - © 2014 Kairo Araujo - BSD License ]\n" % version)

    poweradm = raw_input("\nPower Adm options\n"
                  "1. LPAR configuration.\n"
                  "2. Execute the LPAR creation.\n"
                  "3. Deploy OS on an existing LPAR.\n"
                  "4. Clear NIM OS deploy configs\n"
                  "5. Quit\n\n"
                  "Please choose an option: ")

    if poweradm == '1':

        exec_createlparconf()

    elif poweradm == '2':

        exec_findlpar = findChange('changenum')
        exec_findlpar.selectChange()
        check_exec_findlpar = checkOk('\nDo you want execute change/ticket %s? (y/n): ' %
                (exec_findlpar.getChange()), 'n')
        check_exec_findlpar.mkCheck()
        if check_exec_findlpar.answerCheck() == 'y':
            exec_change = ExecChange('%s' % (exec_findlpar.getChange()))
            exec_change.runChange()
        else:
            print ('Aborting change/ticket %s...\nExiting!' % (exec_findlpar.getChange()))
            exit

    elif poweradm == '3':

        nimmain()

    elif poweradm == '4':

        nimclear()

    elif poweradm == '5':
        print ("5. Quit")
        print ("Quiting...")
        exit()

    else:
        print ("Invalid option. Quiting")
        exit()


