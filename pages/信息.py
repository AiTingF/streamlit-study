import streamlit as st
import  pandas as  pd

column1, column2, column3 = st.columns([2,2,1])
with column1:
    name = st.text_input("请输入你的名字：")
    if name:
        st.write(f"你好，{name}")

with column2:
    password = st.text_input("请输入你的密码：",type = "password")
    if password:
        st.write(f"你的密码是{password}")
with column3:
    age = st.number_input("请输入你的年龄：",value = 20,min_value = 0,max_value = 150,step = 1)
    st.write(f"你的年龄{age}")

st.divider()
paragragh = st.text_area("请输入一段自我介绍：")

st.divider()
checked = st.checkbox("我同意以上内容")
if checked:
    st.write(f"感谢同意！")
submit = st.button("提交")
if submit:
    st.write(f"提交成功！")
