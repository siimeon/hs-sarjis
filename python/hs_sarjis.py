import urllib2
import json
import sys

SEARCH_TERM = 'webkuva/sarjis'


class Sarjis(object):

    def __init__(self, name, url):
        super(Sarjis, self).__init__()
        self.name = name
        self.url = url
        self.data = self.load_data_from_url(url)
        self.hit = self.search_data(self.data)
        self.result = self.parse_img_tag(self.hit)
        self.output = {
            "name": self.name,
            "url": self.result
        }

    def load_data_from_url(self, url):
        return urllib2.urlopen(url).read()

    def get_url(self):
        return self.url

    def search_data(self, data):
        hit = None
        for line in data.split('\n'):
            if SEARCH_TERM in line:
                hit = line.strip()
        if hit is not None:
            return hit
        return None

    def parse_img_tag(self, tag):
        parsed_tag = tag.replace('<', '').replace('/>', '')
        tag_parts = parsed_tag.split(' ')
        for part in tag_parts:
            if 'src' in part:
                url = part.split('src=').pop()
                return url.replace('"', '')

    def get_json(self):
        print json.dumps(self.output)

if __name__ == '__main__':
    # Arguments for this program: name, url
    # Example: hs_sarjis.py name_of_comic http://www.url.of/comic
    s = Sarjis(sys.argv[1], sys.argv[2])
    s.get_json()
