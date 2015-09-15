from htmlParser import HtmlAttributeParser
import argparse
import json


def parse_cli_arguments():
    parser = argparse.ArgumentParser(description='Comic parser CLI')
    parser.add_argument("-s",
                        "--source",
                        required=True,
                        default="",
                        help="Html source either HTTP/HTTPS or file")
    parser.add_argument("-t",
                        "--term",
                        "--search-term",
                        default="",
                        help="Search term for looking html attributes")
    parser.add_argument("-n",
                        "--name",
                        default="",
                        help="Name of comic")
    parser.add_argument("--tag",
                        default="img",
                        help="Tag to be searched")
    parser.add_argument("--attribute",
                        default="src",
                        help="Attribute to be searched")
    return parser.parse_args()


def main():
    arguments = parse_cli_arguments()
    source_parser = HtmlAttributeParser(url=arguments.source,
                                        search_term=arguments.term,
                                        tag=arguments.tag,
                                        attribute=arguments.attribute)
    comic_url = source_parser.search()
    return_json = {"name": arguments.name, "url": comic_url}
    print(json.dumps(return_json))

if __name__ == "__main__":
    main()
