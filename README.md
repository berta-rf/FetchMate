# FetchMate

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Python](https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white&style=plastic)
![JS](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=white&style=plastic)
![SQLite](https://img.shields.io/badge/SQLite-044a64?logo=sqlite&logoColor=white&style=plastic)
![SQLAlchemy](https://img.shields.io/badge/SQL%20Alchemy-778877?logo=sqlalchemy&logoColor=white&style=plastic)
![Playwright](https://img.shields.io/badge/Playwright-green?logo=playwright&logoColor=white&style=plastic)
![Unittest](https://img.shields.io/badge/Unittest-FF9900?logo=unittest&logoColor=white&style=plastic)
![Bootstrap](https://img.shields.io/badge/Bootstrap-712cf9?logo=bootstrap&logoColor=white&style=plastic)

## Table of Contents

- [About](#about)
  - [Meet the Developers](#meet-the-developers)
  - [Why FetchMate?](#why-fetchmate) 
  - [What is FetchMate All About?](#what-is-fetchmate-all-about)
- [Installation](#installation)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create and Activate a Virtual Environment (Optional)](#2-create-and-activate-a-virtual-environment-optional)
  - [3. Install Dependencies using requirements.txt](#3-install-dependencies-using-requirementstxt)
  - [4. Initialize the Database](#4-initialize-the-database)
  - [5. Obtain an API Key](#5-obtain-an-api-key)
  - [6. Run the App](#6-run-the-app)
- [Test](#test)
  - [Unit testing](#unit-testing)
  - [End-to-End testing](#end-to-end-testing)


## About

Welcome to FetchMate, your go-to platform for finding your perfect canine companion! Our mission at FetchMate is to help connect people with their ideal dog breeds, making the journey of welcoming a new furry friend into your home an exciting and tailored experience.

### Meet the Developers
FetchMate is the brainchild of a passionate team of developers who share a love for dogs and a commitment to helping potential dog owners find the best match for their lifestyle. With a blend of expertise in web development and a shared enthusiasm for canine companionship, we've come together to create a tool that simplifies the process of selecting the right dog breed.

#### Contributors
- [@Alison](https://github.com/AlisonEve)
- [@Bella](https://github.com/bellamcdermid)
- [@Berta](https://github.com/berta-rf)
- [@Juling](https://github.com/julingc)
- [@Xixian](https://github.com/XixianWei)
- [@Yingying](https://github.com/Heying778)

### Why FetchMate?
At FetchMate, we understand that choosing the perfect dog is about more than just appearance – it's about finding a companion that will thrive in your home based on your unique lifestyle and preferences. Our inspiration for creating FetchMate comes from the desire to offer a solution that goes beyond aesthetics. We believe that every dog owner deserves a four-legged friend that aligns with their needs, whether it's energy levels, size, grooming requirements, or temperament.

### What is FetchMate All About?
FetchMate offers an enjoyable and convenient online quiz that guides you in discovering the ideal dog breeds that match your individual lifestyle. Our user-friendly 5-minute quiz takes into consideration various aspects of your routine and preferences. Based on your responses, we analyze and recommend dog breeds that align with your requirements. From temperaments to energy levels, size, grooming needs, and more, we've got you covered.

The beauty of FetchMate is its flexibility – you can even retake the quiz if you wish to modify your responses and explore different breed options. Our goal is to provide the most comprehensive and intuitive dog breed finder tool on the web, ensuring that your journey to finding your new best friend is as seamless as possible.

We invite you to enjoy the FetchMate experience and embark on the journey of discovering the perfect furry companion that's tailored just for you. Your feedback is important to us, so feel free to reach out with any suggestions or ideas to enhance the FetchMate experience.

Woof-tastic regards,

The FetchMate Team 💚

## Installation

Follow these steps to set up and run the FetchMate Flask app:

### 1. Clone the Repository
Clone the FetchMate repository to your local machine:

```bash
git clone git@github.com:berta-rf/FetchMate.git
cd FetchMate
```
### 2. Create and Activate a Virtual Environment (Optional): 
You can create and activate a virtual environment if you want an isolated environment for your project. If you skip this step, the packages will be installed globally.
```bash
cd /path/to/your/FetchMate/src
python3 -m venv venv
```

#### Activate the virtual environment:
On macOS or Linux:
```bash
source venv/bin/activate
```

On Windows (Command Prompt):
```bash
venv\Scripts\activate
```

On Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies using requirements.txt:
```bash
pip install -r requirements.txt
```

### 4. Initialize the Database
Run the Python interpreter and create the necessary database tables:
```bash
python3
```
then
```bash
from app import db
db.create_all()
exit()
```

### 5. Obtain an API Key:
To use the features of this project, you need to obtain an API key from https://api-ninjas.com/api/dogs. Here's how:

- Sign up or log in to https://api-ninjas.com/api/dogs.
- Navigate to the API key generation section in your account dashboard.
- Generate a new API key and copy it.
- Open the config.py file in the src folder of your project. Add the API key you obtained in the previous step:
```python
API_KEY = "your_generated_api_key_here"
```

###  6. Run the App
Run the Flask app using the following command:

```bash
python3 app.py
```
or
```bash
python app.py
```

The app will be served at http://localhost:5001.


## Test
We take testing seriously at FetchMate to ensure the reliability and functionality of our application. We have a comprehensive suite of tests that cover different aspects of the system, including unit tests for core functionality and end-to-end tests to validate the user experience.

### Unit testing
To run unit tests for the utility functions in utils.py, follow these steps:

#### 1. Navigate to the Test Directory: 
Open a terminal and navigate to the root of the project, specifically the src folder where the tests are located.
```bash
cd path/to/src
```

#### 2. Run Unit Tests: 
Execute the following command to run the unit tests for the utility functions.
```bash
python -m unittest testing/test_utils_match_breeds.py
```

### End-to-End testing
We also perform end-to-end tests to validate the behavior of our Flask application in a real-world browser scenario. Here's how to run these tests:

#### 1. Install Playwright: 
In the terminal, run the following command to install Playwright.
```bash
playwright install
```

#### 2. Run End-to-End Tests: 
From the src folder, execute the following command to run the browser tests.
```bash
python -m pytest testing/test_web.py
```

Please note that the Flask app must be running for the end-to-end tests to work as expected.


