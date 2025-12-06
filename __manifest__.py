# vues/manifest.py
{
    "name": "Gestion de Contacts",
    "summary": "Module simple pour gérer des contacts",
    "description": "Permet d'ajouter, modifier et supprimer des contacts via des vues liste et formulaire.",
    "version": "1.0.0",
    "category": "Tools",
    "author": "askri med dhia",
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/contact_views.xml",
        "report/contact_report_templates.xml",
    ],
    "demo": [
        "demo/demo_data.xml",
    ],
    "installable": True,
    "application": True,
}
