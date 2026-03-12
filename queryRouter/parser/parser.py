from ..models import ParsedQuery

class QueryParser:
    def parse(self, raw_text: str) -> ParsedQuery:
        clean = raw_text.strip()
        if not clean:
            return ParsedQuery(command="", query="")
            
        parts = clean.split(maxsplit=1)
        command = parts[0].lower()
        query = parts[1] if len(parts) > 1 else ""
        
        return ParsedQuery(command=command, query=query)