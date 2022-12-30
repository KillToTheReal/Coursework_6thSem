from collections import Counter
from dataclasses import dataclass
from .analysis import analyze

@dataclass
class WikiPage:
    """Абстракция описывающая страницу вики"""
    ID: int
    title: str
    abstract: str
    url: str
    path: str

    @property
    def fulltext(self):
        return ' '.join([self.title, self.abstract])

    def analyze(self):
        self.term_frequencies = Counter(analyze(self.fulltext))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)
    
@dataclass
class TextFile:
    ID: int
    abstract: str
    path: str
    
    @property
    def fulltext(self):
        return self.abstract
    
    def analyze(self):
        self.term_frequencies = Counter(analyze(self.fulltext))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)
    
    
@dataclass
class PDFFile:
    ID: int
    abstract: str
    page: int
    path: str
    
    @property
    def fulltext(self):
        return self.abstract
    
    def analyze(self):
        self.term_frequencies = Counter(analyze(self.fulltext))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)
    
@dataclass
class XLSFile:
    ID: int
    abstract: str
    row: int
    path: str
    
    @property
    def fulltext(self):
        return self.abstract
    
    def analyze(self):
        self.term_frequencies = Counter(analyze(self.fulltext))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)
    
@dataclass
class DOCXFile:
    ID: int
    abstract: str
    paragraph: int
    path: str
    
    @property
    def fulltext(self):
        return self.abstract
    
    def analyze(self):
        self.term_frequencies = Counter(analyze(self.fulltext))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)