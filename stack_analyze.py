import html
import os.path
import os
import sys
import urllib.request


def check_url(url, option):
    if option == 'stack':
        values = url.split("/")
        protocol = values[0].split(':')[0]
        type_stack = values[2]
        question = values[3]
        if protocol != 'https' or type_stack != 'stackoverflow.com' or question != 'questions':
            sys.exit('Usage: url is not correct')
    elif option == 'pull':
        values = url.split("/")
        protocol = values[0].split(':')[0]
        type_pull = values[2]
        if protocol != 'https' or type_pull != 'github.com':
            sys.exit('Usage: url is not correct')
    else:
        sys.exit('Usage: option type is not correct')


def remove_python_shell(snippet):
    if ">>>" in snippet:
        snippet_list = snippet.split('\\n')
        final_snippet = ''
        pre_shell = snippet.split('>>>')
        if '' != pre_shell[0]:
            final_snippet += pre_shell[0]
        for element in snippet_list:
            if element not in final_snippet:
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


def make_url(url):
    url_util = url[19:]
    final_url = 'https://patch-diff.githubusercontent.com/raw/' + url_util + '.diff'
    return final_url


def remove_plus(snippet):
    final_snippet = ''
    list_line = snippet.split('\\n')
    for element in list_line:
        final_snippet += element[1:] + '\\n'
    return final_snippet


def read_and_extract(url, option):
    """function to read the url snippets"""
    page = urllib.request.urlopen(url).read()
    if option == 'stack':
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
    elif option == 'pull':
        url_1 = make_url(url)
        page_1 = urllib.request.urlopen(url_1).read()
        pull_count = 0
        snippet_list = str(page_1).split('@@')[1:]  # .replace('+', '')
        for snippet in snippet_list:
            if len(snippet) >= 50:
                filename = "test_directory/pull_" + str(pull_count) + ".py"
                file = open(filename, "w")
                snippet = snippet.split('diff --git')[0]
                snippet = remove_plus(snippet)
                snippet = snippet.replace("\\n", "\n")
                snippet = snippet.replace("\\'", "'")
                snippet = snippet.replace('/\\', '/')
                snippet = snippet.replace('\\r', '')
                snippet = snippet.replace('\\ No newline at end of file', '')
                file.writelines(snippet.replace(">>>", ""))
                file.close()
                pull_count = pull_count + 1


def remove_files_from_test_directory():
    directory = 'test_directory'
    for f in os.listdir(directory):
        os.remove(os.path.join(directory, f))


def main_stack(url, option):
    """principal function to analyze stack overflow url"""
    check_url(url, option)
    read_and_extract(url, option)
    pos = os.path.abspath('test_directory')
    return pos
