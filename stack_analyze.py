import html
import os.path
import os
import sys
import urllib.request


def check_url(url):
    values = url.split("/")
    protocol = values[0].split(':')[0]
    type_stack = values[2]
    question = values[3]
    if protocol != 'https' or type_stack != 'stackoverflow.com' or question != 'questions':
        sys.exit('Usage: url is not correct')


def remove_python_shell(snippet):
    if ">>>" in snippet:
        snippet_list = snippet.split('\\n')
        final_snippet = ''
        for element in snippet_list:
            if (">>>" in element or element.startswith('   ') or element.startswith('...')) \
                    and not element.startswith('#'):
                element = element.replace('>>> ', '')
                element = element.replace('>>>', '')
                element = element.replace('...', '   ')
                final_snippet += element + '\\n'
        return final_snippet
    return snippet


def delete_one_line_file(file):
    file_r = open(file)
    if len(file_r.readlines()) == 1:
        os.remove(file)
    file_r.close()


def read_and_extract(url):
    """function to read the url snippets"""
    page = urllib.request.urlopen(url).read()
    page_1 = str(page).split('answercell post-layout--right')[1:]
    answer_file_count = 0
    answer_count = 0
    for i in page_1:
        page_aux_1 = i.split('<code>')[1:]
        for p in page_aux_1:
            page_aux_2 = p.split('</code>')[0]
            snippet = html.unescape(page_aux_2)
            if " " in snippet and 'Traceback' not in snippet and '$' not in snippet:
                filename = "test_directory/answer_" + str(answer_count) + '_file_' + str(answer_file_count) + ".py"
                file = open(filename, "w")
                snippet = remove_python_shell(snippet)
                snippet = snippet.replace("\\n", "\n")
                file.writelines(snippet.replace("\\", ""))
                file.close()
                delete_one_line_file(filename)
                answer_file_count = answer_file_count + 1
        answer_count = answer_count + 1
        answer_file_count = 0
    '''page_4 = []
    for e in page_1:
        page_3 = e.split('<code>')[1:]
        page_4 = e.split('</code>')[0]
        page_4 = page_4.replace('&quot;', '"')
        file.writelines(page_4.replace("\\n", "\n")) #.replace("\\n", "\n")'''


def remove_files_from_test_directory():
    directory = 'test_directory'
    for f in os.listdir(directory):
        os.remove(os.path.join(directory, f))


def main_stack(url):
    """principal function to analyze stack overflow url"""
    check_url(url)
    read_and_extract(url)
    pos = os.path.abspath('test_directory')
    return pos
