import unittest
from app import create_app, db
from models import User, Event, Ticket

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_user_creation(self):
        u = User(username='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()
        self.assertTrue(u.id)
    
    def test_event_creation(self):
        e = Event(name='Concert', date='2021-12-25', venue='Stadium')
        db.session.add(e)
        db.session.commit()
        self.assertTrue(e.id)
    
    def test_ticket_creation(self):
        u = User(username='john', email='john@example.com')
        e = Event(name='Concert', date='2021-12-25', venue='Stadium')
        db.session.add(u)
        db.session.add(e)
        db.session.commit()
        t = Ticket(user_id=u.id, event_id=e.id)
        db.session.add(t)
        db.session.commit()
        self.assertTrue(t.id)
    
    def test_ticket_association(self):
        u = User(username='john', email='john@example.com')
        e = Event(name='Concert', date='2021-12-25', venue='Stadium')
        db.session.add(u)
        db.session.add(e)
        db.session.commit()
        t = Ticket(user_id=u.id, event_id=e.id)
        db.session.add(t)
        db.session.commit()
        self.assertEqual(t.user.username, 'john')
        self.assertEqual(t.event.name, 'Concert')