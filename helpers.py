### GET yt video LINK ###

def get_clean_id(url):
    marker=["watch?v=","youtu.be/","/shorts/"]
    for i in marker:
        if i in url:
           split_url=url.split(i)
           yt_id=split_url[1]
           clean_id=yt_id[:11]
           if len(clean_id)==11:
               return clean_id  
    else:
         return None

url=str(input("ENter Youtubr Video Link:")).strip()
def youtube_id(url):
   return get_clean_id(url)       
   

clean_id=youtube_id(url)
print(clean_id)
