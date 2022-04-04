import os.path
import sys
import urllib.request


def check_url(url):
    values = url.split("/")
    protocol = values[0].split(':')[0]
    type_stack = values[2]
    question = values[3]
    if protocol != 'https' or type_stack != 'stackoverflow.com' or question != 'questions':
        sys.exit('Usage: url is not correct')


def read_and_extract(url):
    """function to read the url snippets"""
    page = urllib.request.urlopen(url).read()
    file = open("test.py", "w")
    page_1 = str(page).split('s-prose js-post-body')[1]
    page_2 = page_1.split('js-post-menu pt2')[0]
    page_3 = page_2.split('<code>')[1:]
    page_4 = []
    for e in page_3:
        page_4 = e.split('</code>')[0]
        page_4 = page_4.replace('&quot;', '"')
        file.writelines(page_4) #.replace("\\n", "\n")
    file.close()


def main_stack(url):
    """principal function to analyze stack overflow url"""
    check_url(url)
    read_and_extract(url)
    pos = os.path.abspath('test.py')
    return pos
