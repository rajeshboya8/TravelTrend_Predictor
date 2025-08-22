# TTPS (Tourism and Travels Prediction System)

A machine learning-based Django web application that predicts tourist behavior and preferences based on user-provided information. This project integrates a trained ML model with a Django web framework to provide intelligent tourism predictions.

## 🚀 Features

- **Machine Learning Integration**: Uses XGBoost and scikit-learn for predictive modeling
- **Django Web Framework**: Modern web interface with Materialize CSS
- **Tourist Prediction**: Analyzes user data to predict tourism patterns
- **Responsive Design**: Mobile-friendly interface
- **Admin Panel**: Django admin interface for data management

## 📋 Prerequisites

- Python 3.7+
- pip (Python package installer)
- Git

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rajeshboya8/ttp.git
   cd ttps
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Main application: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

## 📁 Project Structure

```
ttps/
├── main/                    # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── urls.py             # URL routing
│   ├── forms.py            # Form definitions
│   ├── ml_model.py         # Machine learning model
│   ├── templates/          # HTML templates
│   ├── static/             # Static files (CSS, JS, images)
│   └── migrations/         # Database migrations
├── ttps/                   # Django project settings
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── requirements.txt        # Python dependencies
├── manage.py              # Django management script
└── README.md              # Project documentation
```

## 🤖 Machine Learning Components

- **XGBoost Model**: Primary prediction model
- **Scikit-learn**: Data preprocessing and feature engineering
- **Pandas & NumPy**: Data manipulation and numerical operations
- **Joblib**: Model serialization

## 🎨 Technologies Used

- **Backend**: Django 2.2.4
- **Frontend**: HTML, CSS, JavaScript, Materialize CSS
- **Machine Learning**: XGBoost, scikit-learn, pandas, numpy
- **Database**: SQLite (development)

## 📊 Usage

1. Navigate to the prediction page
2. Fill in the required information about the tourist
3. Submit the form to get predictions
4. View the results and recommendations

## 🔧 Configuration

The project uses Django's default settings. For production deployment:

1. Update `settings.py` with production settings
2. Configure a production database (PostgreSQL recommended)
3. Set up static file serving
4. Configure environment variables for sensitive data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Rajesh Boya**
- GitHub: [@rajeshboya8](https://github.com/rajeshboya8)

## 🙏 Acknowledgments

- Django community for the excellent web framework
- XGBoost and scikit-learn teams for ML libraries
- Materialize CSS for the beautiful UI components

