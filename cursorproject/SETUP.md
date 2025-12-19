# TrustEd Setup Guide

## Prerequisites

Before setting up TrustEd, ensure you have the following installed:
- Python 3.8 or higher
- Node.js 14 or higher
- npm (comes with Node.js)
- Git (optional, for version control)

## Step-by-Step Setup

### 1. Clone or Download the Repository

If using Git:
```bash
git clone <repository-url>
cd trusted
```

If downloading manually, extract the files to a folder named "trusted".

### 2. Backend Setup (FastAPI)

#### Navigate to the backend directory:
```bash
cd backend
```

#### Create a virtual environment:
On Windows:
```cmd
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Install Python dependencies:
```bash
pip install -r requirements.txt
```

#### Set up environment variables:
Create a `.env` file in the backend directory with the following content:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
ENCRYPTION_KEY=your_32_character_encryption_key_here
```

Note: 
- Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/)
- The encryption key should be exactly 32 characters for AES-256 encryption

### 3. Frontend Setup (React.js)

#### Navigate to the frontend directory:
```bash
cd ../frontend
```

#### Install Node.js dependencies:
```bash
npm install
```

### 4. Running the Application

#### Option 1: Using the startup script (Windows only)
Double-click the `start.bat` file in the root directory.

#### Option 2: Manual startup

##### Start the backend server:
```bash
cd backend
uvicorn main:app --reload
```

##### Start the frontend server:
```bash
cd frontend
npm run dev
```

### 5. Access the Application

Once both servers are running:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- Backend API Documentation: http://localhost:8000/docs

## Default User Credentials

For testing purposes, the system includes demo users:

### Institution User
- Email: institution@trusted.dev
- Password: institution123

### Verifier User
- Email: verifier@trusted.dev
- Password: verifier123

### Admin User
- Email: admin@trusted.dev
- Password: admin123

## Testing the Application

1. Navigate to http://localhost:5173
2. Log in with institution credentials
3. Upload a certificate image (PNG, JPG, PDF)
4. Log out and log in with verifier credentials
5. Upload the same certificate to verify its authenticity

## Troubleshooting

### Common Issues

#### 1. "Module not found" errors
Ensure you've activated the virtual environment and installed all dependencies:
```bash
pip install -r requirements.txt
```

#### 2. "Port already in use" errors
The default ports are 8000 (backend) and 5173 (frontend). If these are in use:
- Backend: `uvicorn main:app --reload --port 8001`
- Frontend: `npm run dev -- --port 5174`

#### 3. AI extraction not working
Ensure your Gemini API key is correctly set in the environment variables.

#### 4. Permission errors
On some systems, you may need to run the terminal as administrator or use `sudo` on macOS/Linux.

### Checking Server Status

#### Backend health check:
Visit http://localhost:8000/healthz

#### Frontend:
Check the terminal output for "VITE v5.x.x ready" message

## Production Deployment

For production deployment, consider:

1. Using a production WSGI server like Gunicorn instead of uvicorn
2. Setting up a reverse proxy (Nginx)
3. Using environment variables for all secrets
4. Implementing proper SSL certificates
5. Using a production database instead of JSON files
6. Setting up proper logging and monitoring

## Updating the Application

To update the application:

1. Pull the latest changes from the repository
2. Update backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. Update frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

## Support

For issues with setup or usage, please check:
1. The console output for error messages
2. The backend API documentation at http://localhost:8000/docs
3. Ensure all prerequisites are properly installed