# Gestion de Contacts (mon_module)

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
*   **askri med dhia**

## License
This module is available under the Odoo Proprietary License.
