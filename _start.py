from uwsgi import opt

from app import create_app


def init_app():
    if opt.get('env') is None:
        env = 'dev' # default environment
    else:
        env = opt.get('env').decode('utf-8')

    return create_app(env.upper())


application = init_app()
