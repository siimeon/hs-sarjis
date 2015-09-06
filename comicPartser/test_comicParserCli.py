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


if __name__ == "__main__":
    unittest.main()
