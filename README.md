<div align="center">
 
<img src="https://readme-typing-svg.demolab.com?font=Syne&weight=800&size=60&duration=2000&pause=800&color=A78BFA&center=true&vCenter=true&width=600&height=80&lines=🧸+ToyGalaxy;🌌+Explore+the+Galaxy;🚀+Shop.+Review.+Blog." alt="ToyGalaxy" />
 
<br/>
 
**A magical, full-fledged toy store bringing joy to every single click.**
 
<br/>
 
[![Live Demo](https://img.shields.io/badge/🚀%20LIVE-www.toygalaxy.com.au-FF4D6D?style=for-the-badge&logoColor=white)](https://www.toygalaxy.com.au/)
&nbsp;
[![Django](https://img.shields.io/badge/Django-6.0.3-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
&nbsp;
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
&nbsp;
[![License](https://img.shields.io/badge/License-MIT-A78BFA?style=for-the-badge)](LICENSE)
 
<br/>
 
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
 
</div>
 
<br/>
 
## 🌟 &nbsp; What is ToyGalaxy?
 
> **ToyGalaxy isn't just an e-commerce platform — it's an experience.**
 
Focused on selling the latest and greatest toys, ToyGalaxy features robust user accounts, engaging blog articles, authentic product reviews, and a seamless cart management system — all built natively with Django's powerful template system, views, and ORM.
 
<br/>
 
<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
</div>
 
<br/>
 
## ✨ &nbsp; Stellar Features
 
<table>
<tr>
<td width="50%">
 
### 🛒 &nbsp; Galactic Product Catalog
Seamlessly add, update, and manage toys across the entire storefront.
 
### 📝 &nbsp; Honest User Reviews
Shoppers drop real thoughts and ratings. Authentic. Unfiltered. Trusted.
 
### 🔐 &nbsp; Fort Knox Authentication
Secure registration, login, logout, and full profile management.
 
</td>
<td width="50%">
 
### 📰 &nbsp; Parenting & Toy Blogs
Publish and read the most captivating toy stories with rich CKEditor support.
 
### 🎨 &nbsp; Beautiful UI / UX
Highly responsive, mobile-ready interface styled with modern CSS and SCSS.
 
### 🛠️ &nbsp; Command Center Admin
Custom-themed admin dashboard powered by `django-jazzmin`.
 
</td>
</tr>
</table>
 
<br/>
 
<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
</div>
 
<br/>
 
## 🗂️ &nbsp; Project Architecture
 
```
🌌 ToyGalaxy/
│
├── 🧑‍🚀  a_users/           → User authentication & profile handling
├── 📰  blogs/             → Blog app for reviews & space news
├── ⚙️   core/              → Core settings and global utilities
├── 🛍️   ecommerch/         → E-commerce engine (catalog, cart)
├── ⭐  productshandler/   → Product reviews & dynamic ratings
├── 🎨  static/ & media/   → CSS, JS, and product imagery
└── 🖼️   templates/         → Stunning HTML templates
```
 
<br/>
 
<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
</div>
 
<br/>
 
## 💻 &nbsp; Tech Stack
 
<div align="center">
 
| Layer | Technology |
|:---:|:---:|
| **Backend** | ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![SASS](https://img.shields.io/badge/SCSS-CC6699?style=flat-square&logo=sass&logoColor=white) |
| **Database** | ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white) |
| **Admin** | ![Jazzmin](https://img.shields.io/badge/django--jazzmin-3.0.4-FF4D6D?style=flat-square) |
| **Media** | ![Pillow](https://img.shields.io/badge/Pillow-12.2.0-34D399?style=flat-square) |
 
</div>
 
<br/>
 
<details>
<summary><b>📦 &nbsp; Full requirements.txt</b> &nbsp; (click to expand)</summary>
 
<br/>
 
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
 
</details>
 
<br/>
 
<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
</div>
 
<br/>
 
## 🚀 &nbsp; Blast Off! — Installation Guide
 
<br/>
 
**Step 1 — Clone the repository**
```bash
git clone https://github.com/shakib5560/ToyGalaxy.git
cd ToyGalaxy
```
 
**Step 2 — Ignite a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```
 
**Step 3 — Install the essentials**
```bash
pip install -r requirements.txt
```
 
**Step 4 — Set up the database**
```bash
python manage.py makemigrations
python manage.py migrate
```
 
**Step 5 — Create mission control (Admin Access)**
```bash
python manage.py createsuperuser
```
 
**Step 6 — 🛸 Lift off!**
```bash
python manage.py runserver
```
 
> Visit **`http://127.0.0.1:8000/`** to explore your galaxy. 🌌
 
<br/>
 
<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
</div>
 
<br/>
 
## 🤝 &nbsp; Contributing
 
We love explorers joining our mission! 🛸
 
| Step | Action |
|:---:|:---|
| 1️⃣ | **Fork** the repository |
| 2️⃣ | Create your **Feature Branch** — `git checkout -b feature/AmazingFeature` |
| 3️⃣ | **Commit** your changes — `git commit -m 'Add AmazingFeature'` |
| 4️⃣ | **Push** to the branch — `git push origin feature/AmazingFeature` |
| 5️⃣ | Open a **Pull Request** and we'll review it fast! |
 
Let's make ToyGalaxy the best place in the universe. Together. 🌟
 
<br/>
 
<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
</div>
 
<br/>
 
## 📜 &nbsp; License
 
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
 
<br/>
 
<div align="center">
 
<img src="https://readme-typing-svg.demolab.com?font=Syne&weight=700&size=22&duration=3000&pause=1000&color=A78BFA&center=true&vCenter=true&width=500&height=50&lines=Built+with+🛠️+and+❤️+by+Shakib;Made+for+the+universe+🌌;Star+the+repo+if+you+love+it+⭐" alt="footer" />
 
[![GitHub](https://img.shields.io/badge/GitHub-shakib5560-181717?style=for-the-badge&logo=github)](https://github.com/shakib5560)
&nbsp;
[![Star](https://img.shields.io/github/stars/shakib5560/ToyGalaxy?style=for-the-badge&color=FF9900&logo=star)](https://github.com/shakib5560/ToyGalaxy/stargazers)
 
</div>
 