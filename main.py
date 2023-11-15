import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://api.todoist.com/rest/v2/tasks'
headers={}
headers['Authorization']=os.getenv('AUTH')
headers['Cookie']=os.getenv('COOKIE')
data = requests.get(url, headers=headers).json()

for task in data:
    task_info=(task['content'], task['created_at'])
    print(task_info)
    st.write(task_info)
