import pandas as pd
import re

def preprocess(data):

    pattern=r"\d{2}/\d{2}/\d{2},\s\d{1,2}:\d{2}\s[ap]m\s-\s"
    messages=re.split(pattern,data)[1:]
    dates=re.findall(pattern,data)
    
    df=pd.DataFrame({'user_message':messages,'message_data':dates})
#convert msg data type
    df['message_data']=pd.to_datetime(df['message_data'],format='%d/%m/%y, %I:%M %p - ', errors='coerce')

    df.rename(columns={'message_data':'date'},inplace=True)
    
    
    users = []
    messages = []


    for message in df['user_message']: 
        entry = re.split(r'([\w\W]+):\s', message)
        if entry[1:]:  
           users.append(entry[1])  
           messages.append(entry[2])  
        else: 
           users.append('group notification')  
           messages.append(entry[0])  

    df['user'] = users
    df['message'] = messages


    df.drop(columns=['user_message'], inplace=True)
    
    df['only_date'] = df['date'].dt.date
    df['year']=df['date'].dt.year
    df['month_num']=df['date'].dt.month
    df['month']=df['date'].dt.month_name()
    df['day']=df['date'].dt.day
    df['day_name']=df['date'].dt.day_name()
    df['hour']=df['date'].dt.hour
    df['minute']=df['date'].dt.minute
    
    return df