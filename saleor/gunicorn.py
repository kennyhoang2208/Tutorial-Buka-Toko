"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count()


bind = '0.0.0.0:' + environ.get('PORT', '8000')
max_requests = 100
worker_class = 'gevent'
workers = max_workers()
timeout = 120