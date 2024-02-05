# Selenium Test Automation Framework

This Selenium-based test automation framework, written in Python, is designed to automate test [scenarios](https://automationexercise.com/test_cases) for the demo site provided by automationexercise.com., powered by Python, with running tests in a docker container and publishing generated test reports on github pages

## Running the Project Locally

### Prerequisites

- **With Docker:** Docker installed on your machine.
- **Without Docker:** Python installed on your machine.

### Instructions

#### Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### Running Tests with Docker

#### Build Docker Image

```bash
docker-compose build
```

#### Run Tests

```bash
docker-compose up
```

This will execute the test suite inside a Docker container. The test reports will be generated in the reports directory.

### Running Tests Without Docker

#### Make changes to the conftest.py file according to the description provided inside the file

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Run Tests

```bash
pytest -sv --alluredir=allure-results --reruns 2
```

This will execute the test suite locally. The test reports will be generated in the allure-results directory.

### Viewing Test Reports

**With Docker:**

1.After running the tests with Docker, navigate to the project directory.

2.Open a terminal and run:

```bash
allure serve reports
```

3.This will open a browser window showing the test reports with a history of launches.

**Without Docker:**

1.After running the tests without Docker, navigate to the project directory.

2.Open a terminal and run:

```bash
allure serve allure-results
```

3.This will open a browser window showing the test reports with a history of launches.

Feel free to customize and enhance the framework based on your requirements!

## Work on the project is in progress

The basic structure for test implementation has been written.
27 out of 26 automated tests have been developed, I'm planning to add a few more test cases that will cover some certain features.

![Progress](https://progress-bar.dev/90/?title=done)

## List of tested features

### User Management

- User Authentication:
  - [x] User Registration (Test Case 1, Test Case 5)
  - [x] User Login (Test Case 2, Test Case 3)
  - [x] User Logout (Test Case 4)

### Customer Support

- [x] Contact Us Form (Test Case 6)

### Interface & Navigation

- [x] Verify Test Cases Page (Test Case 7)
- Scroll Functionality:
  - [x] Verify Scroll Up & Down Functionality with 'Arrow' Button (Test Case 25)
  - [x] Verify Scroll Up & Down Functionality without 'Arrow' Button (Test Case 26)

### Product Management

- Product Display & Information:
  - [x] Verify All Products and Product Detail Page (Test Case 8)
  - [x] View Category Products (Test Case 18)
  - [x] View & Cart Brand Products (Test Case 19)
  - [x] Search Product (Test Case 9)
- Cart & Wishlist:
  - [x] Add Products in Cart (Test Case 12)
  - [x] Verify Product Quantity in Cart (Test Case 13)
  - [x] Remove Products From Cart (Test Case 17)
  - [x] Add Review on Product (Test Case 21)
  - [x] Add to Cart from Recommended Items (Test Case 22)

### Shopping & Checkout

- Subscription Handling:
  - [x] Verify Subscription in Home Page (Test Case 10)
  - [x] Verify Subscription in Cart Page (Test Case 11)
- Checkout Process:
  - [x] Place Order: Register While Checkout (Test Case 14)
  - [x] Place Order: Register Before Checkout (Test Case 15)
  - [x] Place Order: Login Before Checkout (Test Case 16)
  - [x] Verify Address Details in Checkout Page (Test Case 23)
  - [x] Download Invoice After Purchase Order (Test Case 24)
  - [x] Search Products and Verify Cart After Login (Test Case 20)
