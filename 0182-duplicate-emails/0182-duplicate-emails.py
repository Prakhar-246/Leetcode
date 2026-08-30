import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = person.groupby('email').size().reset_index(name='count')
    
    result = result[result['count'] > 1]
    
    return result[['email']].rename(columns={'email': 'Email'})