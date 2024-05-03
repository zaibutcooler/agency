import streamlit as st


def main():
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
