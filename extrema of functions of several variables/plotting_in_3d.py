import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from mpl_toolkits import mplot3d


def get_dot_from_user(x_interval, y_interval):
    print("Coordinates of the starting point (x y), must be inside the segments x = [%d, %d], y = [%d, %d].\n"
          "Enter the coordinates of the starting point (x y), separated by a space: "
          % (x_interval[0], x_interval[1], y_interval[0], y_interval[1]))
    return input().split(" ")


def f(x, y):
    return x ** 3 - 12 * x * y + 8 * y ** 3


def create_empty3d_axis():
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    return ax


def plot_3d_surface(ax, number_of_dots_on_axis, x_interval, y_interval, color_mode, zorder):
    x = np.outer(np.linspace(x_interval[0], x_interval[1], number_of_dots_on_axis), np.ones(number_of_dots_on_axis))
    y = np.outer(np.linspace(y_interval[0], y_interval[1], number_of_dots_on_axis), np.ones(number_of_dots_on_axis)).T
    z = f(x, y)
    ax.plot_surface(x, y, z, cmap=color_mode, zorder = zorder)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("$x^3 - 12xy + 8y^3$")


def plot_3d_section(ax, x_interval, y_interval, z_interval, color, zorder):
    ax.plot3D(x_interval, y_interval, z_interval, color, zorder = zorder)


def plot_3d_level_surface(ax, level, x_interval, y_interval, color, alpha, zorder):
    ax.plot_surface(np.outer(x_interval, np.ones(2)), np.outer(y_interval, np.ones(2)).T,
                    np.outer([level, level], np.ones(2)), color=color, alpha=alpha, zorder = zorder)


def plot_3d_dot(ax, x, y, z, color, marker, edgecolor, zorder):
    ax.scatter(x, y, z, color=color, marker=marker, edgecolor=edgecolor, zorder = zorder)


def main():
    # mpl.use('TkAgg')  # for interactive 3-D graph using PyCharm

    axis = create_empty3d_axis()

    # ax.set_zlim(-9,1) # setting limit at z axis

    plot_3d_surface(axis, 1000, [-0.5, 2.5], [-0.5, 1.5], "plasma", 1)
    plot_3d_level_surface(axis, 0, [-0.5, 2.5], [-0.5, 1.5], "green", 0.5, 2)
    plot_3d_level_surface(axis, -8, [-0.5, 2.5], [-0.5, 1.5], "red", 0.5, 2)
    plot_3d_section(axis, [0, 0], [0, 0], [-9, 0], "gray", 4)
    plot_3d_section(axis, [2, 2], [1, 1], [-9, -8], "gray", 4)
    plot_3d_dot(axis, 0, 0, f(0, 0), "yellow", "^", "black", 3)
    plot_3d_dot(axis, 2, 1, f(2, 1), "yellow", "^", "black", 3)

    plt.show()


if __name__ == "__main__":
    main()
