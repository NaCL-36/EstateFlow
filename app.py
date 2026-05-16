import os
from flask import Flask, render_template
from flask_login import LoginManager
from config import config
from models import db, User, Property, Inquiry
from utils.email_service import mail
from routes.main_routes import main_bp
from routes.admin_routes import admin_bp
from routes.inquiry_routes import inquiry_bp

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'admin.login'
    login_manager.login_message = 'Please log in to access this page.'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(inquiry_bp)

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template('500.html'), 500

    # Create database and sample data
    with app.app_context():
        db.create_all()
        create_sample_data(app)

    return app

def create_sample_data(app):
    """Create sample data if database is empty."""
    if User.query.first() is None:
        # Create admin user
        admin = User(username='admin', email='admin@estateflow.com')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()

    if Property.query.first() is None:
        sample_properties = [
            Property(
                title='Modern Downtown Penthouse',
                description='Stunning penthouse with panoramic city views, luxury finishes, and smart home automation.',
                price=2500000,
                location='New York, NY',
                property_type='Penthouse',
                bedrooms=3,
                bathrooms=3,
                area=2800,
                status='available'
            ),
            Property(
                title='Cozy Suburban Family Home',
                description='Perfect family home with spacious backyard, modern kitchen, and great schools nearby.',
                price=450000,
                location='Austin, TX',
                property_type='House',
                bedrooms=4,
                bathrooms=2.5,
                area=2200,
                status='available'
            ),
            Property(
                title='Luxury Beach Villa',
                description='Exclusive beachfront villa with private beach access, infinity pool, and resort amenities.',
                price=3500000,
                location='Miami, FL',
                property_type='Villa',
                bedrooms=5,
                bathrooms=4,
                area=4500,
                status='available'
            ),
            Property(
                title='Urban Loft in Historic District',
                description='Charming loft with exposed brick, high ceilings, and vibrant neighborhood atmosphere.',
                price=650000,
                location='Chicago, IL',
                property_type='Loft',
                bedrooms=2,
                bathrooms=2,
                area=1400,
                status='available'
            ),
            Property(
                title='Mountain Cabin Retreat',
                description='Serene mountain cabin perfect for getaways with fireplace, deck, and nature views.',
                price=350000,
                location='Denver, CO',
                property_type='Cabin',
                bedrooms=3,
                bathrooms=2,
                area=1800,
                status='available'
            ),
            Property(
                title='Contemporary Condo with Pool',
                description='Modern condo in gated community with resort-style amenities and 24/7 security.',
                price=550000,
                location='Phoenix, AZ',
                property_type='Condo',
                bedrooms=2,
                bathrooms=2,
                area=1600,
                status='available'
            ),
            Property(
                title='Waterfront Estate',
                description='Grand waterfront estate with boat dock, manicured gardens, and gourmet kitchen.',
                price=4200000,
                location='San Diego, CA',
                property_type='Estate',
                bedrooms=6,
                bathrooms=5,
                area=5500,
                status='available'
            ),
            Property(
                title='Investment Townhouse',
                description='Well-maintained townhouse in up-and-coming neighborhood with rental history.',
                price=380000,
                location='Portland, OR',
                property_type='Townhouse',
                bedrooms=3,
                bathrooms=2.5,
                area=1900,
                status='available'
            ),
        ]

        for prop in sample_properties:
            db.session.add(prop)

        db.session.commit()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
