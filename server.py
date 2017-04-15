#!/usr/bin/env python3
# coding: utf-8

from aiohttp import web
# import aiohttp_jinja2
import asyncio
# import functools
# import jinja2
import os
# import sys
import time
import webbrowser

import platform_info

START_TIME = time.time()
PORT = int(os.getenv('PORT', 8000))  # Cloud will provide a web server PORT id

# try:  # Immediately change current directory to avoid exposure of control files
#     os.chdir('static')
# except FileNotFoundError:
#    pass

app = web.Application()


async def handler(request):
    uptime = 'uptime: {}\n\n'.format(time.time - START_TIME)
    return uptime + web.Response(text=platform_info.get_platform_info())


def run_webserver(app, port=PORT):
    # aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.curdir))
    app.router.add_route('GET', '/', handler)
    # app.router.add_route('GET', '/{max_pkgs}', handler)
    app.router.add_static('/static/', path='./static')
    web.run_app(app, port=PORT)


async def launch_browser(port=PORT):
    asyncio.sleep(0.2)  # give the server a fifth of a second to come up
    webbrowser.open('localhost:{}'.format(port))


if PORT == 8000:  # we are running the server on localhost
    asyncio.run_coroutine_threadsafe(launch_browser(PORT), app.loop)
run_webserver(app, port=PORT)
