from uwsgi import opt

from app import create_app


def init_app(env='DEV'):
    return create_app(env.upper())


if opt.get('env') is None:
    env = 'dev' #default environment
else:
    env = opt.get('env').decode('utf-8')


application = init_app(env)
