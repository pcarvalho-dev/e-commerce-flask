def register_routes(app):
    from application.routes import auth
    auth.init_app(app)

    from application.routes import category
    category.init_app(app)

    from application.routes import group
    group.init_app(app)

    from application.routes import user
    user.init_app(app)

    return app
