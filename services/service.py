from constants.attributes import getAttributes, getAlias
from db.db import Db
import spacy
from spacy.matcher import PhraseMatcher
import pandas as pd
from init.scripts.generate_mocks import createMocks
from models.automobile import Automobile
import json
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
        patterns = [self.nlp.make_doc(alias.lower()) for alias in self.aliases.values()]
        matcher.add("CAMPOS_DB", patterns)

        output = self.nlp(input.lower())
        matches = matcher(output)
        
        filters = {}
        for _, start, end in matches:
            matchedText = output[start:end].text.lower()
            field = self.aliasMapReversed.get(matchedText)
            
            if field and end < len(output):
                value = output[end].text
                while value in [',', '.', '!', '?'] and end + 1 < len(output):
                    end += 1
                    value = output[end].text
                filters[field] = value
        
        return filters
    
    def getResults(self,input:str)->pd.DataFrame:
        filters = self.searchQuery(input)
        df = self.db.getAllAutomobileDF()
        
        for param, value in filters.items():
            if param not in df.columns:
                continue
            if df[param].dtype == 'int64':
                try: value = int(value)
                except: continue
            elif df[param].dtype == 'float64':
                try: value = float(value)
                except: continue
            if df[param].dtype == 'object':
                df = df[df[param].str.lower() == value.lower()]
            else:
                df = df[df[param] == value]
                
        return df
    def getResultsApi(self,filters:dict)->pd.DataFrame:
        mappedFilters = self.reverseMap(filters)
        df = self.db.getAllAutomobileDF()
        
        for param, value in mappedFilters.items():
            if param not in df.columns:
                continue
            if df[param].dtype == 'int64':
                try: value = int(value)
                except: continue
            elif df[param].dtype == 'float64':
                try: value = float(value)
                except: continue
            if df[param].dtype == 'object':
                df = df[df[param].str.lower() == value.lower()]
            else:
                df = df[df[param] == value]
        print(df.head())
        return self.mapToJson(df)
    
    def reverseMap(self,filters:dict):
        mappedFilter = {}
        for param_pt, value in filters.items():
            if value is None:
                continue 
            
            dbColumn = self.aliasMapReversed.get(param_pt.lower())
            if dbColumn:
                mappedFilter[dbColumn] = value
        print(mappedFilter)
        return mappedFilter
    def mapToJson(self, df:pd.DataFrame)->str:
        automobileList = []
        for index, row in df.iterrows():
            automobile = Automobile()
            for columnName, value in row.items():
                newColumnNameUnderline = str(columnName).replace('_', ' ')
                newColumnName = newColumnNameUnderline.title()
                newColumnName = newColumnName[0].lower() + newColumnName[1:]
                setattr(automobile, newColumnName.replace(' ', ''), value)
            automobileList.append(automobile.to_dict_pt())
        return automobileList