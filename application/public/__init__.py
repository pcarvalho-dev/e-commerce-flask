def init_app(app):
    from application.public import auth
    auth.init_app(app)

    return app