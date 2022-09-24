from app.main import create_app


if __name__ == '__main__':
    app = create_app('dev')
    app.app_context().push()
    app.run()
else:
    gunicorn_app = create_app('prod')
