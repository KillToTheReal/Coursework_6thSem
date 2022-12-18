import gzip
from lxml import etree
import time
import os
from search.documents import WikiPage, TextFile

def load_documents():
    start_path = '.' # current directory
    start = time.time()
    doc_id = 0
    for path,dirs,files in os.walk(start_path):
        for filename in files:
            if filename.endswith('.txt'):
                with open(os.path.join(path,filename)) as f:
                    path_to_file = os.path.join(path,filename)
                    abstract = f.read()
                    yield TextFile(ID=doc_id, abstract=abstract, path=path_to_file)
                    doc_id += 1

            # elif filename.endswith('gz'):
            #     with gzip.open('data/enwiki-latest-abstract.xml.gz', 'rb') as f:   
            #         for _, element in etree.iterparse(f, events=('end',), tag='doc'):
            #             title = element.findtext('./title')
            #             url = element.findtext('./url')
            #             abstract = element.findtext('./abstract')
            #             path = './data/123.xml'
            #             yield WikiPage(ID=doc_id, title=title, url=url, abstract=abstract, path=path)
            #             doc_id += 1
            #             element.clear()
    end = time.time()
    print(f'Parsing Documents took {end - start} seconds')
