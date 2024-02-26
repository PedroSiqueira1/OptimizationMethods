import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import animation
from functions import *


def generate_himmelblau_gif(data_points_1, initial_point_1, data_points_2, initial_point_2):

    fig1 = plt.figure(figsize = (16,32), dpi = 300)
    ax1 = fig1.add_subplot(111, projection='3d')

    a, b = np.mgrid[-6:6:81j, -6:6:81j]

    
    newax = fig1.add_axes(ax1.get_position(), projection='3d',
                        xlim = ax1.get_xlim(),
                        ylim = ax1.get_ylim(),
                        zlim = ax1.get_zlim(),
                        facecolor = 'none',)
    newax.view_init(azim= 120, elev= 37)
    newax.set_zorder(1)
    ax1.set_zorder(0)


    data_points_1 = np.array(data_points_1)
    data_points_2 = np.array(data_points_2)

    result1 = [ himmelblau(x) for x in data_points_1]
    result2 = [ himmelblau(x) for x in data_points_2]

    newax.plot3D(data_points_1[:,0], data_points_1[:, 1], result1[:], 
                c='blue', alpha = 0.7)
    newax.plot3D(data_points_2[:, 0], data_points_2[:, 1], result2[:],
                c='red', alpha = 0.7)

    newax.plot3D(data_points_1[0, 0], data_points_1[0, 1], result1[0],
                ms = 2.5, c='black', marker='o')
    newax.plot3D(data_points_2[0, 0], data_points_2[0, 1], result2[0],
                ms = 2.5, c='black', marker='s')
    newax.set_axis_off()
    cir = u'■'
    sq = u'●'
    ax1.text2D(0.05, 0.95, f'Initilization\n'\
                        f'{sq}: x = {initial_point_1[0]}, y = {initial_point_1[1]}\n'\
                        f'{cir}: x = {initial_point_2[0]}, y = {initial_point_2[1]}', transform=ax1.transAxes)
                        
    def descent_animation(num):

        # Clear the axes where we are plotting the tracjectories
        newax.clear()
        
        # Manually adjust the order of the axes
        newax.set_zorder(1)
        ax.set_zorder(0)
        
        # Hide the axes in the front plane
        newax.set_axis_off()

        # Plot new frame of trajectory line for the symmetry case
        newax.plot3D(data_points_1[:num+1, 0], data_points_1[:num+1, 1],
                    result1[:num+1], c='blue', alpha = 0.7)
        # Updating Point Location
        newax.scatter(data_points_1[num, 0], data_points_1[num, 1], result1[num],
                s = 10, c='blue', marker='o', edgecolor = 'k', linewidth = 0.5)
        # Adding Constant Origin
        newax.plot3D(data_points_1[0, 0], data_points_1[0, 1], result1[0],
                ms = 2.5, c='black', marker='o')


        # Plot new frame of trajectory line for the offset case
        newax.plot3D(data_points_2[:num+1, 0], data_points_2[:num+1, 1],
                    result2[:num+1], c='red', alpha = 0.7)
        # Updating Point Location
        newax.scatter(data_points_2[num, 0], data_points_2[num, 1], result2[num],
                s = 10, c='red', marker='o', edgecolor = 'k', linewidth = 0.5)
        # Adding Constant Origin
        newax.plot3D(data_points_2[0, 0], data_points_2[0, 1], result2[0],
                ms = 2.5, c='black', marker='s')


        # Setting Axes Limits and view angles
        newax.set_xlim3d([-6, 6])
        newax.set_ylim3d([-6, 6])
        newax.set_zlim3d([0, 2000])
        newax.view_init(azim= 120, elev= 37)


    fig = plt.figure(figsize = (4, 3), dpi = 300)
    ax = fig.add_subplot(111, projection='3d')

    plot_args = {'rstride': 2, 'cstride': 2, 'cmap':"coolwarm",
                'linewidth': 0.01, 'antialiased': False,
                'vmin': 0, 'vmax': 1000, 'edgecolors':'k'}

    x, y = np.mgrid[-6:6:81j, -6:6:81j]

    # Plot surface
    ax.plot_surface(x, y, himmelblau([x,y]), **plot_args)
    ax.view_init(azim= 120, elev= 37)
    ax.set_xlim3d([6, 6])
    ax.set_ylim3d([-6, 6])
    ax.set_zlim3d([0, 2000])

    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    # Add second pair of axes
    newax = fig.add_axes(ax.get_position(), projection='3d',
                        xlim = ax.get_xlim(),
                        ylim = ax.get_ylim(),
                        zlim = ax.get_zlim(),
                        facecolor = 'none',)
    newax.view_init(azim= 120, elev= 37)

    # Manually adjust the order of the axes
    newax.set_zorder(1)
    ax.set_zorder(0)

    # Hide axes in the front plane
    newax.set_axis_off()

    # Add some text to distinguish the two initialization points
    cir = u'■'
    sq = u'●'
    ax.text2D(0.05, 0.95, f'Initilization\n'\
                        f'{sq}: x = {initial_point_1[0]}, y = {initial_point_1[1]}\n'\
                        f'{cir}: x = {initial_point_2[0]}, y = {initial_point_2[1]}',  
            transform=ax.transAxes,
            fontsize = 8)

    # Plotting the Animation
    line_ani = animation.FuncAnimation(fig, descent_animation, interval=1,
                                    frames= min(len(data_points_1), len(data_points_2)), repeat = False)
    plt.show()

    filename = "gifs/gradient_himmelblau.gif"
    writergif = animation.PillowWriter(fps=60)
    line_ani.save(filename, writer=writergif)

def generate_rosenbrock_gif(data_points_1, initial_point_1, data_points_2, initial_point_2):

    fig1 = plt.figure(figsize = (16,32), dpi = 300)
    ax1 = fig1.add_subplot(111, projection='3d')

    a, b = np.mgrid[-2:2:81j, -2:2:81j]

    
    newax = fig1.add_axes(ax1.get_position(), projection='3d',
                        xlim = ax1.get_xlim(),
                        ylim = ax1.get_ylim(),
                        zlim = ax1.get_zlim(),
                        facecolor = 'none',)
    newax.view_init(azim= 120, elev= 37)
    newax.set_zorder(1)
    ax1.set_zorder(0)


    data_points_1 = data_points_1[1::50]
    data_points_2 = data_points_2[1::50]


    data_points_1 = np.array(data_points_1)
    data_points_2 = np.array(data_points_2)




    result1 = [ rosenbrock(x, 2) for x in data_points_1]
    result2 = [ rosenbrock(x, 2) for x in data_points_2]

    newax.plot3D(data_points_1[:,0], data_points_1[:, 1], result1[:], 
                c='blue', alpha = 0.7)
    newax.plot3D(data_points_2[:, 0], data_points_2[:, 1], result2[:],
                c='red', alpha = 0.7)

    newax.plot3D(data_points_1[0, 0], data_points_1[0, 1], result1[0],
                ms = 2.5, c='black', marker='o')
    newax.plot3D(data_points_2[0, 0], data_points_2[0, 1], result2[0],
                ms = 2.5, c='black', marker='s')
    newax.set_axis_off()
    cir = u'■'
    sq = u'●'
    ax1.text2D(0.05, 0.95, f'Initilization\n'\
                        f'{sq}: x = {initial_point_1[0]}, y = {initial_point_1[1]}\n'\
                        f'{cir}: x = {initial_point_2[0]}, y = {initial_point_2[1]}', transform=ax1.transAxes)

    def descent_animation(num):



        # Clear the axes where we are plotting the tracjectories
        newax.clear()
        
        # Manually adjust the order of the axes
        newax.set_zorder(1)
        ax.set_zorder(0)
        
        # Hide the axes in the front plane
        newax.set_axis_off()

        # Plot new frame of trajectory line for the symmetry case
        newax.plot3D(data_points_1[:num+1, 0], data_points_1[:num+1, 1],
                    result1[:num+1], c='blue', alpha = 0.7)
        # Updating Point Location
        newax.scatter(data_points_1[num, 0], data_points_1[num, 1], result1[num],
                s = 10, c='blue', marker='o', edgecolor = 'k', linewidth = 0.5)
        # Adding Constant Origin
        newax.plot3D(data_points_1[0, 0], data_points_1[0, 1], result1[0],
                ms = 2.5, c='black', marker='o')


        # Plot new frame of trajectory line for the offset case
        newax.plot3D(data_points_2[:num+1, 0], data_points_2[:num+1, 1],
                    result2[:num+1], c='red', alpha = 0.7)
        # Updating Point Location
        newax.scatter(data_points_2[num, 0], data_points_2[num, 1], result2[num],
                s = 10, c='red', marker='o', edgecolor = 'k', linewidth = 0.5)
        # Adding Constant Origin
        newax.plot3D(data_points_2[0, 0], data_points_2[0, 1], result2[0],
                ms = 2.5, c='black', marker='s')


        # Setting Axes Limits and view angles
        newax.set_xlim3d([-2, 2])
        newax.set_ylim3d([-2, 2])
        newax.set_zlim3d([0, 2000])
        newax.view_init(azim= 120, elev= 37)


    fig = plt.figure(figsize = (4, 3), dpi = 300)
    ax = fig.add_subplot(111, projection='3d')

    plot_args = {'rstride': 2, 'cstride': 2, 'cmap':"coolwarm",
                'linewidth': 0.01, 'antialiased': False,
                'vmin': 0, 'vmax': 1000, 'edgecolors':'k'}

    x, y = np.mgrid[-2:2:81j, -2:2:81j]

    # Plot surface
    ax.plot_surface(x, y, rosenbrock([x,y], 2), **plot_args)
    ax.view_init(azim= 120, elev= 37)
    ax.set_xlim3d([-2, 2])
    ax.set_ylim3d([-2, 2])
    ax.set_zlim3d([0, 2000])

    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    # Add second pair of axes
    newax = fig.add_axes(ax.get_position(), projection='3d',
                        xlim = ax.get_xlim(),
                        ylim = ax.get_ylim(),
                        zlim = ax.get_zlim(),
                        facecolor = 'none',)
    newax.view_init(azim= 120, elev= 37)

    # Manually adjust the order of the axes
    newax.set_zorder(1)
    ax.set_zorder(0)

    # Hide axes in the front plane
    newax.set_axis_off()

    # Add some text to distinguish the two initialization points
    cir = u'■'
    sq = u'●'
    ax.text2D(0.05, 0.95, f'Initilization\n'\
                        f'{sq}: x = {initial_point_1[0]}, y = {initial_point_1[1]}\n'\
                        f'{cir}: x = {initial_point_2[0]}, y = {initial_point_2[1]}', 
            transform=ax.transAxes,
            fontsize = 8)

    # Plotting the Animation
    line_ani = animation.FuncAnimation(fig, descent_animation, interval=1,
                                    frames= min(len(data_points_1), len(data_points_2)), repeat = False)
    plt.show()

    filename = "gifs/gradient_rosenbrock.gif"
    writergif = animation.PillowWriter(fps=60)
    line_ani.save(filename, writer=writergif)
