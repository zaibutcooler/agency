import streamlit as st
from agency import Agency



def main():
    agency = Agency()
    st.title("Agency xD")

    feature = st.sidebar.radio(
        "Select feature:",
        (
            "Feature One",
            "Feature Two",
        ),
    )


if __name__ == "__main__":
    main()
