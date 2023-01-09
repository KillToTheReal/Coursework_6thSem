import os.path
import requests

from download import download_wikipedia_abstracts
from load import load_documents
from search.timing import timing
from search.index import *
import pickle
from search.documents import WikiPage, TextFile, PDFFile

@timing
def index_documents(documents, index: Index):
    for i, document in enumerate(documents):
        index.index_document(document)
        if i % 250 == 0:    
            print(f'Indexed {i} documents', end='\r')
    return index

@timing
def dump_map(file, map):
    print("Writing pickle file in process.\n")
    with open(str(file), 'wb') as f:
        pickle.dump(map, f)

@timing
def load_map(file):
    print("Map exists. Loading pickle file in process.\n")
    with open(str(file), 'rb') as f:
        return pickle.load(f)
        

if __name__ == '__main__':
    # Скачивает XML если нет файла;
    # Если нужна свежая копия удалите файл
    # С pickle - файлами то же самое
    # if not os.path.exists('data/enwiki-latest-abstract.xml.gz'):
    #     download_wikipedia_abstracts()

    # if not os.path.exists('data/map.pickle'):
    #     index = index_documents(load_documents(), Index()) 
    #     dump_map('data/map.pickle', index)                                  
    # else:
    #     index = load_map('data/map.pickle')           
        
    index = index_documents(load_documents('.'), Index())          
    #Возвращает объект типа ID, Title, abstract(text), url     
    print(f'Index contains {len(index.documents)} documents')
    # print(index.search('Python programming language', search_type='AND',rank=True)[:2])
    # print(index.search('Python programming language', search_type='AND', rank=True)[:2])
    myarray = index.search('rtf', search_type='OR')
    print(myarray)
    pages = [x.path for x in myarray]
    print(pages)
    
    exit()
