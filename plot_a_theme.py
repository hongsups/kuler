
# coding: utf-8

# In[ ]:

"""Collection of functions for plotting a kuler theme in Lab space"""

def col_tuple2list(colormath_color):
    """Convert colormath to list"""
    color_list = []
    for i in range(3):
        color_list.append(colormath_color.get_value_tuple()[i])
    return color_list

def plot_scheme(schemeIdx,index1=0,index2=0):
    """ The 5 colors in each theme will be shown in a 3D space. 
        To show the ordinal properties of the colors, colors are connected with lines 
        Distance between colors is shown as text. 
        The first color is shown as a regular triangle.
        The last color is shown as an inverted triangle.
        The rest are shown as circles. """

    from mpl_toolkits.mplot3d import axes3d, Axes3D
    from colormath import color_diff
    from colormath.color_objects import LabColor, sRGBColor
    from colormath.color_conversions import convert_color
    
    # viewpoint
    if index1 == 'a' and index2 == 'b':
        el = 90
        az = -90
    elif index1 == 'L' and index2 == 'a':
        el = 0
        az = 90
    elif index1 == 'L' and index2 == 'b':
        el = 0
        az = 180
    elif int(index1) == 0 and int(index2) == 0:
        el = None
        az = None
        
    # draw a figure
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')

    # loop over the colors in a scheme
    for i in range(5):
        # df_ already has cm format(ex. Lab1) and list format (ex. L1, a1...)

        # 1. conver Lab color to sRGB for assigning colors for the plot
        LabColor_cm = df_['Lab'+str(i+1)][schemeIdx]
        sRGBColor_cm = convert_color(LabColor_cm,sRGBColor)

        # 2. convert this value to list for plotting
        sRGBColor_list = col_tuple2list(sRGBColor_cm)
        r = min(sRGBColor_list[0],1)
        g = min(sRGBColor_list[1],1)
        b = min(sRGBColor_list[2],1)
        color = np.array([[r,g,b],[0,0,0]])

        # 3. load the Lab coordinates
        L = df_['L'+str(i+1)][schemeIdx]
        a = df_['a'+str(i+1)][schemeIdx]
        b = df_['b'+str(i+1)][schemeIdx]        

        # 4. draw each color (first: triangle, last: reversed triangle, in-betweens: circle)
        marker_vec = ['^','o','o','o','v']
        ax.scatter(a,b,L,c=color,s=250,marker=marker_vec[i])
            
        # 5. draw lines between dots
        if i > 0:
            L_prev = df_['L'+str(i)][schemeIdx]
            a_prev = df_['a'+str(i)][schemeIdx]
            b_prev = df_['b'+str(i)][schemeIdx]        
            ax.plot([a_prev,a],[b_prev,b],[L_prev,L],color='black',alpha=0.2)

            # 6. compute distance between dots
            LabColor_cm_prev = LabColor(L_prev,a_prev,b_prev)
            diff = color_diff.delta_e_cie2000(LabColor_cm,LabColor_cm_prev)
            ax.text((a_prev+a)/2,(b_prev+b)/2,(L_prev+L)/2,'%.1f' %diff,(1,0,0))
            
    # view angle
    ax.view_init(elev=el,azim=az)

    # labels
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_zlabel('L')
    ax.set_xlim3d(-128, 128)
    ax.set_ylim3d(-128, 128)
    ax.set_zlim3d(0, 100)
    # show theme name and number of likes
    ax.set_title('#'+str(schemeIdx)+':'+df.name[schemeIdx]+' ('+str(df.Likes[schemeIdx])+')')

def plot_color_in_scheme(df_input,ax,colorIdx,schemeIdx,index1=0,index2=0):

    from mpl_toolkits.mplot3d import axes3d, Axes3D
    from colormath import color_diff
    from colormath.color_objects import LabColor, sRGBColor
    from colormath.color_conversions import convert_color
    
    # viewpoint
    if index1 == 'a' and index2 == 'b':
        el = 90
        az = -90
    elif index1 == 'L' and index2 == 'a':
        el = 0
        az = 90
    elif index1 == 'L' and index2 == 'b':
        el = 0
        az = 180
    elif int(index1) == 0 and int(index2) == 0:
        el = None
        az = None
        
        # 1. conver Lab color to sRGB for assigning colors for the plot
        LabColor_cm = df_input['Lab'+str(colorIdx)][schemeIdx]
        sRGBColor_cm = convert_color(LabColor_cm,sRGBColor)

        # 2. convert this value to list for plotting
        sRGBColor_list = col_tuple2list(sRGBColor_cm)
        r = min(sRGBColor_list[0],1)
        g = min(sRGBColor_list[1],1)
        b = min(sRGBColor_list[2],1)
        color = np.array([[r,g,b],[0,0,0]])

        # 3. load the Lab coordinates
        L = df_input['L'+str(colorIdx)][schemeIdx]
        a = df_input['a'+str(colorIdx)][schemeIdx]
        b = df_input['b'+str(colorIdx)][schemeIdx]        

        # 4. draw each color (first: triangle, last: reversed triangle, in-betweens: circle)
        ax.scatter(a,b,L,c=color,s=250,marker='o')
            
    # view angle
    ax.view_init(elev=el,azim=az)

    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_zlabel('L')
    ax.set_xlim3d(-128, 128)
    ax.set_ylim3d(-128, 128)
    ax.set_zlim3d(0, 100)


# In[ ]:



