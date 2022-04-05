def init_app(app):
    from application.private import category
    category.init_app(app)
    from application.private import group
    group.init_app(app)
    from application.private import user
    user.init_app(app)
    from application.private import product
    product.init_app(app)

    return app
