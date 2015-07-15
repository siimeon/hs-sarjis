import urllib2
import json
import argparse

HS_SEARCH_TERM = 'webkuva/sarjis'
IS_SEARCH_TERM = 'img/1920'
IL_SEARCH_TERM = '/sarjakuvat/'
# TODO Refactor class to be more general
# TODO Split class and CLI controller to separated file
# TODO Rename class implementation
# TODO Document class
# TODO add support for other than <img src=""> data


class HSComicParser(object):

    def __init__(self, name, url, iltasanomat=False):
        self.name = name
        self.url = url
        self.search_term = HS_SEARCH_TERM if iltasanomat is False else IS_SEARCH_TERM
        self.data = self.load_data_from_url(url)
        self.hit = self.search_data(self.data, self.search_term)
        self.result = self.parse_img_tag(self.hit)
        self.output = {
            "name": self.name,
            "url": self.result
        }

    @staticmethod
    def load_data_from_url(url):
        return urllib2.urlopen(url).read()

    @staticmethod
    def search_data(data, search_term):
        for line in data.split('\n'):
            if search_term in line and "<img" in line:
                return line.strip()

        return None

    @staticmethod
    def parse_img_tag(tag):
        parsed_tag = tag.replace('<', ' ').replace('/>', ' ').replace('>', ' ')
        tag_parts = parsed_tag.split(' ')
        for part in tag_parts:
            if 'src' in part:
                url = part.split('src=').pop()
                return url.replace('"', '')

    def get_url(self):
        return self.url

    def get_data_object(self):
        return self.output

    def get_json(self):
        return json.dumps(self.output)

    def __str__(self):
        return self.get_json()


def get_dilbert_object():
    return {
        "name": "Dilbert",
        "url": "http://www.taloussanomat.fi/dilbert/dilbert.php"
    }


def get_dilbert_json():
    return json.dumps(get_dilbert_object())


def parse_cmd_arguments():
    parser = argparse.ArgumentParser(description='Helsingin Sanomat comic parser')
    parser.add_argument("-n",
                        "--name",
                        help="Name of comic",
                        default="HS comic")
    parser.add_argument("-u",
                        "--url",
                        help="Url address of comic",
                        required=True)
    parser.add_argument("-is",
                        "--iltasanomat",
                        help="Option if Iltasanomat site is source of comic",
                        action="store_true",
                        default=False)
    parser.add_argument("--dilbert",
                        help="Option if Dilbert from Talousanomat is used",
                        action="store_true",
                        default=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_cmd_arguments()
    if args.iltasanomat is True and args.dilbert is True:
        raise ValueError
    if args.dilbert:
        comic_parser = get_dilbert_json()
    else:
        comic_parser = HSComicParser(name=args.name,
                                     url=args.url,
                                     iltasanomat=args.iltasanomat)
    print(comic_parser)
