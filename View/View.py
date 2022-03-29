from typing import Dict

import streamlit as st

from ViewModel.ViewModel import ViewModel
from ViewModel.ViewTerm import ViewTerm


class View:

    @staticmethod
    def __get_mathematical_expression(term_dict) -> str:
        formula = r'\frac{\partial u}{\partial t}='
        for term in term_dict:
            if term_dict[term] != 0:
                formula += str(term_dict[term]) + term.value + '+'
        return formula[:-1]

    @staticmethod
    def __create_side_menu() -> Dict[ViewTerm, float]:
        # sidebarにおけるパラメータ設定
        st.sidebar.markdown('Set Parameter')
        term_dict: Dict[ViewTerm, float] = {}
        num = 0
        for term in ViewTerm:
            num += 1
            st.sidebar.latex(term.value)
            term_num = st.sidebar.number_input('上の項の係数を入力してください({})'.format(num))
            term_dict[term] = term_num
        return term_dict

    @staticmethod
    def __create_plot(term_dict: Dict[ViewTerm, float]):
        view_model = ViewModel(term_dict)
        fig = view_model.create_fig()

        st.subheader('Calculation Result')
        st.pyplot(fig)

    @staticmethod
    def create_view() -> None:
        term_dict = View.__create_side_menu()
        st.subheader('Mathematical expression')
        st.latex(View.__get_mathematical_expression(term_dict))
        View.__create_plot(term_dict)

