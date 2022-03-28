import streamlit as st


def main():
    n = st.number_input(label='What is your favorite number?',
                        value=42,
                        )
    st.write('input: ', n)


if __name__ == '__main__':
    main()
