# FAQ Management System

## Setup Instructions
1. Clone the repository: `git clone https://github.com/your-repo.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## API Usage
- **Fetch FAQs in English (default)**:  
  `curl http://localhost:8000/api/faqs/`
  
- **Fetch FAQs in Hindi**:  
  `curl http://localhost:8000/api/faqs/?lang=hi`

## Contribution Guidelines
- Fork the repository and submit a pull request with a detailed description of changes.
