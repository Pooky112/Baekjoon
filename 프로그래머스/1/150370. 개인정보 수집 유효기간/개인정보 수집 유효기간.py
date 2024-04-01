from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    term_dict = {term.split()[0]: int(term.split()[1]) for term in terms}
    
    today_date = datetime.strptime(today, "%Y.%m.%d")
    
    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        date = datetime.strptime(date, "%Y.%m.%d")
        
        expiry_date = date + relativedelta(months=term_dict[term])
        
        if today_date >= expiry_date:
            answer.append(i + 1)

    return answer
