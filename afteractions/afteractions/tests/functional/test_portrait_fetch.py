from afteractions.lib.pilot import get_portrait_by_name

class TestPortraitFetch(object):
    def setUp(self):
        pass
    
    def test_fetch_by_name(self):
        s = get_portrait_by_name("Quebnaric Deile")
        print s
        assert False
        