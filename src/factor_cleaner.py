import re

def clean_factor(term):
    if not term:
        return None

    term = term.lower().strip()

    
    BAD_FRAGMENTS = {
        "did ve", "ve checked", "ve sent", "thing happens",
        "definitely did", "account number", "digits",
        "recently", "wanted", "sure"
    }

    if term in BAD_FRAGMENTS:
        return None

   
    term = re.sub(r"\bve\b", "'ve", term)

    
    if len(term.split()) < 2:
        return None

    
    term = term.replace("_", " ").title()

    return term


    
    
