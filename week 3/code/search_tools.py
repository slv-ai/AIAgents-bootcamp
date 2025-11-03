from minsearch import Index
from typing import Any, List, Dict
import docs
class SearchTools:
    def __init__(self,index:Index):
        self.index = index
    def search(self,query:str) -> List[Dict[str,Any]]:
        return self.index.search(
            query=query,
            num_results=5
        )