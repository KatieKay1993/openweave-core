#
#    Copyright (c) 2020 Google LLC.
#    All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

#
#    @file
#      This file is utility for Weave
#

from __future__ import absolute_import
from __future__ import print_function
import binascii
import logging
from ctypes import *
import six

class WeaveUtility(object):
    @staticmethod
    def VoidPtrToByteArray(ptr, len):
        if ptr:
            v = bytearray(len)
            memmove((c_byte * len).from_buffer(v), ptr, len)
            return v
        else:
            return None

    @staticmethod
    def ByteArrayToVoidPtr(array):
        if array != None:
            if not (isinstance(array, str) or isinstance(array, bytearray)):
                raise TypeError("Array must be an str or a bytearray")
            return cast( (c_byte * len(array)) .from_buffer_copy(array), c_void_p)
        else:
            return c_void_p(0)

    @staticmethod
    def IsByteArrayAllZeros(array):
        for i in range(len(array)):
            if (array[i] != 0):
                return False
        return True

    @staticmethod
    def ByteArrayToHex(array):
        return binascii.hexlify(bytes(array)).decode()

    @staticmethod
    def CStringToString(s):
        return None if s is None else s.decode()

    @staticmethod
    def StringToCString(s):
        return None if s is None else s.encode()
