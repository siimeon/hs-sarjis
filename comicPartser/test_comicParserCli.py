import unittest
from htmlParser import HtmlAttributeParser


class TestHtmlParser(unittest.TestCase):

    def test_hs_fingerpori(self):
        url = "http://www.hs.fi/fingerpori/"
        search_term = "/webkuva/taysi/"
        tag = "link"
        attribute = "href"
        parser = HtmlAttributeParser(url=url,
                                     search_term=search_term,
                                     tag=tag,
                                     attribute=attribute)
        partial_hit = "snstatic.fi/webkuva/taysi/1920"
        self.assertIn(partial_hit, parser.search())

    def test_iltalehti_fingerpori(self):
        url = "http://www.iltalehti.fi/fingerpori/"
        search_term = "iltalehti.fi/sarjakuvat/"
        parser = HtmlAttributeParser(url=url,
                                     search_term=search_term)
        partial_hit = "iltalehti.fi/sarjakuvat/Fingerpori"
        self.assertIn(partial_hit, parser.search())


if __name__ == "__main__":
    unittest.main()
