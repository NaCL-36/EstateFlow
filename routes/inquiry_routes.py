from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from models import db, Property, Inquiry
from utils.email_service import send_inquiry_confirmation_email, send_inquiry_notification_email

inquiry_bp = Blueprint('inquiry', __name__)

@inquiry_bp.route('/property/<int:property_id>/inquiry', methods=['POST'])
def submit_inquiry(property_id):
    """Handle inquiry form submission."""
    property = Property.query.get_or_404(property_id)

    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    phone = request.form.get('phone', '').strip()
    message = request.form.get('message', '').strip()

    if not all([name, email, phone, message]):
        flash('Please fill in all fields.', 'danger')
        return redirect(url_for('main.property_details', property_id=property_id))

    inquiry = Inquiry(
        name=name,
        email=email,
        phone=phone,
        message=message,
        property_id=property_id,
        status='New'
    )

    db.session.add(inquiry)
    db.session.commit()

    # Send emails
    send_inquiry_confirmation_email(inquiry)
    send_inquiry_notification_email(inquiry)

    flash('Inquiry submitted successfully! We will contact you shortly.', 'success')
    return redirect(url_for('main.property_details', property_id=property_id))

@inquiry_bp.route('/api/inquiry/<int:inquiry_id>', methods=['GET'])
def get_inquiry(inquiry_id):
    """Get inquiry details via API."""
    inquiry = Inquiry.query.get_or_404(inquiry_id)
    return jsonify(inquiry.to_dict())
