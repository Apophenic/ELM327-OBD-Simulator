#
#   OBD-II Simulator adhering to SAE standard J/1979
#
#   https://github.com/Apophenic
#
#   Copyright (c) 2015 Justin Dayer (jdayer9@gmail.com)
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#   THE SOFTWARE.

#   Program entry point.

import sys
import Server

# Default values if no cmd parameters are passed
__address = 'localhost'
__port = 1090
__startshell = False

for arg in sys.argv:
    temp = str.split(arg, '=')
    if temp[0] == '-address':
        __address = temp[1]
    elif temp[0] == '-port':
        __port = temp[1]
    elif temp[0] == '-shell':
        __startshell = True

Server.startserver(__address, int(__port), __startshell)
