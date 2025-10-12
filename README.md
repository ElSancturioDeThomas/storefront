# Commerce - Django Auction Site

A modern, responsive auction website built with Django and Bootstrap 5.3.2, featuring a sophisticated moody-gray minimalist design.

## 📸 Screenshot

![Active Listings Page](assets/active_listings.png)

*The Active Listings page showcasing the responsive card layout with Bootstrap styling and moody-gray design.*

## 🎨 Design Features

### Color Palette
- **Primary Color 01** `#FAFBFF` - Backgrounds, highlights
- **Primary Color 02** `#004EEA` - Logo, buttons, key accents  
- **Primary Color 03** `#001B35` - Headers, strong text, dark backgrounds
- **Primary Color 04** `#008DED` - Highlights, links, CTAs
- **Cloud** `#EDEFF7` - Light backgrounds
- **Smoke** `#D3D6E0` - Secondary backgrounds, dividers
- **Steel** `#BCBFCC` - Borders, icons
- **Space** `#9DA2B3` - Subtext, UI elements
- **Graphite** `#6E7180` - Body text
- **Arsenic** `#40424D` - Strong text, dark UI

## 🚀 Features

### Core Functionality
- **User Authentication** - Registration, login, logout
- **Auction Listings** - Create, view, and manage auction items
- **Bidding System** - Place bids on active auctions
- **Watchlist** - Save items for later bidding
- **Categories** - Browse items by category
- **Comments** - Discuss items with other users
- **Auction Management** - Close auctions and declare winners

### Design & UX
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Bootstrap 5.3.2** - Modern UI components
- **Bootstrap Icons** - Consistent iconography
- **Card-based Layout** - Clean, organized content display
- **Hover Effects** - Interactive elements with smooth transitions
- **Professional Typography** - Clear hierarchy and readability

## 🛠️ Technology Stack

- **Backend**: Django 4.x
- **Frontend**: Bootstrap 5.3.2, HTML5, CSS3
- **Database**: SQLite (development)
- **Icons**: Bootstrap Icons
- **Styling**: Custom CSS with CSS Variables

## 📁 Project Structure

```
commerce/
├── auctions/                 # Main app for user management
│   ├── templates/           # HTML templates
│   ├── static/             # CSS and static files
│   ├── models.py           # User and Watchlist models
│   ├── views.py            # Authentication views
│   └── urls.py             # URL routing
├── listings/               # App for auction listings
│   ├── templates/          # Listing templates
│   ├── models.py           # Listing, Bid, Comment models
│   ├── views.py            # Listing views
│   └── urls.py             # Listing URLs
├── commerce/               # Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
└── manage.py               # Django management script
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Django 4.x
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ElSancturioDeThomas/storefront.git
   cd storefront
   ```

2. **Install dependencies**
   ```bash
   pip install django
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your browser and go to `http://localhost:8000/`

## 📱 Pages & Features

### Homepage (`/`)
- Displays all active auction listings
- Responsive card grid layout
- Quick access to create new listings

### Categories (`/categories/`)
- Browse items by category
- Beautiful category cards with icons
- Filtered listing views

### Create Listing (`/create/`)
- Form to create new auction items
- Image upload support
- Category selection
- Starting bid configuration

### Listing Detail (`/listings/<id>/`)
- Detailed item information
- Bidding interface
- Watchlist management
- Comments section
- Owner controls (close auction)

### User Authentication
- **Registration** (`/register/`) - Create new accounts
- **Login** (`/login/`) - Sign in to existing accounts
- **Logout** - Secure session termination

### Watchlist (`/watchlist/`)
- View saved items
- Quick removal options
- Direct links to item details

## 🎨 Design System

### Components
- **Cards** - Consistent content containers
- **Buttons** - Primary, secondary, and outline variants
- **Forms** - Styled inputs with validation
- **Navigation** - Responsive navbar with dropdown
- **Alerts** - Status messages and notifications
- **Badges** - Category and count indicators

### Responsive Breakpoints
- **Mobile** (< 768px) - Single column layout
- **Tablet** (768px - 991px) - Two column layout
- **Desktop** (≥ 992px) - Three column layout

## 🔧 Configuration

### Django Settings
The project uses standard Django settings with:
- SQLite database for development
- Static files configuration
- Template settings
- Authentication settings

### Static Files
- Bootstrap 5.3.2 loaded via CDN
- Bootstrap Icons via CDN
- Custom CSS with CSS variables
- Responsive image handling

## 🧪 Testing

To run the Django test suite:
```bash
python manage.py test
```

## 📝 API Endpoints

### Authentication
- `POST /register/` - User registration
- `POST /login/` - User login
- `GET /logout/` - User logout

### Listings
- `GET /` - List all active listings
- `GET /listings/<id>/` - View specific listing
- `POST /create/` - Create new listing
- `POST /listings/<id>/bid/` - Place a bid
- `POST /listings/<id>/close/` - Close auction

### Watchlist
- `GET /watchlist/` - View user's watchlist
- `POST /watchlist/add/<id>/` - Add to watchlist
- `POST /watchlist/remove/<id>/` - Remove from watchlist

### Categories
- `GET /categories/` - List all categories
- `GET /categories/<category>/` - List items in category

## 🚀 Deployment

### Production Considerations
- Use PostgreSQL or MySQL for production database
- Configure static files serving
- Set up environment variables
- Use a production WSGI server (Gunicorn)
- Configure reverse proxy (Nginx)

### Environment Variables
```bash
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
ALLOWED_HOSTS=your-domain.com
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is part of the CS50 Web Programming course and is for educational purposes.

## 🙏 Acknowledgments

- **CS50 Web Programming** - Course structure and requirements
- **Django** - Web framework
- **Bootstrap** - UI framework
- **Bootstrap Icons** - Icon library

## 📞 Support

For questions or support, please open an issue in the GitHub repository.

---

**Built with ❤️ using Django and Bootstrap**
