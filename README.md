# mon_module (Odoo 18)

Ce dépôt contient un module Odoo minimal nommé `mon_module` exposant une API REST pour gérer des contacts.

## Description
This Odoo module provides a simple yet effective way to manage contacts within your Odoo instance. It allows for the creation, modification, and deletion of contacts, along with categorization and reporting capabilities. Additionally, it exposes a REST API for external integration.

## Features
*   **Contact Management**: comprehensive CRUD (Create, Read, Update, Delete) operations for contacts.
*   **Categorization**: Organize contacts into different categories.
*   **Relations**: Link contacts to other related contacts.
*   **Reporting**: Generate PDF reports for selected contacts.
*   **REST API**: Fully functional API for external access and management of contacts.

## Installation
1.  Clone this repository into your Odoo addons directory:
    ```bash
    git clone https://github.com/meduk0/module-odoo-18.git mon_module
    ```
2.  Update your Odoo configuration file (`odoo.conf`) to include the path to the directory containing this module.
3.  Restart your Odoo server.
4.  Log in to Odoo as an administrator.
5.  Go to **Apps**, search for "Gestion de Contacts" (or `mon_module`), and click **Install**.

## Usage
### Web Interface
*   Navigate to the **Contacts** menu (or the specific menu item created by this module).
*   Use the **Create** button to add a new contact.
*   Fill in the details such as Name, Email, Phone, Address, and Category.
*   Use the **Print** menu to generate reports for selected contacts.

**Arborescence du projet**

```
`__init__.py`                # Initialisation du package Python pour le module Odoo
`__manifest__.py`            # Métadonnées du module (nom, version, dépendances, données)
`api_test_script.py`         # Script Python exemple pour tester l'API REST (utilise requests)
`README.md`                  # Ce fichier
`controllers/`               # Contrôleurs HTTP exposant les endpoints de l'API
    `__init__.py`            # Initialisation du package controllers
    `main.py`               # Définition des routes HTTP (voir Endpoints)
`demo/`                      # Données de démonstration à charger (XML)
    `demo_data.xml`         # Exemple de données démo
`models/`                    # Définitions des modèles Odoo (ORM)
    `__init__.py`
    `contact.py`            # Modèle `mon_module.contact` (champs et logique métier)
    `contact_report.py`     # Logique du rapport (génération de rapports liés aux contacts)
`report/`
    `contact_report_templates.xml` # Template QWeb pour rapports PDF/HTML
`security/`
    `ir.model.access.csv`   # Règles d'accès et droits pour les modèles
`views/`
    `contact_views.xml`    # Vues XML (form, tree) pour l'interface Odoo
```

Notes:
- Les fichiers `*.py` contiennent la logique côté serveur. Les fichiers XML (dans `views/`, `report/`, `demo/`, `security/`) sont des données/ressources Odoo chargées par le module.

**Endpoints disponibles**

Tous les endpoints sont définis dans `controllers/main.py`. Ils exposent une API JSON publique (auth=`public`, `csrf=False`) destinée à être utilisée dans un environnement contrôlé. Voici la liste et des exemples d'utilisation :

- GET /api/contacts
  - Description : Récupère la liste de tous les contacts.
  - Méthode : `GET`
  - Auth : `public`
  - Exemple :
    - Request : `GET http://<host>:8069/api/contacts`
    - Response (200) :
      ```json
      {"status": "success", "data": [{"id":1, "name":"Alice", "email":"a@x.com", "phone":"...", "category": null}, ...]}
      ```

- GET /api/contact/<int:contact_id>
  - Description : Récupère les détails d'un contact par son ID.
  - Méthode : `GET`
  - Exemple : `GET http://<host>:8069/api/contact/5`
  - Responses :
    - 200 : `{ "status": "success", "data": { ... } }`
    - 404 : `{ "status": "error", "message": "Contact not found" }`

- POST /api/contact/create
  - Description : Crée un contact.
  - Méthode : `POST`
  - Payload JSON attendu :
    ```json
    {
      "name": "Nom",
      "email": "ex@example.com",    # optionnel
      "phone": "+33123456789",      # optionnel
      "category_id": 3               # optionnel, id d'une catégorie existante
    }
    ```
  - Exemple : `POST http://<host>:8069/api/contact/create` avec Content-Type: application/json
  - Response (success) : `{ "status": "success", "message": "Contact created", "id": 42 }`

- PUT/POST /api/contact/update/<int:contact_id>
  - Description : Met à jour un contact existant. Accepte `PUT` et `POST` pour compatibilité.
  - Méthode : `PUT` (ou `POST`)
  - Payload : JSON partiel ou complet. Ex : `{ "name": "Nouveau nom" }`
  - Response: `{ "status": "success", "message": "Contact updated" }`

- DELETE/POST /api/contact/delete/<int:contact_id>
  - Description : Supprime un contact.
  - Méthode : `DELETE` (ou `POST`)
  - Response: `{ "status": "success", "message": "Contact deleted" }`

Sécurité et mise en garde :
- Les routes sont exposées en `auth='public'` et `csrf=False`. Cela facilite les tests mais n'est pas sécurisé pour une API publique sans authentification/autorisation. En production, protégez les routes (par ex. `auth='user'` ou un système de token).

Exemples de test
- Un script d'exemple `api_test_script.py` est fourni (il utilise la librairie `requests`). Pour l'exécuter :

```sh
# installer requests si nécessaire (préférer un venv)
python -m pip install requests
python api_test_script.py
```

Installation du module dans Odoo

1. Copier le dossier `mon_module` dans le répertoire `addons` d'Odoo (ou ajouter son chemin dans `addons_path`).
2. Redémarrer le serveur Odoo : `./odoo-bin -c <config>` ou via votre gestionnaire de services.
3. Depuis l'interface Odoo, aller dans Apps, cliquer sur "Update Apps List" puis rechercher "mon_module" et l'installer.

Développement local
- Pour développer, activez le mode développeur dans Odoo pour voir les vues, champs et accéder aux logs.
- Les logs Odoo vous aideront à déboguer : surveillez le terminal où tourne Odoo.

Tests
- `api_test_script.py` montre un flux basique : list, create, read, update, delete.

### API Documentation
The module exposes the following endpoints for external integration. All endpoints return JSON responses.

#### 1. List All Contacts
*   **URL**: `/api/contacts`
*   **Method**: `GET`
*   **Response**:
    ```json
    {
      "status": "success",
      "data": [
        {
          "id": 1,
          "name": "John Doe",
          "email": "john@example.com",
          "phone": "123456789",
          "category": "Customer"
        },
        ...
      ]
    }
    ```

#### 2. Get Contact Details
*   **URL**: `/api/contact/<contact_id>`
*   **Method**: `GET`
*   **Response**:
    ```json
    {
      "status": "success",
      "data": {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "123456789",
        "category": "Customer"
      }
    }
    ```

#### 3. Create Contact
*   **URL**: `/api/contact/create`
*   **Method**: `POST`
*   **Body** (JSON):
    ```json
    {
      "name": "Jane Doe",
      "email": "jane@example.com",
      "phone": "987654321",
      "category_id": 1
    }
    ```
*   **Response**:
    ```json
    {
      "status": "success",
      "message": "Contact created",
      "id": 2
    }
    ```

#### 4. Update Contact
*   **URL**: `/api/contact/update/<contact_id>`
*   **Method**: `PUT` or `POST`
*   **Body** (JSON):
    ```json
    {
      "email": "newemail@example.com"
    }
    ```
*   **Response**:
    ```json
    {
      "status": "success",
      "message": "Contact updated"
    }
    ```

#### 5. Delete Contact
*   **URL**: `/api/contact/delete/<contact_id>`
*   **Method**: `DELETE` or `POST`
*   **Response**:
    ```json
    {
      "status": "success",
      "message": "Contact deleted"
    }
    ```

## Author
*   **meduk0**

## License
This module is available under the Odoo Proprietary License.
