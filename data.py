# import streamlit as st
# import database as db

# st.set_page_config(page_title="Test database",page_icon="😱",layout="wide")
# st.title("Test Database")
# with st.form("Form1"):
#     col1,col2 = st.columns([2,1])
#     with col1:
#         m=st.selectbox("select",["ab","bc"])
#         o=st.selectbox("select",["hk","lf"])
#     with col2:
#         n=st.selectbox("select",["cd","ef"])

#     submittedd=st.form_submit_button("submit")
#     ok =db.button("ok",command=connection())
# if submittedd:
#     with col1:
#         st.write("Model selected:",m)
#         st.write("phone selected",o)
#     with col2:
#         st.write("phone selected",n)            