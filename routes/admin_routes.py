from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user, login_user, logout_user
from models import db, User, Property, Inquiry
from utils.helpers import save_picture
from functools import wraps
import os

admin_bp = Blueprint('admin', __name__, url_prefix='/estateflow-secure-admin-panel')

def admin_required(f):
    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Please log in first.', 'warning')
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login page."""
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user, remember=request.form.get('remember'))
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html')

@admin_bp.route('/logout')
@login_required
def logout():
    """Admin logout."""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    """Admin dashboard."""
    total_properties = Property.query.count()
    total_inquiries = Inquiry.query.count()
    new_inquiries = Inquiry.query.filter_by(status='New').count()
    recent_inquiries = Inquiry.query.order_by(Inquiry.created_at.desc()).limit(5).all()

    return render_template(
        'dashboard.html',
        total_properties=total_properties,
        total_inquiries=total_inquiries,
        new_inquiries=new_inquiries,
        recent_inquiries=recent_inquiries
    )

@admin_bp.route('/properties')
@admin_required
def manage_properties():
    """Manage properties."""
    page = request.args.get('page', 1, type=int)
    properties = Property.query.paginate(page=page, per_page=10, error_out=False)

    return render_template('manage_properties.html', properties=properties.items, page=page, pages=properties.pages)

@admin_bp.route('/property/add', methods=['GET', 'POST'])
@admin_required
def add_property():
    """Add new property."""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        price = request.form.get('price', type=float)
        location = request.form.get('location', '').strip()
        property_type = request.form.get('property_type', '').strip()
        bedrooms = request.form.get('bedrooms', type=int)
        bathrooms = request.form.get('bathrooms', type=int)
        area = request.form.get('area', type=float)
        status = request.form.get('status', 'available')

        if not all([title, description, price, location, property_type, bedrooms, bathrooms, area]):
            flash('Please fill in all required fields.', 'danger')
            return render_template('add_property.html')

        featured_image = None
        if 'featured_image' in request.files:
            file = request.files['featured_image']
            if file and file.filename:
                featured_image = save_picture(file)

        property = Property(
            title=title,
            description=description,
            price=price,
            location=location,
            property_type=property_type,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            area=area,
            featured_image=featured_image,
            status=status
        )

        db.session.add(property)
        db.session.commit()

        flash(f'Property "{title}" added successfully!', 'success')
        return redirect(url_for('admin.manage_properties'))

    return render_template('add_property.html')

@admin_bp.route('/property/<int:property_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_property(property_id):
    """Edit property."""
    property = Property.query.get_or_404(property_id)

    if request.method == 'POST':
        property.title = request.form.get('title', property.title).strip()
        property.description = request.form.get('description', property.description).strip()
        property.price = request.form.get('price', type=float) or property.price
        property.location = request.form.get('location', property.location).strip()
        property.property_type = request.form.get('property_type', property.property_type).strip()
        property.bedrooms = request.form.get('bedrooms', type=int) or property.bedrooms
        property.bathrooms = request.form.get('bathrooms', type=int) or property.bathrooms
        property.area = request.form.get('area', type=float) or property.area
        property.status = request.form.get('status', property.status)

        if 'featured_image' in request.files:
            file = request.files['featured_image']
            if file and file.filename:
                featured_image = save_picture(file)
                if featured_image:
                    property.featured_image = featured_image

        db.session.commit()
        flash(f'Property "{property.title}" updated successfully!', 'success')
        return redirect(url_for('admin.manage_properties'))

    return render_template('edit_property.html', property=property)

@admin_bp.route('/property/<int:property_id>/delete', methods=['POST'])
@admin_required
def delete_property(property_id):
    """Delete property."""
    property = Property.query.get_or_404(property_id)
    title = property.title

    if property.featured_image:
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], property.featured_image)
        if os.path.exists(filepath):
            os.remove(filepath)

    db.session.delete(property)
    db.session.commit()

    flash(f'Property "{title}" deleted successfully!', 'success')
    return redirect(url_for('admin.manage_properties'))

@admin_bp.route('/inquiries')
@admin_required
def manage_inquiries():
    """Manage inquiries."""
    page = request.args.get('page', 1, type=int)
    status_filter = request.args.get('status', '').strip()

    query = Inquiry.query

    if status_filter:
        query = query.filter_by(status=status_filter)

    inquiries = query.order_by(Inquiry.created_at.desc()).paginate(page=page, per_page=20, error_out=False)

    return render_template('inquiries.html', inquiries=inquiries.items, page=page, pages=inquiries.pages, status_filter=status_filter)

@admin_bp.route('/inquiry/<int:inquiry_id>/status/<status>', methods=['POST'])
@admin_required
def update_inquiry_status(inquiry_id, status):
    """Update inquiry status."""
    inquiry = Inquiry.query.get_or_404(inquiry_id)

    if status in Inquiry.INQUIRY_STATUSES:
        inquiry.status = status
        db.session.commit()
        flash(f'Inquiry status updated to "{status}".', 'success')
    else:
        flash('Invalid status.', 'danger')

    return redirect(request.referrer or url_for('admin.manage_inquiries'))

@admin_bp.route('/inquiry/<int:inquiry_id>/delete', methods=['POST'])
@admin_required
def delete_inquiry(inquiry_id):
    """Delete inquiry."""
    inquiry = Inquiry.query.get_or_404(inquiry_id)
    db.session.delete(inquiry)
    db.session.commit()
    flash('Inquiry deleted successfully!', 'success')
    return redirect(request.referrer or url_for('admin.manage_inquiries'))
