import urllib2


class HtmlAttributeParser(object):

    def __init__(self, url, search_term, tag="img", attribute="src"):
        """
        HtmlAttributeParser class for parsing attribute value from html data
        :param url: String; String of HTTP/HTTPS url or filesystem path
        :param search_term: String; String for searching attribute
        :param tag: String; String of HTML tag used that has looked information. Default 'img'
        :param attribute: String; String of HTML tag attribute that value is looked. Default 'src'
        """
        # Init class variables
        self.url = url
        self.search_term = search_term
        self.tag = tag
        self.attribute = attribute

    def search(self):
        """
        search() method does searching of attribute
        :return: String; String of attribute value or None if value not found
        """
        # Load data from url
        data = self.load_data_from_url(self.url)
        # Searching tag and search term from data
        hit = self.search_from_data(data)
        # Parsing attribute value from hit from previous step
        return self.parse_attribute(hit)

    def get_url(self):
        """
        get_url() method returns String of url or filesystem path that is used
        :return: String; String of url variable
        """
        return self.url

    def set_tag(self, tag):
        """
        set_tag() method sets new tag to be searched
        :param tag: String; String of tag name
        :return: None; Nothing is returned
        """
        self.tag = tag

    def set_attribute(self, attribute):
        """
        set_attribute() method sets new attribute to be searched
        :param attribute: String; String of attribute name
        :return: None; Nothing is returned
        """
        self.attribute = attribute

    def search_from_data(self, data):
        """
        search_from_data() method finds first hit of correct tag and search term in line of data
        :param data: String; String of content that search is performed
        :return: String or None; String is returned if hit is found and None if no hit is found
        """
        tag = "<" + self.tag
        for line in data.split('\n'):
            if self.search_term in line and tag in line:
                line_array = line.split(tag)
                tag_attributes = line_array[1].split(">")[0]
                return tag_attributes
        return None

    def parse_attribute(self, tag):
        """
        parse_attribute() method is used to parse attribute from hit line from search_from_data() method
        :param tag: String; String that contains attribute looked for (example src attribute from img)
        :return: String or None; String of attribute value or None is returned
        """
        parsed_tag = tag.replace('<', ' ').replace('/>', ' ').replace('>', ' ')
        tag_parts = parsed_tag.split(' ')
        for part in tag_parts:
            if self.attribute in part:
                url = part.split(self.attribute + '=').pop()
                return url.replace('"', '')
        return None

    @staticmethod
    def load_data_from_url(url):
        """
        load_data_from_url() function loads data from url ether http/https or file system
        Note! if your are trying to load data with HTTP/HTTPS please be sure that url has protocol in it
        example "http://" or "https://"
        :param url: String; HTTP/HTTPS url or filesystem path
        :return: String; Content of given url or file
        """
        if "http://" in url or "https://" in url:
            return urllib2.urlopen(url).read()
        else:
            return open(url, "r").read()
