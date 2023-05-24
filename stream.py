import streamlit as st
import pandas as pd
import pickle
import sqlite3
from stream_prediction import predict
from ajout_voiture import ajout



onglet = st.sidebar.selectbox("Choisissez un onglet", ["predict", "ajouter"])

if onglet == "predict":

    predict()


elif onglet == "ajouter":
    
    ajout()