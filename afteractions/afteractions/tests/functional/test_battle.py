from afteractions.tests import *

class TestBattleController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='battle', action='index'))
        # Test response...
