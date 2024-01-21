# automationexercise-python-ui

Implementation of automation of test [scenarios](https://automationexercise.com/test_cases) for the demo site, powered by Python Selenium, with running tests in a docker container and publishing generated test reports on github pages

## Work on the project is in progress

The basic structure for test implementation has been written.
9 out of 26 automated tests have been developed

![Progress](https://progress-bar.dev/33/?title=done)

## List of tested features 

### User Management:
   - User Authentication:
     - [x] User Registration (Test Case 1, Test Case 5)
     - [ ] User Login (Test Case 2, Test Case 3) - In Progress
     - [ ] User Logout (Test Case 4) - In Progress

### Customer Support:
   - [x] Contact Us Form (Test Case 6)

### Interface & Navigation:
   - [x] Verify Test Cases Page (Test Case 7)
   - Scroll Functionality:
     - [x] Verify Scroll Up & Down Functionality with 'Arrow' Button (Test Case 25)
     - [x] Verify Scroll Up & Down Functionality without 'Arrow' Button (Test Case 26)

### Product Management:
   - Product Display & Information:
     - [x] Verify All Products and Product Detail Page (Test Case 8)
     - [ ] View Category Products (Test Case 18) - In Progress
     - [ ] View & Cart Brand Products (Test Case 19) - In Progress
     - [x] Search Product (Test Case 9) 
   - Cart & Wishlist:
     - [x] Add Products in Cart (Test Case 12)
     - [x] Verify Product Quantity in Cart (Test Case 13)
     - [x] Remove Products From Cart (Test Case 17)
     - [x] Add Review on Product (Test Case 21)
     - [x] Add to Cart from Recommended Items (Test Case 22)

### Shopping & Checkout:
   - Subscription Handling:
     - [x] Verify Subscription in Home Page (Test Case 10)
     - [x] Verify Subscription in Cart Page (Test Case 11)
   - Checkout Process:
     - [ ] Place Order: Register While Checkout (Test Case 14) - Not Developed
     - [ ] Place Order: Register Before Checkout (Test Case 15) - Not Developed
     - [ ] Place Order: Login Before Checkout (Test Case 16) - Not Developed
     - [ ] Verify Address Details in Checkout Page (Test Case 23) - Not Developed
     - [ ] Download Invoice After Purchase Order (Test Case 24) - Not Developed
     - [ ] Search Products and Verify Cart After Login (Test Case 20) - Not Developed

