# Plant Care Application

A comprehensive plant care management system with AI-powered disease detection, crop recommendations, and farming tools.

## Features

### 🌱 Core Features
- **Disease Detection**: AI-powered plant disease identification using computer vision
- **Crop Recommendation**: Data-driven crop suggestions based on soil and weather conditions
- **Fertilizer Calculator**: Precise fertilizer recommendations for optimal crop growth
- **Weather Integration**: Real-time weather data and forecasting
- **Farm Management**: Track crops, farms, and agricultural activities
- **Community Forum**: Connect with other farmers and agricultural experts

### 🤖 AI-Powered Tools
- **Gemini AI Integration**: Advanced plant disease detection and analysis
- **Machine Learning Models**: Crop yield prediction and optimization
- **Smart Recommendations**: Personalized farming advice based on data

## Technology Stack

### Backend
- **Framework**: Flask (Python)
- **Database**: MySQL
- **AI/ML**: Google Gemini API, TensorFlow/Keras models
- **APIs**: OpenWeather API for weather data
- **Authentication**: JWT tokens
- **Database Migration**: Alembic

### Frontend
- **Framework**: React 18
- **Styling**: Modern CSS with responsive design
- **State Management**: React Context API
- **HTTP Client**: Axios for API communication
- **UI Components**: Custom component library

## Prerequisites

Before running this application, make sure you have:

- **Python 3.8+** installed
- **Node.js 16+** and npm installed
- **MySQL** database server running
- **Gemini API Key** from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **OpenWeather API Key** from [OpenWeatherMap](https://openweathermap.org/api) (optional)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd plantCare_update
```

### 2. Backend Setup

#### Install Python Dependencies
```bash
cd backend
pip install -r requirements.txt
```

#### Environment Configuration
Create a `.env` file in the `backend` directory:
```bash
cp .env.example .env
```

Edit the `.env` file with your actual values:
```env
# Database Configuration
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_database_password
MYSQL_DB=plantcare_db

# Flask Application Settings
SECRET_KEY=your_super_secret_key_here
JWT_SECRET_KEY=your_jwt_secret_key_here
FLASK_ENV=development

# Gemini API for plant disease detection
GEMINI_API_KEY=your_gemini_api_key_here

# Email Configuration (optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=your-email@gmail.com

# Weather API (optional)
WEATHER_API_KEY=your_openweather_api_key_here
```

#### Database Setup
1. Create a MySQL database named `plantcare_db`
2. Run database migrations:
```bash
flask db upgrade
```

#### Start Backend Server
```bash
python run.py
```
The backend will run on `http://localhost:5000`

### 3. Frontend Setup

#### Install Dependencies
```bash
cd frontend
npm install
```

#### Environment Configuration
Create a `.env` file in the `frontend` directory:
```bash
cp .env.example .env
```

Edit the `.env` file:
```env
REACT_APP_API_URL=http://localhost:5000
REACT_APP_OPENWEATHER_API_KEY=your_openweather_api_key_here
```

#### Start Frontend Development Server
```bash
npm start
```
The frontend will run on `http://localhost:3000`

## Project Structure

```
plantCare_update/
├── backend/                    # Flask API backend
│   ├── app/                   # Main application package
│   │   ├── models/           # Database models
│   │   ├── routes/           # API endpoints
│   │   ├── services/         # Business logic
│   │   ├── utils/            # Helper utilities
│   │   └── static/           # Static files and ML models
│   ├── migrations/           # Database migrations
│   ├── models/               # Pre-trained ML models
│   └── requirements.txt      # Python dependencies
├── frontend/                  # React frontend application
│   ├── public/               # Static assets
│   ├── src/                  # Source code
│   │   ├── components/       # Reusable components
│   │   ├── pages/           # Page components
│   │   └── utils/           # Utility functions
│   └── package.json         # Node.js dependencies
└── README.md                # Project documentation
```

## API Documentation

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout

### Disease Detection
- `POST /api/disease-detection` - Upload and analyze plant images
- `GET /api/disease-scans` - Get user's scan history

### Crop Management
- `GET /api/crop-predictions` - Get crop recommendations
- `POST /api/monitored-crops` - Add crops to monitor
- `GET /api/farms` - Get user's farms

### Calculators
- `POST /api/calculator/fertilizer` - Calculate fertilizer requirements
- `POST /api/calculator/pesticide` - Calculate pesticide requirements

## Development

### Running Tests
```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

### Database Migrations
```bash
cd backend
flask db migrate -m "Description of changes"
flask db upgrade
```

### Building for Production
```bash
cd frontend
npm run build
```

## Environment Variables

### Backend Environment Variables
- `MYSQL_HOST` - Database host
- `MYSQL_USER` - Database username  
- `MYSQL_PASSWORD` - Database password
- `MYSQL_DB` - Database name
- `SECRET_KEY` - Flask secret key
- `JWT_SECRET_KEY` - JWT signing key
- `GEMINI_API_KEY` - Google Gemini API key
- `WEATHER_API_KEY` - OpenWeather API key

### Frontend Environment Variables
- `REACT_APP_API_URL` - Backend API URL
- `REACT_APP_OPENWEATHER_API_KEY` - OpenWeather API key

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security Notes

- Never commit `.env` files containing real API keys
- Use environment variables for all sensitive configuration
- The `.env.example` files show the required variables without exposing secrets
- API keys should be kept secure and rotated regularly

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Note**: This application uses MySQL as the database. Make sure you have MySQL installed and running before starting the backend server.