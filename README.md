# 🧸 ToyGalaxy

Welcome to **ToyGalaxy** — a full-fledged toy store built with **Django**! 🚀  
Browse, shop, review, and blog — all in one smooth web experience.  
Built following Django's best practices with a traditional server-rendered approach (no frontend framework).

---

## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 About

**ToyGalaxy** is an e-commerce platform focused on selling toys, featuring user accounts, blog articles, product reviews, and a cart management system.  
Built purely with Django templates, views, and ORM — keeping the stack simple yet powerful.

---

## ✨ Features
- 🛒 **Product Management** – Add, update, and delete toys (admin only).
- 📝 **User Reviews** – Customers can leave reviews for products.
- 🔐 **User Authentication** – Register, login, logout.
- 📰 **Blog System** – Publish blogs related to toys and parenting.
- 📂 **Media Handling** – Upload product images.
- 🛠️ **Admin Dashboard** – Manage products, blogs, and users.
- 📱 **Responsive Templates** – Clean mobile-friendly UI with CSS and SCSS.

---

## 🛠️ Tech Stack

- **Backend:** Django
- **Frontend:** Django Templates, HTML5, CSS3, SCSS
- **Database:** SQLite3 (for development)
- **Others:** 
  - Django Messages Framework (for alerts)
  - Django Admin
  - Static/media file handling

---

## 🗂 Project Structure

```
ToyGalaxy/
│
├── a_users/           # User authentication and profile handling
├── blogs/             # Blog application
├── core/              # Core settings and utilities
├── ecommerch/         # Ecommerce application (product catalog, cart, etc.)
├── productshandler/   # Product reviews and ratings
├── media/             # Uploaded images (product images)
├── static/assets/     # Static files (CSS, JS, images)
├── templates/         # HTML templates
│
├── db.sqlite3         # Development database
├── manage.py          # Django management script
└── README.md          # Project documentation
```

---

## 🚀 Installation

Follow these simple steps to set up ToyGalaxy locally:

### 1. Clone the repository

```bash
git clone https://github.com/shakib5560/ToyGalaxy.git
cd ToyGalaxy
```

### 2. Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

*(If `requirements.txt` is missing, use `pip freeze > requirements.txt` to generate one.)*

### 4. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see ToyGalaxy in action!

---

## 🖼️ Screenshots

> (Insert screenshots here — you can show Home Page, Product Page, Cart Page, Blog Page, etc.)

| Home Page | Product Details | Blog |
|:---------:|:---------------:|:----:|
| ![Home Page](https://i.ibb.co/GQcChkh7/Screenshot-from-2025-04-28-08-04-59.png) | ![Product Details](https://i.ibb.co/4nyZwz35/Screenshot-from-2025-04-28-08-05-30.png) | ![Blog](https://i.ibb.co/q3R6Kd6g/Screenshot-from-2025-04-28-08-05-58.png) |

---

## 🤝 Contributing

Contributions are welcome! 🚀

- Fork the repository
- Create a feature branch
- Make your changes
- Submit a pull request

Let's make ToyGalaxy even better together!

---

## 📜 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

> Built with 🛠 and ❤️ by [Shakib](https://github.com/shakib5560)

---
