#!/usr/bin/env python
##############################################################################
# Copyright by The HDF Group.                                                #
# All rights reserved.                                                       #
#                                                                            #
# This file is part of H5Serv (HDF5 REST Server) Service, Libraries and      #
# Utilities.  The full HDF5 REST Server copyright notice, including       s   #
# terms governing use, modification, and redistribution, is contained in     #
# the file COPYING, which can be found at the root of the source code        #
# distribution tree.  If you do not have access to this file, you may        #
# request a copy from help@hdfgroup.org.                                     #
##############################################################################

import os
import sys

hl_tests = ('test_attribute',
         'test_committedtype',
         'test_complex_numbers',
         'test_dataset_compound',
         'test_dataset_create',
         'test_dataset_extend',
         'test_dataset_fancyselect',
         'test_dataset_objref',
         'test_dataset_getitem',
         'test_dataset_pointselect',
         'test_dataset_scalar',
         'test_dataset_setitem',
         'test_dimscale',
         'test_file',
         'test_folder',
         'test_group',
         'test_table',
         'test_visit',
         'test_vlentype'
         )

#
# Run tests
#
os.chdir('test')
os.chdir('hl')
for file_name in hl_tests:
    print(file_name)
    rc = os.system('python ' + file_name + '.py')
    if rc != 0:
        sys.exit("Failed")

os.chdir('..')
os.chdir('..')
print("Done!")
