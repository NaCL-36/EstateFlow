from flask_mail import Mail, Message
from flask import current_app

mail = Mail()

def send_inquiry_confirmation_email(inquiry):
    """Send confirmation email to inquiry submitter."""
    try:
        msg = Message(
            subject=f'Inquiry Received - {inquiry.property.title}',
            recipients=[inquiry.email],
            html=f"""
            <html>
                <body style="font-family: Arial, sans-serif; color: #333;">
                    <h2 style="color: #1a1a2e;">Inquiry Received</h2>
                    <p>Dear {inquiry.name},</p>
                    <p>Thank you for your inquiry about <strong>{inquiry.property.title}</strong>.</p>
                    <p><strong>Property Details:</strong></p>
                    <ul>
                        <li>Location: {inquiry.property.location}</li>
                        <li>Price: ${inquiry.property.price:,.2f}</li>
                        <li>Type: {inquiry.property.property_type}</li>
                        <li>Bedrooms: {inquiry.property.bedrooms}</li>
                        <li>Bathrooms: {inquiry.property.bathrooms}</li>
                    </ul>
                    <p>We will review your inquiry and get back to you shortly.</p>
                    <p>Best regards,<br><strong>EstateFlow Team</strong></p>
                </body>
            </html>
            """
        )
        mail.send(msg)
        return True
    except Exception as e:
        current_app.logger.error(f'Failed to send confirmation email: {str(e)}')
        return False

def send_inquiry_notification_email(inquiry):
    """Send notification email to admin about new inquiry."""
    try:
        admin_email = current_app.config.get('MAIL_DEFAULT_SENDER', 'noreply@estateflow.com')
        msg = Message(
            subject=f'New Inquiry - {inquiry.property.title}',
            recipients=[admin_email],
            html=f"""
            <html>
                <body style="font-family: Arial, sans-serif; color: #333;">
                    <h2 style="color: #d4af37;">New Inquiry Received</h2>
                    <p><strong>Property:</strong> {inquiry.property.title}</p>
                    <p><strong>Inquiry From:</strong> {inquiry.name}</p>
                    <p><strong>Email:</strong> {inquiry.email}</p>
                    <p><strong>Phone:</strong> {inquiry.phone}</p>
                    <p><strong>Message:</strong></p>
                    <p>{inquiry.message}</p>
                    <p><a href="#" style="background-color: #d4af37; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">View in Dashboard</a></p>
                </body>
            </html>
            """
        )
        mail.send(msg)
        return True
    except Exception as e:
        current_app.logger.error(f'Failed to send admin notification email: {str(e)}')
        return False
