import streamlit as st

def collect_data_tab():
    st.write("## Collect Data")
    st.sidebar.text("Sidebar content for Collect Data tab")

    # Left column with an image
    st.image("test_image.png", use_column_width=True)

    # Right column with input rows
    st.write("### Input Rows")
    dimension_a = st.text_input("Dimension A", "")
    dimension_b = st.text_input("Dimension B", "")
    dimension_c = st.text_input("Dimension C", "")
    dimension_d = st.text_input("Dimension D", "")

def results_tab():
    st.write("## Results")
    st.sidebar.text("Sidebar content for Results tab")
    # Add your code for the Results tab here

def historical_data_tab():
    st.write("## Historical Data")
    st.sidebar.text("Sidebar content for Historical Data tab")
    # Add your code for the Historical Data tab here

def main():
    st.title("Streamlit App with Tabs")

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
