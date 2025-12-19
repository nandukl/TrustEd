# TrustEd System Documentation

## Table of Contents
1. [System Overview](#system-overview)
2. [Architecture](#architecture)
3. [Components](#components)
4. [API Endpoints](#api-endpoints)
5. [Database Structure](#database-structure)
6. [Security Implementation](#security-implementation)
7. [User Roles](#user-roles)
8. [Workflow](#workflow)
9. [Error Handling](#error-handling)
10. [Deployment](#deployment)

## System Overview

TrustEd is a smart fake degree recognition system that uses AI-powered verification to detect fraudulent academic certificates. The system provides a secure platform for institutions to upload certificates and for verifiers to check their authenticity.

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│   Frontend      │    │    Backend       │    │   Database       │
│   (React.js)    │◄──►│   (FastAPI)      │◄──►│   (JSON Files)   │
└─────────────────┘    └──────────────────┘    └──────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  AI Services     │
                    │ (Google Gemini)  │
                    └──────────────────┘
```

## Components

### Frontend (React.js)
- **LoginPage**: User authentication interface
- **InstitutionUploadPage**: Certificate upload and management for institutions
- **VerifierPage**: Certificate verification interface
- **AuthContext**: Authentication state management
- **API Services**: Backend communication layer

### Backend (FastAPI)
- **main.py**: Main application with API endpoints
- **gemini_extractor.py**: AI-powered certificate data extraction
- **utils.py**: Utility functions for hashing and ledger operations
- **storage.py**: Data storage and retrieval functions
- **auth.py**: Authentication and authorization functions
- **ai.py**: AI-based forgery detection

### Database
- **institutions.json**: Valid institution records
- **verifications.json**: Verification attempt records
- **ledger.txt**: Blockchain-like immutable certificate ledger

## API Endpoints

### Authentication
- `POST /login` - User authentication
  - Request: `{email, password}`
  - Response: `{token, role, name}`

### Institution Portal
- `POST /institution/upload-certificate` - Upload a single certificate
- `GET /institution/certificates` - Get all certificates uploaded by institution
- `POST /institution/upload-certificates-csv` - Upload multiple certificates via CSV
- `POST /institution/batch-upload-certificate` - Batch upload certificate images

### Verification
- `POST /verify` - Verify certificate authenticity
- `GET /verifications` - List verification attempts

### Public
- `GET /institutions` - List valid institutions
- `POST /institutions/bulk` - Bulk upload institutions
- `GET /` - Health check
- `GET /healthz` - Health check

## Database Structure

### institutions.json
```json
{
  "items": [
    {
      "name": "Student Name",
      "institution": "Institution Name",
      "year": 2021,
      "certificate_id": "CERT-ID-001"
    }
  ]
}
```

### verifications.json
```json
{
  "items": [
    {
      "id": "vrf_1234567890",
      "status": "valid|suspicious",
      "confidence": 0.95,
      "reasons": ["Reason 1", "Reason 2"],
      "extracted": {
        "name": "Extracted Name",
        "institution": "Extracted Institution",
        "year": 2021,
        "certificate_id": "EXTRACTED-ID"
      },
      "institution_match": { /* Matched institution record */ },
      "file_hash": "sha256_hash",
      "created_at": "ISO timestamp"
    }
  ]
}
```

### ledger.txt
Each line contains a JSON block:
```json
{
  "timestamp": "ISO timestamp",
  "certificate_file_hash": "sha256_hash",
  "prev_block_hash": "previous_block_hash",
  "block_hash": "current_block_hash"
}
```

Or for certificate records:
```json
{
  "student_id": "STU-1234",
  "certificate_data": {
    "student_name": "Student Name",
    "institution_name": "Institution Name",
    "year": 2021,
    "certificate_id": "CERT-ID-001",
    "file_name": "certificate.jpg",
    "uploaded_by": "institution@trusted.dev",
    "upload_date": "ISO timestamp"
  },
  "file_hash": "sha256_hash",
  "timestamp": "Unix timestamp",
  "block_type": "certificate",
  "block_hash": "block_hash"
}
```

## Security Implementation

### Data Encryption
- **AES-256**: Encryption of sensitive certificate data
- **SHA-256**: Hashing for data integrity verification
- **JWT**: Secure authentication tokens

### Access Control
- **Role-based access**: Institution and Verifier roles
- **Token authentication**: Secure API access
- **Input validation**: Protection against malicious uploads

### Data Protection
- Encrypted storage of sensitive fields
- Immutable ledger for certificate records
- Secure transmission of data between components

## User Roles

### Institution
- Upload certificates to the system
- View uploaded certificate records
- Manage certificate data

### Verifier
- Verify certificate authenticity
- View verification results
- Access verification reports

## Workflow

### Certificate Upload Process
1. Institution logs in to the portal
2. Selects certificate image file (PNG, JPG, PDF)
3. System uploads file to backend
4. Gemini AI extracts certificate data
5. System generates SHA-256 hash of file
6. Data is encrypted with AES-256
7. Certificate is stored in blockchain ledger
8. Record is added to institutions database

### Certificate Verification Process
1. Verifier logs in to the portal
2. Selects certificate image file for verification
3. System uploads file to backend
4. Gemini AI extracts certificate data
5. System generates SHA-256 hash of file
6. Hash is checked against blockchain ledger
7. Data is cross-verified with institutions database
8. Verification result is generated and returned

## Error Handling

### Common Errors
- **Invalid file format**: Only PNG, JPG, PDF supported
- **Authentication failure**: Invalid credentials
- **AI extraction failure**: Could not extract data from certificate
- **Database errors**: Storage/retrieval issues
- **Network errors**: Communication failures

### Error Responses
All API errors follow this format:
```json
{
  "detail": "Error message"
}
```

## Deployment

### Environment Variables
- `GEMINI_API_KEY`: Google Gemini API key for AI services
- `ENCRYPTION_KEY`: 32-character key for AES-256 encryption

### Production Deployment
1. Set up production database (consider MongoDB for scalability)
2. Configure environment variables
3. Deploy backend using a WSGI server (Gunicorn, uWSGI)
4. Deploy frontend using a static file server (Nginx)
5. Set up SSL certificates for secure communication
6. Configure load balancing for high availability

### Scaling Considerations
- Implement database indexing for faster queries
- Use caching for frequently accessed data
- Consider cloud storage for certificate images
- Implement rate limiting for API endpoints
- Use a message queue for background processing