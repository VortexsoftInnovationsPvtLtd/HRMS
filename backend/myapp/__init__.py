from flask import Flask, jsonify, redirect
from flask_cors import CORS
from myapp.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    CORS(app, origins=Config.CORS_ORIGINS)

    # Import and register blueprints
    from myapp.routes.employee import employee_bp
    app.register_blueprint(employee_bp, url_prefix='/api')

    # Test route
    @app.route('/ping')
    def ping():
        return "pong"

    # Root route - only one implementation (choose either jsonify or redirect)
    @app.route('/')
    def root():
        # Choose ONE of these options:

        # Option 1: Return API information as JSON
        return jsonify({
            "message": "HRMS API is running",
            "endpoints": {
                "employees": "/api/employees",
                "ping": "/ping"
            }
        })

        # OR Option 2: Redirect to main API endpoint
        # return redirect('/api/employees')

    # Print all registered routes for debugging
    print("Registered routes:")
    print(app.url_map)

    return app


app = create_app()