from ..models import ParsedQuery

class QueryParser:
    def parse(self, raw_text: str, separator: str = ":") -> ParsedQuery:
        clean = raw_text.strip()
        if not clean:
            return ParsedQuery(command="", query="")
            
        if separator in clean:
            parts = clean.split(separator, 1)
            command = parts[0].strip().lower()
            query = parts[1].strip()
        else:
            command = clean.lower()
            query = ""
        
        return ParsedQuery(command=command, query=query)