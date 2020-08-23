from IPython.core.display import display

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

def url_to_html(url):
    # Source: https://realpython.com/python-web-scraping-practical-introduction/
    page = urlopen(url)  # open the url
    html = page.read().decode("utf-8")  # read the url
    return html


def html_to_text(html):
    soup = BeautifulSoup(html, "html.parser")  # parse html
    parsed = soup.get_text().replace("\n\n", "")  # remove superfluous newlines
    return parsed


def main():
    # Source: https://realpython.com/python-web-scraping-practical-introduction/
    with open("requirements_urls.txt", "r") as fp:
        lines = fp.readlines()
    for line in lines:
        url = line.replace("\n", "")
        fname = url.split("/")[-2]
        html = url_to_html(url)
        parsed = html_to_text(html)
        soup = BeautifulSoup(html, "html.parser")
        test = soup.find_all("table")
        dfdict = []
        count = 0
        print("*****" + fname + "*****")
        for i in test:
            df = pd.read_html(str(i))  # this parses all the tables in webpages to a list
            df = pd.DataFrame(df[0])
            display(df)
            print()


if __name__ == "__main__":
    main()
