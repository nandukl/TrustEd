# 🎓 TrustEd – Smart Fake Degree Recognition System

## 🧠 Problem Overview

Fake and forged educational certificates are a major concern for employers, universities, and government agencies. Manual verification is slow, inconsistent, and vulnerable to corruption. There's an urgent need for a **smart, automated, and secure digital verification platform** that can verify the authenticity of degrees and detect fake or tampered ones.

## 🚀 Objective

To design and develop a **web-based AI-powered verification platform** that:

* Digitally verifies the authenticity of academic certificates
* Detects tampered, forged, or invalid documents
* Enables institutions, employers, and students to trust digital credentials

## 🏗️ Architecture Flow

```
User Uploads Certificate (React.js UI)
            ↓
Backend (FastAPI + Python)
            ↓
Tesseract OCR (Text Extraction)
            ↓
Extracted Text Parsing
            ↓
Database Verification (JSON Files)
            ↓
Blockchain-like Ledger Storage
            ↓
Verification Result (Genuine / Suspicious)
            ↓
Admin Dashboard (React.js)
```

## ⚙️ Technologies Used

| Layer          | Technology              | Purpose                                                  |
| -------------- | ----------------------- | -------------------------------------------------------- |
| **Frontend**   | React.js, Tailwind CSS  | Certificate upload, result display, and admin dashboard  |
| **Backend**    | FastAPI (Python)        | API handling, OCR integration, and verification logic     |
| **Database**   | JSON Files + Blockchain | Stores valid student records and certificate data        |
| **AI**         | Tesseract OCR           | Extracts text data from uploaded certificate images      |
| **Security**   | SHA-256 + AES-256       | Secure hashing and encryption of sensitive data          |

## 💡 Core Modules & Features

### 1. **User Authentication Module**

* Role-based access control (Institution, Verifier)
* JWT token authentication
* Demo user accounts for testing

### 2. **Institution Portal**

* Upload certificate images (PNG, JPG, PDF)
* Automatic data extraction using Tesseract OCR
* SHA-256 hash generation for certificate integrity
* AES-256 encryption for sensitive data
* Blockchain-like ledger storage
* Certificate records management

### 3. **Verification Module**

* Certificate authenticity checking
* Cross-verification with institutional database
* Blockchain ledger verification
* Detailed comparison reports
* Confidence scoring system

### 4. **Blockchain-like Ledger**

* Immutable certificate storage
* SHA-256 hash chaining
* Certificate metadata storage
* Verification trail

### 5. **Database Module**

* Institutions database (`institutions.json`)
* Verification records (`verifications.json`)
* Blockchain ledger (`ledger.txt`)

## 📊 Key Features

✅ OCR-based automatic certificate data extraction
✅ Real-time database validation
✅ Genuine/Suspicious classification
✅ SHA-256 hash-based integrity checking
✅ AES-256 encryption for sensitive data
✅ Blockchain-like immutable ledger
✅ Role-based access control
✅ Responsive web interface

## 🧩 Future Enhancements

* **True Blockchain Integration** for tamper-proof validation
* **QR-code generation** for instant authenticity check
* **Advanced image forensics** to detect seal or signature forgery
* **University API integration** for automatic record syncing
* **Multi-language OCR support** for regional certificates
* **Mobile application** for on-the-go verification

## 🛠️ Setup Instructions

### Prerequisites

* Python 3.8+
* Node.js 14+
* Tesseract OCR (Optional but recommended)

### Quick Start (Windows)

1. Double-click the `start.bat` file to launch both backend and frontend servers automatically

### Manual Setup

#### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables:
   ```bash
   export ENCRYPTION_KEY="your_32_char_encryption_key_here"
   ```
   
   On Windows, use:
   ```cmd
   set ENCRYPTION_KEY=your_32_char_encryption_key_here
   ```

5. (Optional) Install Tesseract OCR for better certificate data extraction:
   ```bash
   python install_tesseract.py
   ```
   
   Or follow the instructions in [README_TESSERACT.md](README_TESSERACT.md)

6. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```

#### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

## 🌐 Access Points

* **Frontend**: http://localhost:5173
* **Backend API**: http://localhost:8000
* **API Docs**: http://localhost:8000/docs

## 📁 Project Structure

```
.
├── backend/
│   ├── main.py              # FastAPI application
│   ├── gemini_extractor.py  # OCR text extraction (renamed from gemini_extractor.py)
│   ├── ocr.py               # OCR processing functions
│   ├── utils.py             # Utility functions
│   ├── storage.py           # Data storage functions
│   ├── auth.py              # Authentication functions
│   ├── ai.py                # AI forgery detection
│   ├── requirements.txt     # Python dependencies
│   └── db/                  # Database files
│       ├── institutions.json
│       ├── verifications.json
│       └── ledger.txt
├── install_tesseract.py     # Tesseract OCR installation script
├── README_TESSERACT.md      # Tesseract OCR installation guide
└── frontend/
    ├── src/
    │   ├── pages/           # React components
    │   ├── auth/            # Authentication context
    │   └── services/        # API services
    ├── package.json         # Node.js dependencies
    └── tailwind.config.js   # Tailwind CSS configuration
```

## 🔐 Security Features

* **SHA-256 Hashing**: Ensures certificate integrity
* **AES-256 Encryption**: Protects sensitive data
* **JWT Authentication**: Secure user sessions
* **Role-based Access**: Controlled system access
* **Immutable Ledger**: Tamper-proof record storage

## 👥 User Roles

1. **Institution**: Can upload and manage certificates
2. **Verifier**: Can verify certificate authenticity

## 📈 System Workflow

1. Institution uploads certificate image
2. Tesseract OCR extracts certificate data
3. System generates SHA-256 hash of certificate
4. Data is encrypted with AES-256
5. Certificate is stored in blockchain-like ledger
6. Verifier uploads certificate for checking
7. System verifies against ledger and database
8. Detailed verification report is generated

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.