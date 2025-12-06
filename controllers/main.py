import json
from odoo import http
from odoo.http import request, Response

class ContactController(http.Controller):
    @http.route('/api/contacts', type='http', auth='public', methods=['GET'], csrf=False)
    def get_contacts(self):
        contacts = request.env['mon_module.contact'].sudo().search([])
        data = []
        for contact in contacts:
            data.append({
                'id': contact.id,
                'name': contact.name,
                'email': contact.email,
                'phone': contact.phone,
                'category': contact.category_id.name if contact.category_id else None,
            })
        return request.make_response(
            json.dumps({'status': 'success', 'data': data}),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/contact/<int:contact_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_contact_details(self, contact_id):
        contact = request.env['mon_module.contact'].sudo().browse(contact_id)
        if not contact.exists():
            return request.make_response(
                json.dumps({'status': 'error', 'message': 'Contact not found'}),
                headers={'Content-Type': 'application/json'},
                status=404
            )
        
        data = {
            'id': contact.id,
            'name': contact.name,
            'email': contact.email,
            'phone': contact.phone,
            'category': contact.category_id.name if contact.category_id else None,
        }
        return request.make_response(
            json.dumps({'status': 'success', 'data': data}),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/contact/create', type='http', auth='public', methods=['POST'], csrf=False)
    def create_contact(self, **kwargs):
        try:
            data = json.loads(request.httprequest.data)
        except Exception:
            return request.make_response(
                json.dumps({'status': 'error', 'message': 'Invalid JSON'}),
                headers={'Content-Type': 'application/json'},
                status=400
            )

        if not data.get('name'):
            return request.make_response(
                json.dumps({'status': 'error', 'message': 'Name is required'}),
                headers={'Content-Type': 'application/json'},
                status=400
            )
        
        vals = {
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
        }
        
        if data.get('category_id'):
             vals['category_id'] = data.get('category_id')

        new_contact = request.env['mon_module.contact'].sudo().create(vals)
        return request.make_response(
            json.dumps({'status': 'success', 'message': 'Contact created', 'id': new_contact.id}),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/contact/update/<int:contact_id>', type='http', auth='public', methods=['PUT', 'POST'], csrf=False)
    def update_contact(self, contact_id, **kwargs):
        contact = request.env['mon_module.contact'].sudo().browse(contact_id)
        if not contact.exists():
            return request.make_response(
                json.dumps({'status': 'error', 'message': 'Contact not found'}),
                headers={'Content-Type': 'application/json'},
                status=404
            )
        
        try:
            data = json.loads(request.httprequest.data)
        except Exception:
            return request.make_response(
                json.dumps({'status': 'error', 'message': 'Invalid JSON'}),
                headers={'Content-Type': 'application/json'},
                status=400
            )

        vals = {}
        if 'name' in data: vals['name'] = data['name']
        if 'email' in data: vals['email'] = data['email']
        if 'phone' in data: vals['phone'] = data['phone']
        if 'category_id' in data: vals['category_id'] = data['category_id']

        contact.write(vals)
        return request.make_response(
            json.dumps({'status': 'success', 'message': 'Contact updated'}),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/contact/delete/<int:contact_id>', type='http', auth='public', methods=['DELETE', 'POST'], csrf=False)
    def delete_contact(self, contact_id):
        contact = request.env['mon_module.contact'].sudo().browse(contact_id)
        if not contact.exists():
            return request.make_response(
                json.dumps({'status': 'error', 'message': 'Contact not found'}),
                headers={'Content-Type': 'application/json'},
                status=404
            )
        
        contact.unlink()
        return request.make_response(
            json.dumps({'status': 'success', 'message': 'Contact deleted'}),
            headers={'Content-Type': 'application/json'}
        )
