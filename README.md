
# 🌾 Millets & Grains E-commerce Store
## Introduction

**Project Milestone 4:** Code Institute Full-Stack Development Program: Django Framework  

This project is a Django-based **e-commerce platform focused on selling millets and grains**, developed as part of the Code Institute Full-Stack Development Program. The platform provides users with a seamless online shopping experience, allowing them to **browse products, view detailed information, add items to a shopping cart, and complete secure checkouts** using standard e-commerce flows.  

The application is designed with both **end-users and administrators in mind**. Customers benefit from a clean, intuitive interface with a responsive layout optimized for desktops, tablets, and mobile devices, ensuring they can shop conveniently from any device.  

For administrators, the **Django admin panel** offers robust product management capabilities. Admins can **add new products, edit existing listings, update prices, manage stock levels, and categorize items** effectively. This ensures that the platform remains up-to-date and efficient, providing a smooth and professional shopping experience.  

The project demonstrates practical application of Django concepts including **models, views, templates, user authentication, session management, and deployment to a live environment**. It also emphasizes best practices for e-commerce development such as **data security, responsive design, and accessibility**, making it a fully functional and production-ready platform.  

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

The primary goal of this project is to create a fully functional and **user-friendly e-commerce platform** that allows customers to conveniently purchase healthy grains and millets online. Specific objectives include:

- **Clean and intuitive interface:** Design a platform where users can easily browse, search, and filter products without confusion, making the shopping experience seamless and enjoyable.  
- **Secure and reliable checkout process:** Implement a checkout system that safeguards user information, supports smooth transactions, and reduces friction during payment and order confirmation.  
- **Efficient product management for admins:** Provide a powerful admin panel where administrators can quickly add new products, edit product information, update prices, manage stock levels, and categorize items for easy navigation.  
- **Responsive and mobile-friendly design:** Ensure the website adapts to all screen sizes, from desktops to smartphones, so users can shop comfortably from any device.  
- **Scalability and maintainability:** Structure the code and database to allow future expansion, including adding more products, features, or integrations like payment gateways and discounts.  

---

## Target Audience

The platform is designed to cater to a variety of users with different needs:  

- **🌾 Health-conscious consumers:** Individuals looking for nutritious, natural grains and millets to support a healthy lifestyle. They value quality, convenience, and a smooth online shopping experience.  
- **🛒 Online shoppers:** Customers who prefer the ease of browsing products online, adding items to a cart, and completing purchases from the comfort of their homes or on the go.  
- **🏢 Store administrators:** Users responsible for managing product listings, pricing, inventory, and categories. The admin panel provides them with the tools needed to maintain a well-organised, up-to-date store efficiently.  
- **📱 Mobile users:** Individuals accessing the platform via smartphones and tablets, who expect responsive design and smooth navigation without compromising functionality.  

---


## Key Features

This e-commerce platform is designed to provide a smooth and engaging shopping experience for customers while offering powerful tools for administrators. Key features include:

- **Browse Products by Category and View Details:**  
  Users can explore a wide range of millets and grains, sorted into categories for easy navigation. Each product includes detailed information such as description, price, stock availability, and images, helping customers make informed purchasing decisions.

- **Add/Remove Items to/from Shopping Cart:**  
  Customers can easily add products to a virtual shopping cart, update quantities, or remove items as needed. The cart provides a clear summary of selected items, prices, and total costs before proceeding to checkout.

- **Secure Checkout and Payment Process:**  
  The platform supports a secure and reliable checkout system, ensuring customer data and payment details are protected. Users can review their order, enter shipping information, and complete payment with confidence, reducing friction in the purchase process.

- **Admin Panel for Product and Inventory Management:**  
  Administrators have access to the Django admin interface, where they can efficiently manage all products. This includes adding new items, updating prices, editing descriptions, managing stock levels, and organizing products into categories. This ensures the store remains accurate, up-to-date, and easy to navigate for customers.

- **Fully Responsive and Mobile-Friendly Interface:**  
  The website is designed with a mobile-first approach, providing an optimal viewing experience across desktops, tablets, and smartphones. All pages, from browsing products to checkout, are fully responsive, ensuring smooth functionality and accessibility on any device.

- **Future Scalability:**  
  The platform has been developed with scalability in mind, making it easy to integrate additional features in the future, such as wishlists, product reviews, multi-currency support, or advanced filtering options.


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

The platform consists of a range of pages designed to provide a smooth shopping experience for customers while offering full management capabilities for administrators.

- **Home Page:**  
  Serves as the main landing page for visitors. It showcases featured products, promotions, and categories, allowing users to quickly find items of interest. The layout is clean and intuitive, making it easy to navigate between product categories and discover new grains and millets.
- **Product Detail Page:**  
  Displays comprehensive information for each product, including high-quality images, detailed descriptions, pricing, stock availability, and category tags. Users can add items to their shopping cart directly from this page, and view related products to encourage exploration and additional purchases.
- **Cart Page:**  
  Provides an overview of all items added to the shopping cart. Users can update quantities, remove products, and view the total cost before proceeding to checkout. This page ensures transparency and control over purchases, helping reduce cart abandonment.
- **Checkout Page:**  
  Enables users to securely complete their orders. Customers can enter shipping information, select payment methods, and review their order summary before confirming the purchase. The checkout process is designed to be simple, secure, and efficient.
- **Login/Register Pages:**  
  Required for order processing and account management. New users can create accounts, while returning users can log in to view order history, manage personal details, and quickly checkout. Authentication ensures security and a personalised shopping experience.
- **Admin Panel:**  
  Provides administrators with comprehensive management tools for the store. Admins can add new products, update existing listings, edit prices, manage stock levels, and organize products into categories. This ensures the store remains current, accurate, and easy to navigate for customers.
- **Optional Future Pages:**  
  Potential pages for future updates could include a Wishlist page, Product Reviews page, Promotions or Discounts page, and an Analytics Dashboard for admins to track sales and performance.

---

## Development Process

The development of this Django-based e-commerce store followed an **iterative, feature-driven approach**, ensuring that both functionality and user experience were prioritised at every stage.  

- **Iterative, Feature-Driven Development:**  
  The project was built incrementally, focusing on core features first, such as product browsing, cart functionality, and secure checkout. Additional enhancements, like responsive design and admin product management, were integrated in later iterations. This approach allowed continuous testing, feedback, and refinement throughout the development cycle.  

- **Django & PostgreSQL Integration:**  
  Django served as the primary backend framework, providing robust functionality for models, views, templates, and user authentication. PostgreSQL was used as the relational database to manage products, categories, orders, and order items, ensuring structured and reliable storage. Data models were carefully designed to maintain relationships and support future scalability.  

- **Responsive Design with Bootstrap 5:**  
  The front-end interface was developed using **Bootstrap 5**, providing a mobile-first, fully responsive layout. Pages, including product listings, product detail views, cart, and checkout, adapt seamlessly to various screen sizes and devices, offering users a smooth and consistent shopping experience.  

- **Admin Product Management via Django Admin Panel:**  
  The Django admin interface was customised to allow administrators to efficiently manage products, update prices, manage stock, and organise categories. This powerful backend functionality ensures that the store remains current and provides full control over inventory and product data.  

- **Version Control with Git & GitHub:**  
  Git was used for source control, enabling structured tracking of development progress, while GitHub served as the central repository for the project. Commits were made regularly with descriptive messages, ensuring a clear history of changes and allowing for collaboration and rollbacks when necessary.  

- **Testing and Debugging:**  
  Manual testing was conducted throughout development to verify functionality, responsiveness, and accessibility. Any bugs or inconsistencies were addressed iteratively, ensuring a polished final product. Browser dev tools and PostgreSQL queries were used to troubleshoot and optimise both front-end and back-end components.  

- **Deployment Workflow:**  
  The application was prepared for production deployment with **Gunicorn** and **Whitenoise** for serving the app and static files. Environment variables were securely configured for `SECRET_KEY`, `DEBUG`, and database credentials. The platform was deployed to **Heroku** with PostgreSQL on AWS RDS, following best practices for security and scalability.  

---

## Future Implementations
The e-commerce platform has been designed with scalability in mind, allowing for the addition of new features and enhancements in future iterations. Planned improvements include:

- **Wishlist / Favourites:**  
  Allow users to save products they are interested in for later, enabling a more personalised shopping experience and encouraging repeat visits.  
- **Product Reviews and Ratings:**  
  Enable customers to leave feedback on products, rate them, and read other user reviews. This builds trust and helps shoppers make informed decisions.  
- **Multi-Currency Support:**  
  Introduce functionality for international users, allowing prices to be displayed in different currencies and improving accessibility for a global audience.  
- **Multiple Payment Gateway Integration:**  
  Expand payment options by integrating popular gateways such as PayPal, Stripe, or Apple Pay, providing users with secure, flexible, and convenient payment methods.  
- **Discount Codes and Promotions:**  
  Implement coupon codes, seasonal discounts, and promotional offers to enhance marketing strategies, incentivise purchases, and boost customer engagement.  
- **Enhanced Admin Analytics:**  
  Provide dashboards with sales tracking, inventory insights, and order statistics to help administrators make data-driven decisions and improve store management.  
- **Advanced Filtering and Sorting:**  
  Allow users to filter products by price, category, popularity, or nutritional attributes, and sort results for faster discovery of desired items.  


---

## Accessibility
Ensuring accessibility was a key focus during the development of the e-commerce platform. The goal is to make the store usable for all visitors, including those with disabilities or assistive technologies. Key measures include:

- **Semantic HTML5 Elements:**  
  The platform uses proper semantic HTML tags (e.g., `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) to structure content meaningfully. This improves navigation for screen readers and enhances the overall accessibility of the site.
- **Alt Text for All Meaningful Images:**  
  All product images, icons, and illustrations include descriptive `alt` text. This ensures that users relying on screen readers can understand visual content, and improves SEO performance for the site.
- **ARIA Labels for Interactive Elements:**  
  Accessible Rich Internet Applications (ARIA) labels were added to buttons, links, forms, and icon-only controls to provide context for screen readers. This ensures that users understand the function of interactive elements.
- **Full Keyboard Navigability and Focus States:**  
  Users can navigate the entire website using a keyboard alone. Focus states are clearly visible on links, buttons, and form fields, providing a smooth and intuitive experience for users with mobility or vision impairments.
- **Responsive and Readable Design:**  
  Text sizes, contrast ratios, and button placements were designed to meet accessibility standards, making the interface clear and easy to use across all devices.
- **Accessibility Testing:**  
  The site was tested using **Lighthouse** and **WAVE** tools to identify potential issues and confirm compliance with accessibility best practices. Manual testing was also performed to ensure that forms, navigation, and checkout workflows are fully usable for all users.

These measures ensure that the platform is inclusive, user-friendly, and compliant with modern accessibility standards, providing a positive experience for all visitors.

---

## Deployment & Local Development

This section outlines how the e-commerce store is deployed to production and how it can be run locally for development purposes.  

### Deployment

The project is deployed on **Heroku**, providing a cloud-hosted platform that ensures the application is accessible online. Key deployment details include:

- **Hosting on Heroku:**  
  The Django application is deployed using Heroku’s cloud platform, allowing for easy scalability and reliable uptime.

- **PostgreSQL Database on AWS RDS:**  
  Production data is stored in a **PostgreSQL** database hosted on Amazon RDS. This provides a secure, scalable, and managed database solution. The `DATABASE_URL` environment variable stores the connection string securely.  

- **Production-Ready Serving:**  
  - **Gunicorn** is used as the WSGI HTTP server to serve the Django application efficiently in production.  
  - **Whitenoise** is configured to serve static files such as CSS, JavaScript, and images directly, reducing server load and improving performance.

- **Environment Variables:**  
  Sensitive information and configuration are managed via environment variables:  
  - `SECRET_KEY` – Stores Django’s secret key securely.  
  - `DEBUG` – Set to `False` in production to prevent exposure of sensitive data.  
  - `DATABASE_URL` – Connection string for the production PostgreSQL database.  

- **Deployment Workflow:**  
  1. Configure PostgreSQL on AWS RDS and obtain the connection URL.  
  2. Set up the Heroku app and link the GitHub repository.  
  3. Add environment variables (`SECRET_KEY`, `DEBUG`, `DATABASE_URL`) in Heroku settings.  
  4. Install production dependencies (Gunicorn, dj-database-url, psycopg2-binary, Whitenoise) and freeze them in `requirements.txt`.  
  5. Push the code to Heroku and run database migrations.  
  6. Test the live deployment to ensure the app, database, and static files are served correctly.  



### Local Development
To run the project locally for development or testing:  

    1. **Clone the Repository:**  
    ```bash
    git clone <repository-url>
    cd <project-directory>

    2. **Set Up a Virtual Environment:**  
        python3 -m venv env
        source env/bin/activate  # On Windows use `env\Scripts\activate`

    3. **Install Dependencies:**  
        pip install -r requirements.txt

    4. **Configure Environment Variables:**  
        SECRET_KEY='your-secret-key'
        DEBUG=True
        DATABASE_URL='your-local-database-url'

    5. **Apply Migrations:**  
        python manage.py migrate

    6. **Create a Superuser (Admin Account):**  
        python manage.py createsuperuser

    7. **Run the Development Server:**  
        python manage.py runserver

    8. **Access the Application:**  
        Open a web browser and navigate to http://127.0.0.1:8000 to view the store locally.




### Technologies Used
This project leverages a modern full-stack development stack, combining robust backend functionality, responsive front-end design, and cloud deployment tools.

- **Languages:**  
  - **Python** – Primary backend programming language used for Django development.  
  - **HTML5** – Structuring content and semantic markup for accessibility and SEO.  
  - **CSS3** – Styling and layout of web pages, including responsive design techniques.  
  - **JavaScript** – Enhancing interactivity and front-end behaviour, such as dynamic cart updates and form validations.

- **Frameworks & Libraries:**  
  - **Django 4.x** – High-level Python web framework providing MVC structure, user authentication, admin panel, and ORM for database management.  
  - **Bootstrap 5** – Front-end framework for responsive, mobile-first UI design with pre-built components and grid system.  
  - **Crispy Forms** – Enhances Django form rendering with Bootstrap integration for clean and user-friendly forms.

- **Database:**  
  - **PostgreSQL** – Relational database used to store products, categories, orders, and order items. Chosen for reliability, scalability, and strong data integrity.  

- **Deployment:**  
  - **Heroku** – Cloud hosting platform for deploying the Django application with automated build and scaling capabilities.  
  - **Gunicorn** – WSGI HTTP server serving the Django app in production.  
  - **Whitenoise** – Efficiently serves static files in production without relying on external storage or CDN.  

- **Design & Visual Tools:**  
  - **Adobe Illustrator** – Used to design logos, icons, and visual assets for a professional brand identity.  
  - **Adobe Photoshop** – Image editing, cropping, resizing, and optimisation for web performance.  
  - **Google Fonts** – Integrates modern, readable typography across all pages.  
  - **Font Awesome** – Icon library providing scalable vector icons for buttons, navigation, and UI elements.  

- **Version Control & Collaboration Tools:**  
  - **Git** – Version control system for tracking changes and managing the codebase.  
  - **GitHub** – Repository hosting, collaboration, and project management platform.  

- **Testing & Accessibility Tools:**  
  - **Lighthouse & WAVE** – Accessibility and performance testing tools to ensure the platform is user-friendly and compliant with modern standards.  
  - **Chrome DevTools** – Debugging, responsive design testing, and performance optimisation during development.  

- **Environment & Configuration Tools:**  
  - **Python-dotenv / Django-environ** – Manage environment variables securely for local and production deployments.  
  - **psycopg2-binary** – PostgreSQL adapter for connecting Django to the database.  



### Acknowledgments
I would like to express my sincere gratitude to the following individuals and groups for their support, guidance, and contributions throughout the development of this project:

- **Code Institute Mentor:**  
  Special thanks to my mentor for providing invaluable guidance, constructive feedback, and expert advice throughout the development process. Your insights helped shape the project and ensured adherence to best practices in full-stack web development.
- **Fellow Students:**  
  Appreciation goes to my peers at Code Institute for collaboration, brainstorming, and peer reviews. Their feedback on functionality, design, and usability was instrumental in improving the overall quality of the e-commerce platform.
- **Friends and Family:**  
  Heartfelt thanks to friends and family who tested the platform, provided honest feedback, and supported me during development. Your suggestions helped identify usability issues, improve the user experience, and ensure the site is intuitive and accessible for a wide audience.
- **Open Source and Community Resources:**  
  Recognition to the authors and contributors of the tools, frameworks, and libraries used in this project, including Django, Bootstrap, Crispy Forms, PostgreSQL, and Font Awesome. Your work enabled the creation of a functional, responsive, and accessible e-commerce platform.







---