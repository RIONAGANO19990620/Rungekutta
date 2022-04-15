from enum import Enum


class ViewTerm(Enum):
    du_dx = r"\frac{\partial u}{\partial x}"
    d2u_dx2 = r"\frac{\partial^2 u}{\partial x^2}"
#    u_d2u_dx2 = r"u \frac{\partial^2 u}{\partial x^2}"
    d3u_dx3 = r"\frac{\partial^3 u}{\partial x^3}"
#    u_d3u_dx3 = r"u \frac{\partial^3 u}{\partial x^3}"
    u_du_dx = r"u \frac{\partial u}{\partial x}"
