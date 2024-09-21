from .ai import ai_routes


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(ai_routes)