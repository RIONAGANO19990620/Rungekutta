from typing import Dict, List

import numpy as np
from matplotlib import pyplot as plt

from Model.Mesh import Mesh
from Model.RungeKutta import RungeKutta
from Model.Term.D1Dx import D1Dx
from Model.Term.D2Dx import D2Dx
from Model.Term.D3Dx import D3Dx
from Model.Term.Term import Term
from ViewModel.ViewTerm import ViewTerm


class ViewModel:
    X_max = 10
    X_mesh = 100
    T_max = 8
    T_change = 200
    mesh = Mesh(X_max, X_mesh, T_max, T_change)
    first_data = np.exp(-(mesh.x_array - mesh.X_max // 2) ** 2 / 4)

    def __init__(self, term_dict: Dict[ViewTerm, float]):
        self.term_dict = term_dict

    def create_fig(self):
        fig = plt.figure(figsize=(20, 10))
        title = 'calculate_result'
        term_list = ViewModel.__create_term(self.term_dict)
        data = RungeKutta.solve(term_list, ViewModel.first_data, ViewModel.mesh.T_mesh, ViewModel.mesh.T_change,
                                ViewModel.mesh.dt, ViewModel.mesh.dx)
        RungeKutta.plot(data, ViewModel.mesh.t_array, ViewModel.mesh.x_array, title)
        plt.legend()
        plt.rcParams["font.size"] = 25
        return fig

    @staticmethod
    def __create_term(term_dict) -> List[Term]:
        term_list = []
        for term in term_dict:
            num = term_dict[term]
            if term is ViewTerm.du_dx:
                term_instance = D1Dx(num)
            elif term is ViewTerm.u_du_dx:
                term_instance = D1Dx(num, True)
            elif term is ViewTerm.d2u_dx2:
                term_instance = D2Dx(num)
            elif term is ViewTerm.u_d2u_dx2:
                term_instance = D2Dx(num, True)
            elif term is ViewTerm.d3u_dx3:
                term_instance = D3Dx(num)
            elif term is ViewTerm.u_d3u_dx3:
                term_instance = D3Dx(num, True)
            else:
                raise ValueError
            term_list.append(term_instance)
        return term_list
