from afteractions.tests import *

class TestIndexController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='home', action='index'))
        # Test response...
