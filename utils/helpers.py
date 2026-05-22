import os
from werkzeug.utils import secure_filename
from flask import current_app

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_picture(file):
    """Save uploaded picture and return filename."""
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        try:
            os.makedirs(upload_folder, exist_ok=True)
        except OSError:
            pass
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        return filename
    return None

def get_price_range_filter(min_price=None, max_price=None):
    """Create price range filters for property queries."""
    filters = {}
    if min_price:
        filters['min'] = float(min_price)
    if max_price:
        filters['max'] = float(max_price)
    return filters

def format_currency(amount):
    """Format number as currency."""
    return f"${amount:,.2f}"

def format_datetime(dt):
    """Format datetime for display."""
    if dt:
        return dt.strftime('%B %d, %Y at %I:%M %p')
    return ''

def paginate_query(query, page=1, per_page=12):
    """Paginate query results."""
    return query.paginate(page=page, per_page=per_page, error_out=False)
