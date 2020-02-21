import streamlit as st
import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import math
import matplotlib.colors as colors


@st.cache
def pelv_upload():
    pelv = mesh.Mesh.from_file("pelv_origin_2.stl")
    return pelv


def fem_upload():
    fem = mesh.Mesh.from_file("fem_origin_2.stl")
    return fem


def main():

    pelv_data = pelv_upload()
    fem_data = fem_upload()

    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])

    if page == "Homepage":
        st.header("Finite Element Analysis of FAI")
        st.write("Enter at your own peril.")

    elif page == "Exploration":
        st.title("Data Exploration")
        angle = st.slider("Rotate Femur", -30, 15, 0)
        view1 = st.slider("Rotate Graph", -30, 30, 0)
        view2 = st.slider("Rotate Graph", 45, 135, 90)
        fem_data.rotate([0.0, 0.5, 0.0], math.radians(angle))
        visualize_data(fem_data, pelv_data, view1, view2)


def rotate_fem(angle, fem):
    new_fem = fem.rotate([0.0, 0.5, 0.0], math.radians(angle))
    return new_fem


def visualize_data(fem, pelv, view1, view2):
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)
    axes.auto_scale_xyz([-100, 100], [-100, 100], [-100, 100])
    axes.view_init(view1, view2)
    fem_plot = mplot3d.art3d.Poly3DCollection(fem.vectors)
    fem_plot.set_color(colors.rgb2hex([0.9, 0.6, 0.0]))
    axes.add_collection3d(fem_plot)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(pelv.vectors))

    st.write(figure)


if __name__ == "__main__":
    main()

