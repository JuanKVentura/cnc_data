import streamlit as st

def collect_data_tab():
    st.write("## Collect Data")

    col1, col2 = st.columns([2, 1])

    
    # Left column with an image
    col1.image("test_image.png", use_column_width=True)
    # Right column with input rows

    with col2:
        dimension_a=st.text_input("Dimension A", "")


def results_tab():
    st.write("## Results")

def historical_data_tab():
    st.write("## Historical Data")

def main():
    st.title("CNC data")
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    # Create tabs
    tabs = ["Collect data", "Results", "Historical data"]
    selected_tab = st.sidebar.radio("Select Tab", tabs)

    # Display content based on selected tab
    if selected_tab == "Collect data":
        collect_data_tab()
    elif selected_tab == "Results":
        results_tab()
    elif selected_tab == "Historical data":
        historical_data_tab()

if __name__ == "__main__":
    main()
