#!/usr/bin/env python
from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
if __name__ == '__main__':
    manager.run()