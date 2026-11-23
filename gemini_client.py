from google import genai
from dotenv import load_dotenv
import os
import time
from config import notes_schema
import json
def get_client():
    load_dotenv()
    if not os.getenv("GEMINI_API_KEY"):
        return None
    
    return genai.Client()

### To get Input ready FOR gemini###
youtube_link=str(input("Enter YOUtube Link:"))
def video_part(youtube_link):
    input_dict={"type":"video","url":youtube_link}
    return input_dict

### Calling gemini agent###
def call_gemini(client, contents, log, step, schema=None):
    st_time=time.time()
    if schema==True:
       interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=contents,
        response_format=notes_schema
                      
)
    if schema==None:
        interaction = client.interactions.create(
                model="gemini-3.5-flash-lite",
                input=contents,

        )
