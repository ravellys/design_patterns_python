from tornado import ioloop
from tornado import httpserver
from tornado.web import Application

from controller.produto import *


class RunApp(Application):
    def __init__(self):
        handlers = [
            ('/', Index),
            ('/produto/create', Create),
            (r'/produto/update/(\d+)/status/(\d+)', Update),
            (r'/produto/delete/(\d+)', Delete),
        ]

        settings = dict(
            debug=True,
            template_path='views',
            static_path='static'
        )

        Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    http_server = httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    ioloop.IOLoop.instance().start()
