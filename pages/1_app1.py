import streamlit as st

def load_page1():
    from pages.app1.page1 import main
    main()
    
def load_page2():
    from pages.app1.page2 import main
    main()

def load_page3():
    from pages.app1.page3 import main
    main()

def load_page4():
    from pages.app1.page4 import main
    main()

def load_page5():
    from pages.app1.page5 import main
    main()
    
st.sidebar.button('Page 1', on_click=load_page1)
st.sidebar.button('Page 2', on_click=load_page2)
st.sidebar.button('Page 3', on_click=load_page3)
st.sidebar.button('Page 4', on_click=load_page4)
st.sidebar.button('Page 5', on_click=load_page5)

