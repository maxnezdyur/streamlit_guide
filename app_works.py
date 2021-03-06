import streamlit as st
import numpy as np

# from bokeh.plotting import figure
import plotly.graph_objects as go


def main():
    x1 = np.array([0] * 6)
    x2 = np.linspace(0, 45, 9)
    x = np.concatenate((x1, x2))
    y1 = np.linspace(0, -25, 5)
    y2 = np.linspace(-25, 35, 10)
    y = np.concatenate((y1, y2))
    z1 = np.linspace(0, -10, 7)
    z2 = np.linspace(-10, 25, 8)
    z = np.concatenate((z1, z2))
    x = running_mean(x, 4)
    y = running_mean(y, 4)
    z = running_mean(z, 4)
    color = np.abs(x) + 1000 * np.abs(y) + np.abs(z) + 100

    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])

    if page == "Homepage":
        st.header("Finite Element Analysis of FAI")
        st.write(
            "Enter at your own peril. The material ahead will be interesting, confusing, and really cool. I hope you enjoy it as much as I did."
        )

    elif page == "Exploration":
        st.title("Data Exploration")
        visualize_data(x, y, z, color)


def running_mean(l, N):
    sum = 0
    result = list(0 for x in l)

    for i in range(0, N):
        sum = sum + l[i]
        result[i] = sum / (i + 1)

    for i in range(N, len(l)):
        sum = sum - l[i - N] + l[i]
        result[i] = sum / N

    return result


def visualize_data(x, y, z, c):
    # p = figure(plot_width=400, plot_height=400)
    # # add a circle renderer with a size, color, and alpha
    # p.circle(x, y, size=20, color="navy", alpha=0.5)
    # # show the results
    # st.write(p)
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=x,
                y=y,
                z=z,
                mode="lines+markers",
                marker=dict(
                    size=4,
                    color=c,  # set color to an array/list of desired values
                    colorscale="Picnic",  # choose a colorscale
                    opacity=0.8,
                ),
            )
        ],
        layout=go.Layout(
            title="Femoral Head Rotation during Activity",
            xaxis=dict(title="Flexion/Extension Angle"),
            yaxis=dict(title="Adduction/Abduction Angle"),
            width=1000,
            height=500,
        ),
    )
    st.write(fig)


if __name__ == "__main__":
    main()

