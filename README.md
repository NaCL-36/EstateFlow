# EstateFlow - Premium Real Estate Platform

A professional, modern, and fully-responsive real estate listing website built with Flask, Python, and Bootstrap 5. Perfect for freelancer portfolios and real clients.

## 🏆 Features

### Public Website
- **Home Page** - Hero section with featured properties and call-to-action
- **Properties Listing** - Full property catalog with advanced filtering
- **Property Details** - Comprehensive property information with inquiry form
- **About Page** - Company information and team showcase
- **Contact Page** - Contact information and inquiry form
- **Search & Filtering** - Filter by location, price, property type, bedrooms

### Property Management
- **Title, Description, Price** - Essential property information
- **Location & Type** - City and property type classification
- **Bedrooms & Bathrooms** - Accommodation details
- **Area & Images** - Square footage and featured image support
- **Property Status** - Available, Pending, or Sold status tracking

### Inquiry System
- **Automated Inquiry Form** - On every property details page
- **User Information Capture** - Name, email, phone, and message
- **Database Storage** - All inquiries saved for follow-up
- **Email Automation** - Auto-reply to customers and admin notifications
- **Status Tracking** - New → Contacted → Visit Scheduled → Closed

### Admin Dashboard
- **Secure Authentication** - Username/password login system
- **Property Management** - Add, edit, delete properties
- **Image Upload** - Featured image support for each property
- **Inquiry Management** - View and manage all inquiries
- **Status Updates** - Track inquiry progress
- **Statistics** - Dashboard with key metrics and recent activity

## 🛠️ Technology Stack

### Backend
- **Flask** - Lightweight Python web framework
- **Flask-SQLAlchemy** - ORM for database operations
- **Flask-Login** - User authentication management
- **Flask-Mail** - Email sending functionality
- **SQLite** - Lightweight database (easily upgradeable to PostgreSQL)
- **Werkzeug** - Secure password hashing

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Professional styling with custom design system
- **JavaScript** - Interactive functionality
- **Bootstrap 5** - Responsive component framework
- **Font Awesome** - Icon library

## 📁 Project Structure

```
EstateFlow/
├── app.py                           # Main Flask application
├── config.py                        # Configuration settings
├── models.py                        # Database models
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
├── static/
│   ├── css/
│   │   └── style.css               # Professional styling
│   ├── js/
│   │   └── main.js                 # JavaScript functionality
│   ├── images/                      # Static images
│   └── uploads/                     # Property images
│
├── templates/
│   ├── base.html                   # Base template inheritance
│   ├── index.html                  # Home page
│   ├── properties.html             # Properties listing
│   ├── property_details.html       # Property details page
│   ├── about.html                  # About page
│   ├── contact.html                # Contact page
│   ├── login.html                  # Admin login
│   ├── dashboard.html              # Admin dashboard
│   ├── add_property.html           # Add property form
│   ├── edit_property.html          # Edit property form
│   ├── manage_properties.html      # Properties management
│   ├── inquiries.html              # Inquiry management
│   ├── 404.html                    # Not found page
│   └── 500.html                    # Server error page
│
├── routes/
│   ├── main_routes.py              # Public website routes
│   ├── admin_routes.py             # Admin dashboard routes
│   └── inquiry_routes.py           # Inquiry handling routes
│
└── utils/
    ├── email_service.py            # Email automation
    └── helpers.py                  # Utility functions
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd EstateFlow
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Initialize Database

The database is automatically created when you run the app for the first time. Sample data is also populated automatically.

### Step 5: Run the Application

```bash
python app.py
```

The application will start at `http://localhost:5000`

## 📝 Configuration

Edit `config.py` to customize:
- Database settings
- Email configuration
- Upload folder paths
- Session settings

### Email Configuration

To enable email functionality, set these environment variables:

```bash
export MAIL_SERVER=smtp.gmail.com
export MAIL_PORT=587
export MAIL_USERNAME=your-email@gmail.com
export MAIL_PASSWORD=your-app-password
export MAIL_DEFAULT_SENDER=noreply@estateflow.com
```

## 🔐 Admin Login

Default credentials (change in production):
- **Username**: admin
- **Password**: admin123

Access admin dashboard at: `http://localhost:5000/admin/login`

## 📊 Database Models

### User Model
- id, username, password_hash, email, created_at

### Property Model
- id, title, description, price, location, property_type
- bedrooms, bathrooms, area, featured_image, status
- created_at, updated_at

### Inquiry Model
- id, name, email, phone, message, property_id
- status (New, Contacted, Visit Scheduled, Closed)
- created_at, updated_at

## 🎨 Design Features

- **Professional Color Scheme**: Navy, White, Light Gray, and Gold
- **Responsive Design**: Works on mobile, tablet, and desktop
- **Smooth Animations**: Hover effects and transitions
- **Modern Cards**: Clean, professional property cards
- **Sticky Filters**: Easy property filtering
- **Admin Sidebar**: Organized admin navigation
- **Hero Section**: Impressive landing section

## ✨ Key Functionality

### Public Features
- Browse properties with advanced filtering
- Search by keyword, location, price, type, bedrooms
- View detailed property information
- Submit inquiries for properties
- Responsive mobile-friendly interface

### Admin Features
- Secure login with session management
- Add/edit/delete properties
- Upload property images
- View all inquiries
- Update inquiry status
- Dashboard with statistics
- Email notifications

## 🔧 Customization

### Adding New Property Types

Edit in `add_property.html` and `edit_property.html`:
```html
<option>Your New Type</option>
```

### Changing Colors

Edit CSS variables in `style.css`:
```css
:root {
    --navy: #your-color;
    --gold: #your-color;
}
```

### Email Templates

Customize email templates in `utils/email_service.py`

## 📈 Future Enhancements

- [ ] User registration for clients
- [ ] Saved properties/favorites list
- [ ] Property image galleries
- [ ] Advanced analytics dashboard
- [ ] Payment integration
- [ ] Property comparison tool
- [ ] Virtual tours support
- [ ] SMS notifications
- [ ] Multi-language support
- [ ] API for third-party integration

## 🐛 Troubleshooting

### Database Issues
```bash
# Delete and recreate database
rm estateflow.db
python app.py
```

### Email Not Sending
- Check email credentials
- Verify SMTP settings
- Check firewall/antivirus blocking

### Import Errors
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

## 📄 License

This project is open source and available for educational and commercial use.

## 💼 Portfolio Use

This project is perfect for:
- Freelancer portfolios
- Demonstrating Flask expertise
- Real estate business websites
- Client projects
- Learning web development

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.

## 📧 Support

For issues or questions, please create an issue in the repository.

---

**Built with ❤️ using Flask & Bootstrap**

EstateFlow - Premium Real Estate Platform for the Modern Web
