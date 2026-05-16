from flask import Blueprint, render_template, request, jsonify, current_app
from models import db, Property, Inquiry
from utils.helpers import paginate_query
from sqlalchemy import or_, and_

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Home page with featured properties."""
    featured = Property.query.filter_by(status='available').limit(6).all()
    return render_template('index.html', featured_properties=featured)

@main_bp.route('/properties')
def properties():
    """Properties listing page with filtering."""
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '').strip()
    city = request.args.get('city', '').strip()
    property_type = request.args.get('type', '').strip()
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    bedrooms = request.args.get('bedrooms', type=int)

    query = Property.query.filter_by(status='available')

    if search:
        query = query.filter(
            or_(
                Property.title.ilike(f'%{search}%'),
                Property.description.ilike(f'%{search}%')
            )
        )

    if city:
        query = query.filter(Property.location.ilike(f'%{city}%'))

    if property_type:
        query = query.filter(Property.property_type == property_type)

    if min_price is not None:
        query = query.filter(Property.price >= min_price)

    if max_price is not None:
        query = query.filter(Property.price <= max_price)

    if bedrooms:
        query = query.filter(Property.bedrooms >= bedrooms)

    properties_page = paginate_query(query, page, 12)

    property_types = db.session.query(Property.property_type).distinct().all()
    property_types = [p[0] for p in property_types if p[0]]

    cities = db.session.query(Property.location).distinct().all()
    cities = [c[0] for c in cities if c[0]]

    return render_template(
        'properties.html',
        properties=properties_page.items,
        page=page,
        pages=properties_page.pages,
        total=properties_page.total,
        has_prev=properties_page.has_prev,
        has_next=properties_page.has_next,
        property_types=property_types,
        cities=cities,
        search=search,
        city=city,
        property_type=property_type,
        min_price=min_price,
        max_price=max_price,
        bedrooms=bedrooms
    )

@main_bp.route('/property/<int:property_id>')
def property_details(property_id):
    """Property details page."""
    property = Property.query.get_or_404(property_id)
    related = Property.query.filter(
        Property.property_type == property.property_type,
        Property.id != property.id,
        Property.status == 'available'
    ).limit(3).all()

    return render_template('property_details.html', property=property, related=related)

@main_bp.route('/about')
def about():
    """About page."""
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    """Contact page."""
    return render_template('contact.html')

@main_bp.route('/api/properties/search')
def api_search():
    """API endpoint for property search."""
    query = Property.query.filter_by(status='available')

    if request.args.get('search'):
        search = request.args.get('search')
        query = query.filter(
            or_(Property.title.ilike(f'%{search}%'))
        )

    if request.args.get('type'):
        query = query.filter(Property.property_type == request.args.get('type'))

    properties = query.limit(20).all()
    return jsonify([p.to_dict() for p in properties])
