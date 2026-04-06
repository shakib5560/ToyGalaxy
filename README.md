<div align="center">
  <h1>🧸 ToyGalaxy 🌌</h1>
  <p><strong>A magical, full-fledged toy store bringing joy to every click!</strong></p>
  
  [![Live Demo](https://img.shields.io/badge/Live_Demo-Visit_ToyGalaxy-FF5722?style=for-the-badge&logo=rocket)](https://www.toygalaxy.com.au/)
  [![Django](https://img.shields.io/badge/Django-6.0.3-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
  [![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
  
  <p>
    Browse, shop, review, and blog — all in one smooth web experience. <br>
    Built following Django's best practices with a stunning traditional server-rendered approach.
  </p>
</div>

---

## 🚀 Live Environment

We are live! Hop onto your spaceship and explore the galaxy of toys here:  
👉 **[www.toygalaxy.com.au](https://www.toygalaxy.com.au/)**

---

## 📋 Table of Contents
- [About](#-about-the-project)
- [Stellar Features](#-stellar-features)
- [Project Architecture](#-project-architecture)
- [Tech Stack & Dependencies](#-tech-stack--dependencies)
- [Blast Off (Installation)](#-blast-off-installation-guide)
- [Screenshots](#-visual-journey)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 About the Project

**ToyGalaxy** isn't just an e-commerce platform; it's an experience. Focused on selling the latest and greatest toys, it features robust user accounts, engaging blog articles, authentic product reviews, and a seamless cart management system.  
Everything is built natively with robust **Django** templates, views, and ORM — keeping the stack elegant, fast, and powerfully simple.

---

## ✨ Stellar Features

- 🛒 **Galactic Product Catalog** – Seamlessly add, update, and manage toys.
- 📝 **Honest User Reviews** – Shoppers can drop their thoughts and rate products.
- 🔐 **Fort Knox Authentication** – Secure registration, login, logout, and profile management.
- 📰 **Parenting & Toy Blogs** – Publish and read the most captivating toy stories.
- 🎨 **Beautiful UI/UX** – A highly responsive, mobile-ready interface styled with modern CSS/SCSS.
- 🛠️ **Command Center Admin** – A fully equipped, custom-themed admin dashboard powered by `django-jazzmin`.
- 🗂️ **Rich Text Editing** – Integrated `django-ckeditor` for crafting beautiful blog posts and descriptions.

---

## 🗂 Project Architecture

```raw
ToyGalaxy/
│
├── a_users/           # 🧑‍🚀 User authentication & profile handling
├── blogs/             # 📰 Blog application for reviews & news
├── core/              # ⚙️ Core settings and global utilities
├── ecommerch/         # 🛍️ E-commerce engine (catalog, cart)
├── productshandler/   # ⭐ Product reviews and dynamic ratings
├── static/ & media/   # 🎨 CSS, JS, and product imagery
└── templates/         # 🖼️ Stunning HTML templates
```

---

## 💻 Tech Stack & Dependencies

The project relies on a carefully curated selection of libraries and tools:

- **Backend:** Django (v6.0.3)
- **Frontend:** Django Templates, HTML5, CSS3, SCSS
- **Database:** SQLite3 (development environment ready)

### 📦 Installed Packages (`requirements.txt`)
All the magical ingredients making ToyGalaxy possible:

```text
asgiref==3.11.1
bleach==6.3.0
certifi==2026.2.25
charset-normalizer==3.4.7
Django==6.0.3
django-ckeditor==6.7.3
django-ckeditor-5==0.2.20
django-jazzmin==3.0.4
django-js-asset==3.1.2
django-requests==0.0.2
django-shortuuid==0.1.2
django-summernote==0.8.20.0
idna==3.11
pillow==12.2.0
requests==2.33.1
shortuuid==1.0.13
sqlparse==0.5.5
urllib3==2.6.3
uv==0.11.3
webencodings==0.5.1
```

---

## 🚀 Blast Off! (Installation Guide)

Ready to launch ToyGalaxy locally? Follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/shakib5560/ToyGalaxy.git
cd ToyGalaxy
```

### 2. Ignite a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the essentials
```bash
pip install -r requirements.txt
```

### 4. Setup the database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create mission control (Admin Access)
```bash
python manage.py createsuperuser
```

### 6. Lift off! 🛸
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to explore your galaxy.

---

## 🖼️ Visual Journey

A quick sneak peek at what's waiting for you!

| Home Universe | Toy Details | The Blogosphere |
|:---------:|:---------------:|:----:|
| ![Home Page](https://i.ibb.co/GQcChkh7/Screenshot-from-2025-04-28-08-04-59.png) | ![Product Details](https://i.ibb.co/4nyZwz35/Screenshot-from-2025-04-28-08-05-30.png) | ![Blog](https://i.ibb.co/q3R6Kd6g/Screenshot-from-2025-04-28-08-05-58.png) |

---

## 🤝 Contributing

We love explorers joining our mission! 🛸 

1. **Fork** the repository
2. Create your **Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the Branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

Let's make ToyGalaxy the best place in the universe!

---

## 📜 License

This project is generously licensed under the MIT License.  
See the [LICENSE](LICENSE) file for more information.

---

<div align="center">
  <p>Built with 🛠️ and ❤️ by <a href="https://github.com/shakib5560">Shakib</a></p>
</div>
