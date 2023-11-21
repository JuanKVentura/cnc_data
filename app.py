import streamlit as st

def main():
    st.title("Embedded Content")

    # Embedding the iframe
    st.markdown(
        '<iframe src="https://lumalabs.ai/embed/94b0a14b-7f81-4485-a035-691631f929c1?mode=video&background=%23ffffff&color=%23000000&showTitle=true&loadBg=true&logoPosition=bottom-left&infoPosition=bottom-right&cinematicVideo=undefined&showMenu=false" width="376" height="500" frameborder="0" title="luma embed" style="border: none;"></iframe>',
        unsafe_allow_html=True
    )

    st.markdown("---")  # Add a horizontal line for separation

    # Displaying the PDF
    pdf_url = "https://iweb.palliser.ca/pfurn/mfgengineering/Work%20Instructions%20%20Mexico/WI%20ARMADO%20APEX.pdf"
    st.markdown(f'<iframe src="{pdf_url}" width="100%" height="600px" style="border: none;"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
