import bead_dynamics_funcs as bda
import math

# Data Required pre-analysis and post-analysis
RADIUS = [0.1, 0.125, 0.15]
RADIUS_B = 0.79
t_title, T = "Time", []
x_title, X = "X-coordinate", []
y_title, Y = "Y-coordinate", []
r_title, R = "Magnitude", []
a_title, A = "Angle", []
ra_title, RA = "Rotational Angle", []
th_title, Th = "Theta", []
am_title, am = "Average Magnitude", 0
aav_title, aav = "Average Angular Velocity", 0
ath_title, ath = "Average Theta", 0
data = []
# File Directory format of File
filedir = "C:\Development\pythonwork\iypt\\bead_dynamics\\{}-{}\\{}.txt"

# Utilizing Functions to make Analysis to Data, and Write into new Files
def process(i: int, j: int):

    # Data Import from text files 
    T = bda.import_data(filedir.format(i, j, 't'))
    X = bda.import_data(filedir.format(i, j, 'x'))
    Y = bda.import_data(filedir.format(i, j, 'y'))

    # Calculations by function in bead_dynamics_funcs.py
    R = bda.magnitude(T, X, Y)
    A = bda.angle(T, X, Y)
    RA = bda.rotational_angle(A)
    Th = bda.theta(R, RADIUS[i-1], RADIUS_B)
    am = sum(R) / float(len(R))
    aav = min(RA) / max(T)
    ath = sum(Th) / float(len(Th))
    data = [am, aav, ath]

    # Write Processed Data into Text Files
    bda.write_data('r', R, filedir.format(i, j, 'r'))
    bda.write_data('a', A, filedir.format(i, j, 'a'))
    bda.write_data('ra', RA, filedir.format(i, j, 'ra'))
    bda.write_data('th', Th, filedir.format(i, j, 'th'))
    bda.write_data('Post-process Analysis', data, filedir.format(i, j, 'analysis'))

# Collect am, aav, ath into a list for ploting
def collect_plot_data() -> list:
    data = []
    for i in range(3):
        am = []
        aav = []
        ath = []
        for j in range(3):
            f = open(filedir.format(i+1, j+1, 'analysis'))
            title = f.readline()
            title = title[:len(title)-1]
            temp = f.readline()
            am.append(float(temp[:len(temp)-1]))
            temp = f.readline()
            aav.append(math.radians( abs( float( temp[:len(temp)-1] ) ) ) )
            temp = f.readline()
            ath.append(float(temp[:len(temp)-1]))
            f.close()
        data.append((am, aav, ath))
    return data

if __name__ == "__main__":
    for i in range(3):
        for j in range(3):
            process(i+1, j+1)
    data = collect_plot_data()
    for i in range(3): 
        bda.set_display(RADIUS[i],"average angular veloctiy, rad/s","average theta, degree",data[i][1], data[i][2])
    bda.show_display()
