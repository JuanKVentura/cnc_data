import streamlit as st
import pandas as pd
import datetime


data_file_path = "data.csv"
try:
    df = pd.read_csv(data_file_path)
    data_load_failed=False
except FileNotFoundError:
    # Create an empty DataFrame if the file doesn't exist
    data_load_failed=True

def collect_data_tab():
    s1=st.expander("Sample 1", expanded=False)
    
    s1.write("## Collect Data")

    col1, col2 = s1.columns([2, 1])
    
    # Left column with an image
    col1.image("sample1.jpg", width=400)
    # Right column with input rows
    with col2:
        dimension_1a = st.text_input("Dimension A", "")
        dimension_2a = st.text_input("Dimension B", "")
        dimension_3a = st.text_input("Dimension C", "")
        if st.button("Save data"):
            time_stamp=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            df2 = pd.DataFrame(
            {
                "Time_stamp": [time_stamp, time_stamp, time_stamp],
                "Dimension": ["1A","1B", "1C"],
                "Value": [dimension_1a, dimension_2a, dimension_3a]
            })
            df_appended=pd.concat([df,df2])
            df_appended.to_csv(data_file_path, index=False)
            st.success("Data appended successfully!")

def results_tab():
    st.write("## Results")

def historical_data_tab():
    st.write("## Historical Data")
    st.write(df)
def main():
    st.set_page_config(layout="wide")
    st.title("CNC data")
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            #GithubIcon {
              visibility: hidden;
                }
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    # Initialize connection.
    try:
        conn = st.connection('mysql', type='sql')
        st.sucess("DB connection OK")
        
    # Perform query.
    df = conn.query('SELECT * from CNCDATA;', ttl=600)
    
    # Print results.
    for row in df.itertuples():
        st.write(f"{row.time_stamp} has a value {row.dimension} of {row.value}")
    
    if data_load_failed:
        st.write("data could not be loaded please contact your app admin")
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
