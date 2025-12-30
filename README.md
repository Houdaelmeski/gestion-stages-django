
# 🎓 Système de Gestion des Stages

Application web de gestion complète des stages développée pour le **Ministère de l'Agriculture, de la Pêche Maritime, du Développement Rural et des Eaux et Forêts** (Maroc).

Cette solution permet de centraliser et automatiser la gestion des stages après admission des stagiaires, du suivi administratif jusqu'à l'évaluation finale.

---

## 📋 Vue d'ensemble

**Période de développement** : Juillet 2024 – Août 2024  
**Contexte** : Stage au Ministère de l'Agriculture, de la Pêche Maritime, du Développement Rural et des Eaux et Forêts

L'application couvre la gestion complète du cycle de vie d'un stage avec un système de rôles multi-niveaux et un tableau de bord administratif pour le suivi en temps réel.

---

## ✨ Fonctionnalités principales

### 👥 Gestion des utilisateurs
- **Trois types de rôles** : Administrateur, Encadrant, Stagiaire
- Authentification sécurisée et gestion des sessions
- Profils utilisateurs personnalisés avec permissions granulaires

### 📊 Gestion des stages
- Création et suivi des stages avec statuts (En cours, Terminé, Suspendu)
- Affectation automatique ou manuelle des encadrants aux stagiaires
- Calendrier et planning des stages
- Historique complet des modifications

### 📁 Gestion documentaire
- Téléversement sécurisé des documents :
  - CV et lettre de motivation
  - Convention de stage
  - Rapports de stage (intermédiaire et final)
  - Attestation d'assurance
  - Certificats et autres documents
- Stockage organisé et sécurisé
- Système de validation des documents

### 🔍 Recherche et consultation
- Recherche avancée par critères multiples
- Filtres dynamiques (période, encadrant, statut, département)
- Export des données en format Excel/PDF
- Statistiques et rapports analytiques

### 📈 Tableau de bord administratif
- Vue d'ensemble en temps réel
- Indicateurs clés de performance (KPI)
- Graphiques et visualisations
- Notifications et alertes

---

## 🛠️ Technologies utilisées

### Backend
- **Django 4.x** - Framework web Python
- **Django ORM** - Gestion de la base de données
- **Django Authentication** - Système d'authentification

### Frontend
- **HTML5 / CSS3** - Structure et design
- **JavaScript** - Interactivité
- **Bootstrap** (optionnel) - Framework CSS responsive

### Base de données
- **SQLite** - Développement
- **PostgreSQL** - Production (recommandé)

### Conception
- **UML** - Diagrammes de cas d'utilisation, classes et séquences
- **Merise** - Modélisation de la base de données

---

## 📁 Structure du projet

\`\`\`
stagiere1/
│
├── site1/                      # Application principale
│   ├── migrations/             # Migrations de base de données
│   ├── templates/              # Templates HTML
│   ├── admin.py               # Configuration admin Django
│   ├── models.py              # Modèles de données
│   ├── views.py               # Vues et logique métier
│   ├── forms.py               # Formulaires Django
│   ├── urls.py                # Routes URL
│   └── decorators.py          # Décorateurs personnalisés
│
├── stagiere1/                  # Configuration du projet
│   ├── settings.py            # Paramètres Django
│   ├── urls.py                # URLs principales
│   └── wsgi.py                # Configuration WSGI
│
├── static/                     # Fichiers statiques
│   ├── css/                   # Feuilles de style
│   ├── js/                    # Scripts JavaScript
│   └── img/                   # Images
│
├── profile/                    # Gestion des profils
│
├── manage.py                   # Script de gestion Django
├── .gitignore                 # Fichiers à ignorer
└── README.md                  # Ce fichier
\`\`\`

---

## 🚀 Installation et configuration

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Git

### Installation

\`\`\`bash
# 1. Cloner le dépôt
git clone https://github.com/Houdaelmeski/django-internship-management.git
cd django-internship-management

# 2. Créer un environnement virtuel
python -m venv venv

# 3. Activer l'environnement virtuel
# Windows :
venv\Scripts\activate
# Linux / Mac :
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Configurer les variables d'environnement
# Créer un fichier .env à la racine du projet
# SECRET_KEY=votre_clé_secrète
# DEBUG=True
# DATABASE_URL=sqlite:///db.sqlite3

# 6. Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# 7. Créer un superutilisateur
python manage.py createsuperuser

# 8. Collecter les fichiers statiques
python manage.py collectstatic

# 9. Lancer le serveur de développement
python manage.py runserver
\`\`\`

L'application sera accessible à l'adresse : **http://localhost:8000**

---

## 👤 Utilisation

### Accès administrateur
1. Connectez-vous à l'interface admin : http://localhost:8000/admin
2. Utilisez les identifiants du superutilisateur créé

### Création d'utilisateurs
1. L'administrateur crée les comptes encadrants et stagiaires
2. Les utilisateurs reçoivent leurs identifiants par email
3. Première connexion avec changement de mot de passe obligatoire

### Gestion d'un stage
1. L'administrateur crée un nouveau stage
2. Affecte un encadrant au stage
3. Le stagiaire téléverse ses documents
4. L'encadrant suit l'avancement
5. Validation et clôture du stage

---

## 🔐 Sécurité

- Authentification obligatoire pour toutes les pages sensibles
- Gestion des permissions par rôle (RBAC)
- Protection CSRF activée
- Validation des fichiers uploadés (type, taille)
- Sanitisation des entrées utilisateur
- Stockage sécurisé des mots de passe (hashage)

---

## 📊 Modèle de données

### Entités principales
- **User** : Utilisateurs du système (hérite de AbstractUser)
- **Stagiaire** : Informations des stagiaires
- **Encadrant** : Informations des encadrants
- **Stage** : Détails des stages
- **Document** : Documents associés aux stages
- **Affectation** : Relations encadrant-stagiaire

---



---

## 📝 Licence

Ce projet a été développé dans le cadre d'un stage au Ministère de l'Agriculture, de la Pêche Maritime, du Développement Rural et des Eaux et Forêts.

---

## 👨‍💻 Auteur

**Houda Elmeski**  
Étudiante en Ingénierie - École Marocaine des Sciences de l'Ingénieur

- GitHub : [@Houdaelmeski](https://github.com/Houdaelmeski)
- LinkedIn : Houda El MESKI

---

## 🙏 Remerciements

Je tiens à remercier le **Ministère de l'Agriculture, de la Pêche Maritime, du Développement Rural et des Eaux et Forêts** pour l'opportunité de réaliser ce projet et pour leur accompagnement tout au long du stage.

---

## 📞 Support

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur GitHub ou à me contacter directement.

---

**⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile sur GitHub !**
