import streamlit as st
import pickle 
import numpy as np
import sklearn
with open('model.pickle', 'rb') as f:
    model = pickle.load(f)

st.title('Sales prediction')
col1, col2 = st.columns(2)
with col1:
    tvsales = st.number_input(label='Tv',)
with col2:
    radiosales = st.number_input(label='Radio')
x = np.array([tvsales,radiosales]).reshape(1,-1)
if st.button('Predict',use_container_width=True):
    if tvsales != 0 and radiosales != 0:
        salepred = model.predict(x)
        st.success(f'Sale prediction: {round(float(salepred),3)}')
    else: st.warning('Please input Tv or Radio ads sales')

