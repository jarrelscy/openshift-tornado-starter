#!/usr/bin/env python

#
# This file may be used instead of Apache mod_wsgi to run your python
# web application in a different framework.  A few examples are
# provided (cherrypi, gevent), but this file may be altered to run
# whatever framework is desired - or a completely customized service.
#

import imp
import os



if __name__ == '__main__':
   app = imp.load_source('application', 'main.py')

   app.application.listen(8080 , '0.0.0.0')
   app.ioloop.IOLoop.instance().start()
