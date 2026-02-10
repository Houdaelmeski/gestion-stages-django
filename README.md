🎓 Système de Gestion des Stages

Application web dédiée à la centralisation et à l’automatisation de la gestion des stages au sein d’une organisation.

La plateforme permet de gérer les stagiaires, les encadrants, les périodes de stage ainsi que les documents associés à travers un système de rôles et un tableau de bord administratif.

📋 Présentation générale

Période de développement : Juillet 2024 – Août 2024
Type de projet : Application web de gestion des stages

L’application couvre l’ensemble du cycle de vie d’un stage, depuis l’intégration du stagiaire jusqu’au suivi administratif, avec un système d’accès multi-rôles.

✨ Fonctionnalités principales
👥 Gestion des utilisateurs

Système multi-rôles : Administrateur, Encadrant, Stagiaire

Authentification sécurisée et gestion des sessions

Gestion des permissions basée sur les rôles (RBAC)

Profils utilisateurs personnalisés

📊 Gestion des stages

Création et suivi des stages avec gestion des statuts

Affectation des encadrants aux stagiaires

Gestion des périodes et plannings de stage

Historique et traçabilité des actions

📁 Gestion documentaire

Téléversement sécurisé des documents liés au stage :

CV et lettre de motivation

Convention de stage

Rapports de stage

Attestation d’assurance

Autres documents justificatifs

Organisation et validation des documents

🔍 Recherche et consultation

Recherche avancée multi-critères

Filtres dynamiques (période, encadrant, statut)

Export des données (Excel / PDF)

Synthèses et rapports analytiques

📈 Tableau de bord administratif

Vue d’ensemble de l’activité

Indicateurs clés de suivi

Graphiques et visualisations interactives

Notifications et alertes

🛠️ Technologies utilisées
Backend

Django – Framework web Python

Django ORM – Gestion de la base de données

Système d’authentification Django

Frontend

HTML5 / CSS3

JavaScript

Bootstrap – Interface responsive

Base de données

SQLite (environnement de développement)

PostgreSQL (environnement de production)

Conception

UML – Diagrammes de cas d’utilisation, classes et séquences

Merise – Modélisation relationnelle

📁 Structure du projet
project-root/
│
├── core/                      # Application principale
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── decorators.py
│
├── config/                    # Configuration du projet
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
├── manage.py
├── .gitignore
└── README.md

🚀 Installation et configuration
Prérequis

Python 3.8 ou plus

pip

Git

Installation
git clone https://github.com/votre-username/votre-repo.git
cd votre-repo

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux / Mac

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


L’application est accessible à l’adresse : http://localhost:8000

🔐 Sécurité

Authentification requise pour les pages protégées

Gestion des accès par rôles

Protection CSRF

Validation des fichiers téléversés (type et taille)

Hashage sécurisé des mots de passe

Nettoyage des entrées utilisateur

📊 Modèle de données (entités principales)

User – Utilisateurs du système

Stagiaire – Profils des stagiaires

Encadrant – Profils des encadrants

Stage – Informations des stages

Document – Documents associés

Affectation – Relations stagiaire–encadrant

📝 Licence

Projet développé dans le cadre d’un projet académique.

👩‍💻 Auteur

Houda El Meski
Étudiante ingénieure en informatique

GitHub : @HoudaElmeski

LinkedIn : Houda El MESKI
