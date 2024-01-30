import streamlit as st
from pathlib import Path

def main():
    st.write(f'# {Path(__file__).parent.name} - {Path(__file__).name}')