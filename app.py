import streamlit as st
import datetime

st.set_page_config(layout="wide")

data_file_path = "data.csv"
try:
    df = pd.read_csv(data_file_path)
except FileNotFoundError:
    # Create an empty DataFrame if the file doesn't exist
    data_con_msg="data could not be loaded please contact your app admin"

def collect_data_tab():
    s1=st.expander("Sample 1", expanded=False)
    
    s1.write("## Collect Data")

    col1, col2 = s1.columns([2, 1])
    
    # Left column with an image
    col1.image("test_image.png", width=400)
    # Right column with input rows
    with col2:
        dimension_1a = st.text_input("Dimension A", "")
        dimension_2a = st.text_input("Dimension B", "")
        dimension_3a = st.text_input("Dimension C", "")


def results_tab():
    st.write("## Results")

def historical_data_tab():
    st.write("## Historical Data")
    st.write(df)
def main():
    st.title("CNC data")
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    if data_con_msg!="":
        st.write(data_con_msg)
    # Create tabs
    tabs = ["Collect data", "Results", "Historical data"]
    selected_tab = st.sidebar.radio("Select page", tabs)

    # Display content based on selected tab
    if selected_tab == "Collect data":
        collect_data_tab()
    elif selected_tab == "Results":
        results_tab()
    elif selected_tab == "Historical data":
        historical_data_tab()

if __name__ == "__main__":
    main()
