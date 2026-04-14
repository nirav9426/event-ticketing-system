from flask import Flask, jsonify, request
from models import db, User, Event, Ticket

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/event_tickets'
    db.init_app(app)
    
    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        user = User(username=data['username'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    
    @app.route('/events', methods=['POST'])
    def create_event():
        data = request.get_json()
        event = Event(name=data['name'], date=data['date'], venue=data['venue'])
        db.session.add(event)
        db.session.commit()
        return jsonify({'message': 'Event created successfully'}), 201
    
    @app.route('/tickets', methods=['POST'])
    def book_ticket():
        data = request.get_json()
        ticket = Ticket(user_id=data['user_id'], event_id=data['event_id'])
        db.session.add(ticket)
        db.session.commit()
        return jsonify({'message': 'Ticket booked successfully'}), 201
    
    @app.route('/payments', methods=['POST'])
    def process_payment():
        # Payment processing logic here
        return jsonify({'message': 'Payment processed successfully'}), 200
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)