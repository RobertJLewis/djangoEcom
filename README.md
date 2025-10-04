
# 🌾 Millets & Grains E-commerce Store
## Introduction

**Project Milestone 3:** Code Institute Full-Stack Development Program: Django Framework  

This project is a Django-based e-commerce platform selling **millets and grains**. Users can browse products, add items to a shopping cart, and complete secure checkouts.  

The **admin panel** allows full product management: adding, editing, updating prices, and managing stock.  

---

## Table of Contents

- [Introduction](#introduction)  
- [Project Goals](#project-goals)  
- [Target Audience](#target-audience)  
- [Key Features](#key-features)  
- [Database Schema](#database-schema)  
- [Website Pages](#website-pages)  
- [Development Process](#development-process)  
- [Future Implementations](#future-implementations)  
- [Accessibility](#accessibility)  
- [Deployment & Local Development](#deployment--local-development)  
- [Technologies Used](#technologies-used)  
- [Acknowledgments](#acknowledgments)  

---

## Project Goals
- Provide a clean and user-friendly platform to purchase healthy grains  
- Enable a secure and seamless checkout process  
- Allow admin users to efficiently manage products, prices, and inventory  
- Deliver a responsive, mobile-friendly experience  

---

## Target Audience
- 🌾 Health-conscious consumers  
- 🛒 Online shoppers looking for nutritious grains  
- 🏢 Store administrators managing inventory and orders  

---

## Key Features
- Browse products by category and view details  
- Add/remove items to/from shopping cart  
- Secure checkout and payment process  
- Admin panel for product and inventory management  
- Fully responsive and mobile-friendly interface  
- Custom error pages (404 / 500)  

---

## Database Schema
The store uses **PostgreSQL** for structured and reliable storage.  

Key models include:

- `Product` – Name, description, category, price, stock, images  
- `Category` – Product grouping for easy browsing  
- `Order` – Tracks purchases, timestamps, payment status  
- `OrderItem` – Links individual products to orders  

---

## Website Pages
- **Home Page** – Displays featured and all products  
- **Product Detail Page** – Product images, description, and add-to-cart button  
- **Cart Page** – Review and update items  
- **Checkout Page** – Complete orders securely  
- **Login/Register Pages** – Required for checkout and order confirmations  
- **Admin Panel** – Manage products, prices, stock, and categories  

---

## Development Process
- Iterative, feature-driven development using Django & PostgreSQL  
- Responsive design using Bootstrap 5  
- Admin product management via Django admin panel  
- Version control with Git & GitHub  

---

## Future Implementations
- Wishlist/favourites  
- Product reviews and ratings  
- Multi-currency support  
- Multiple payment gateway integration  
- Discount codes and promotions  

---

## Accessibility
- Semantic HTML5 elements for assistive technologies  
- Alt text for all meaningful images  
- ARIA labels for buttons, links, and forms  
- Full keyboard navigability and focus states  
- Lighthouse & WAVE accessibility testing  

---

## Deployment & Local Development
### Deployment
- Hosted on **Heroku**  
- PostgreSQL database on AWS RDS  
- Gunicorn and Whitenoise for production-ready serving  
- Environment variables for `SECRET_KEY`, `DEBUG`, and `DATABASE_URL`  


### Technologies Used
- Languages: Python, HTML, CSS, JavaScript
- Frameworks & Libraries: Django 4.x, Bootstrap 5, Crispy Forms
- Database: PostgreSQL
- Deployment: Heroku, Gunicorn, Whitenoise
- Design Tools: Adobe Illustrator & Photoshop, Google Fonts, Font Awesome


### Acknowledgments
Code Institute mentor for guidance and feedback
Fellow students for collaboration and testing
Friends and family for usability testing
