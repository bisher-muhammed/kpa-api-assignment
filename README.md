# KPA API Assignment

This is a Django REST Framework-based API project for submitting and retrieving wheel specification forms.

## Project Structure

```
kpa-api-assignment/
│
├── api/                  # App containing models, views, serializers, urls
├── core/                 # Django project folder
├── manage.py             # Django management script
├── db.sqlite3            # SQLite database
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables file
├── .gitignore            # Git ignored files
├── schema.yaml           # API schema (for Swagger)
└── README.md             # Project documentation
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/bisher-muhammed/kpa-api-assignment.git
cd kpa-api-assignment
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # For Windows
# Or
source venv/bin/activate    # For Linux/macOS
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Server will be running at:

```
http://127.0.0.1:8000/
```

---

## API Endpoints

### Wheel Specification Form

#### 1. Submit a Form

**POST** `/api/forms/wheel-specifications/`

**Request Body Example:**

```json
{
  "form_number": "WHEEL-001",
  "submitted_by": "John Doe",
  "submitted_date": "2025-07-27",
  "axle_box_housing_bore_dia": "123 mm",
  "bearing_seat_diameter": "80 mm",
  "condemning_dia": "50 mm",
  "intermediate_wwp": "65 mm",
  "last_shop_issue_size": "88 mm",
  "roller_bearing_bore_dia": "150 mm",
  "roller_bearing_outer_dia": "250 mm",
  "roller_bearing_width": "70 mm",
  "tread_diameter_new": "920 mm",
  "variation_same_axle": "2 mm",
  "variation_same_bogie": "3 mm",
  "variation_same_coach": "4 mm",
  "wheel_disc_width": "140 mm",
  "wheel_gauge": "1676 mm",
  "wheel_profile": "IRW/UB-1"
}
```

#### 2. Get All Forms

**GET** `/api/forms/wheel-specifications/`

Returns a list of all submitted forms.

---

## Swagger Documentation

After running the server, visit:

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

This will open the Swagger UI where you can explore and test the API.

---

## Notes

* `.env` file contains environment variables.
* Make sure to activate the virtual environment before running any Django commands
