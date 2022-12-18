import math

from .timing import timing
from .analysis import analyze
from .documents import WikiPage, TextFile
from typing import Union

class Index:
    def __init__(self):
        self.index = {}
        self.documents = {}

    def index_document(self, document: Union[WikiPage, TextFile]):
        print(document.ID)
        if document.ID not in self.documents:
            self.documents[document.ID] = document
            document.analyze()
            print('Document analyzed')
            
        for token in analyze(document.fulltext):
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(document.ID)

    def document_frequency(self, token):
        return len(self.index.get(token, set()))

    def inverse_document_frequency(self, token):
        # https://ru.wikipedia.org/wiki/TF-IDF
        # https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html
        return math.log10(len(self.documents) / self.document_frequency(token))
    
    def all_data(self):
        return self.documents, self.index
    
    def _results(self, analyzed_query):
        return [self.index.get(token, set()) for token in analyzed_query]

    @timing
    def search(self, query, search_type='AND', rank=False):
        """
        Основная функция. Она возвращает найденные по запросу документы 
        и сортирует их по релевантности (sets are fast, but unordered).

        Параметры:
          - query: Запрос
          - search_type: ('AND', 'OR') Все ли литералы из запроса должны присутсвовать в искомом документе или только один
          - score: (True, False) Если значение True, результаты сортируются по TF-IDF score
        """
        if search_type not in ('AND', 'OR'):
            return []

        analyzed_query = analyze(query)
        results = self._results(analyzed_query)
        if search_type == 'AND':
            # Тип поиска где все токены должны присутствовать в документе
            documents = [self.documents[doc_id] for doc_id in set.intersection(*results)]
        if search_type == 'OR':
            # Хотя бы один токен должен присутствовать в документе
            documents = [self.documents[doc_id] for doc_id in set.union(*results)]

        if rank:
            return self.rank(analyzed_query, documents)
        return documents

    def rank(self, analyzed_query, documents):
        results = []
        if not documents:
            return results
        for document in documents:
            score = 0.0
            for token in analyzed_query:
                tf = document.term_frequency(token)
                idf = self.inverse_document_frequency(token)
                score += tf * idf
            results.append((document, score))
        return sorted(results, key=lambda doc: doc[1], reverse=True)
