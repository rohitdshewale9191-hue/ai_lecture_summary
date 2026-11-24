import streamlit as st
def init_state():
    st_dict={"link":None,
             "notes":None,
             "cards":None,
             "card_pos":0,
             "flipped":False,
             "quiz":None,
             "quiz_problems":[],
             "quiz_submitted":False,
             "log":[]
             }