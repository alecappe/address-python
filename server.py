from flask import Flask
from flask_restful import Resource, Api, reqparse
from http.client import OK
from http.client import CREATED
from http.client import NO_CONTENT


app = Flask(__name__)
api = Api(app)

address_book = [
    {
        'name': 'pippo',
        'surname': 'rossi',
        'number': '0550555789'
    },
    {
        'name': 'pippo2',
        'surname': 'rossi2',
        'number': '0550555789'
    }
]


class Contacts(Resource):
    def get(self):
        return address_book, OK

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('surname', required=True)
        parser.add_argument('number', required=True)
        args = parser.parse_args(strict=True)

        address_book.append({
            'name': args['name'],
            'surname': args['surname'],
            'number': args['number']
        })
        return address_book, CREATED


class Contact(Resource):
    def delete(self, name, surname):
        for address in address_book:
            if address['name'] == name and address['surname'] == surname:
                address_book.remove(address)
        return None, NO_CONTENT


api.add_resource(Contacts, '/contacts')
api.add_resource(Contact, '/contact/<name>/<surname>')

if __name__ == '__main__':
    app.run(debug=True)
