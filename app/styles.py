def apply_dark_mode(dark_mode):
    import streamlit as st
    if dark_mode:
        st.markdown("""
            <style>
            .main {
                background-color: #121212;
                color: white;
            }
            .chat-box {
                background-color: #1e1e1e;
                color: white;
                border-radius: 15px;
                padding: 1.5rem;
                box-shadow: 0 4px 10px rgba(255,255,255,0.1);
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .main {
                background-color: #f0f2f6;
            }
            .chat-box {
                background-color: white;
                padding: 1.5rem;
                border-radius: 15px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            </style>
        """, unsafe_allow_html=True)

