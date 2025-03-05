# X-Auto-Tweet with GUI

## Problem
Managing multiple tweets manually can be time-consuming and inefficient. If a user wants to store multiple tweets and post them one by one, they must do so manually, which requires effort and constant attention.

## Solution
X-Auto-Tweet automates the process of posting tweets at scheduled intervals. This script allows users to store multiple tweets in a database and post them automatically at predefined times, eliminating the need for manual posting.

## Brief Description
This project is a GUI-based Flask web application that enables users to:
- Store tweets along with images in a SQLite database.
- View, modify, and delete stored tweets through a user-friendly interface.
- Automatically post tweets at scheduled intervals using the Tweepy API.
- Securely store Twitter API credentials using environment variables.

## Features
- **Flask Web App**: Provides an intuitive interface for managing tweets.
- **Automated Tweet Posting**: Uses `schedule` and `tweepy` to post tweets periodically.
- **SQLite Database**: Stores tweet text and images.
- **User Authentication**: Secures API keys using environment variables.

## Technologies Used
- **Python**
- **Flask (for web interface)**
- **Tweepy (for Twitter API integration)**
- **SQLite (for database storage)**
- **Schedule (for automated posting)**
- **HTML/CSS (for frontend styling)**
- **PythonAnywhere (for deployment)**

## Installation & Setup

### 1. Clone the Repository
```bash
    git clone https://github.com/ethical-dilkhush/X-Auto-Tweet.git
    cd X-Auto-Tweet
```

### 2. Set Up a Virtual Environment
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
```

### 3. Configure API Keys
Create a `.env` file and add your Twitter API keys:
```
API_KEY=your_api_key
API_SECRET_KEY=your_secret_key
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret
```

### 4. Initialize the Database
```bash
    python Data_Inserting.py
```

### 5. Run the Flask App
```bash
    python Data_Inserting.py
```
Then, open `http://127.0.0.1:5000/` in your browser.

### 6. Run Auto Posting Script
```bash
    python auto_posting.py
```
This will start fetching tweets from the database and posting them to Twitter.

## Deploying on PythonAnywhere

### 1. Upload Files
- `Data_Inserting.py`
- `auto_posting.py`
- `database.db`
- `requirements.txt`
- `styles.css`
- `.env` (Add API keys securely in PythonAnywhere environment variables instead)

### 2. Set Up Virtual Environment on PythonAnywhere
```bash
    mkvirtualenv myenv --python=python3.9
    workon myenv
    pip install -r requirements.txt
```

### 3. Configure Web App (Flask)
- Go to the **Web** tab and add a **new Flask app**.
- Modify `wsgi.py`:
```python
import sys
import os
from Data_Inserting import app

sys.path.insert(0, os.path.dirname(__file__))
application = app
```
- Restart the web app.

### 4. Schedule Auto Posting
- Go to the **Tasks** tab in PythonAnywhere.
- Add a scheduled task:
```bash
    workon myenv && python auto_posting.py
```
- Set the interval (e.g., every hour).

## License
This project is open-source and available under the MIT License.

## Author
Developed by [Ethical Dilkhush](https://github.com/ethical-dilkhush)

