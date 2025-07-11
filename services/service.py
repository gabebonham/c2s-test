from constants.attributes import getAttributes, getAlias
from db.db import Db
import spacy
from spacy.matcher import PhraseMatcher
import pandas as pd
from init.scripts.generate_mocks import createMocks
class Service:
    def __init__(self):
        self.db = Db()
        self.attributes = getAttributes()
        self.aliases = getAlias()  
        self.aliasMapReversed = {v.lower(): k for k, v in self.aliases.items()}
        self.nlp = spacy.load("pt_core_news_sm")
        pass
    def searchQuery(self, input:str)->dict:
        matcher = PhraseMatcher(self.nlp.vocab)
        patterns = [self.nlp.make_doc(alias) for alias in self.aliasMapReversed.keys()]
        matcher.add("CAMPOS_DB", patterns)

        output = self.nlp(input)
        matches = matcher(output)
        
        filters = {}
        for _, start, end in matches:
            field = output[start:end].text.lower()

            if end < len(output):
                value = output[end].text
                internalField = self.aliasMapReversed.get(field)
            if internalField:
                filters[internalField] = value
        
        return filters
    def getResults(self,input:str)->pd.DataFrame:
        filters = self.searchQuery(input)
        df = self.db.getAllAutomobileDF()
        for param, value in filters.items():
            if df[param].dtype == 'int64':
                value = int(value)
            elif df[param].dtype == 'float64':
                value = float(value)
            df = df[df[param] == value]
        return df

# createMocks()
service = Service()
print(service.getResults("marca Bugatti ano 2020").head())