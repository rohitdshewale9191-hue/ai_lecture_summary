from google import genai
from dotenv import load_dotenv
import os
import time
from config import notes_schema,notes_prompt
import json
def get_client():
    load_dotenv()
    if not os.getenv("GEMINI_API_KEY"):
        return None
    
    return genai.Client()

### To get Input ready FOR gemini###
youtube_link=str(input("Enter YOUtube Link:"))
def video_part(youtube_link):
   return {"type":"video","uri":youtube_link}
    

### Calling gemini agent###
def call_gemini(client, contents, log, step, schema=None):
    st_time=time.time()
    if schema is not None:
       interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=contents,
        response_format={
    "type": "text",
    "mime_type": "application/json",
    "schema": schema
}
                      
)

    else:
        interaction = client.interactions.create(
                model="gemini-3.5-flash-lite",
                input=contents,

        )
      
    end_time=time.time()
    final_time = round(end_time - st_time, 2) 
    log.append({"step":step, 
                "seconds":final_time, 
                "input_tokens": interaction.usage.total_input_tokens, 
                "output_tokens": interaction.usage.total_output_tokens})
    if schema is not None:
        return json.loads(interaction.output_text)
    else:
        return interaction.output_text

    

##
def extract_notes(client, youtube_link,levels, languages, log):
    formatted_prompt = notes_prompt.format(levels, languages)
    input_list=[ video_part(youtube_link),{"type": "text", "text":formatted_prompt}]
    return  call_gemini(client, input_list, log, "notes",notes_schema)
log=[]
step="notes"
levels="intermidate"
languages="English"
client=get_client()
youtube_link=str(input("Enter YOUtube Link:"))
contents=video_part(youtube_link)
print(repr(youtube_link))
answer = extract_notes(
    client, youtube_link, levels, languages, log
)
print(answer)
