import streamlit as st
import  pandas as  pd
with st.sidebar:
    st.image("./头像.jpg", width=300)

    if "a" not in st.session_state:
        st.session_state.a = 0
    clicked = st.button("点赞+1👍")
    if clicked:
        st.session_state.a += 1
    st.write(f"点赞{st.session_state.a}👍")


st.title("我的个人网站")
"### 早上好"
a = 329 * 3
a
[11,22,33]

{"a":"1","b":"2","c":"3"}



df = pd.DataFrame({"学号":["01","02","03","04","05"],
                   "班级":["01班","02班","03班","04班","05班"],
                   "成绩":["95","82","82","84","75"],})

st.dataframe(df)
st.divider()
st.table(df)


