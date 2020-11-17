import bead_dynamics_funcs as bda

# Utilizing Functions to make Analysis to Data, and Write into new Files
def process(i: int, j: int):
    RADIUS = [0.125, 0.15, 0.175]
    filedir = "C:\Development\pythonwork\\Tracker\\{}-{}\\{}.txt"

    t_title, T = "Time", []
    x_title, X = "X-coordinate", []
    y_title, Y = "Y-coordinate", []
    r_title, R = "Magnitude", []
    a_title, A = "Angle", []
    ra_title, RA = "Rotational Angle", []
    th_title, Th = "Theta", []

    T = bda.import_data(filedir.format(i, j, 't'))
    X = bda.import_data(filedir.format(i, j, 'x'))
    Y = bda.import_data(filedir.format(i, j, 'y'))
    R = bda.magnitude(T, X, Y)
    A = bda.angle(T, X, Y)
    RA = bda.rotational_angle(A)
    Th = bda.theta(R, RADIUS[i-1])
    bda.write_data('r', R, filedir.format(i, j, 'r'))
    bda.write_data('a', A, filedir.format(i, j, 'a'))
    bda.write_data('ra', RA, filedir.format(i, j, 'ra'))
    bda.write_data('th', Th, filedir.format(i, j, 'th'))

    analyze(T, R, A, RA, Th, i, j)

def analyze(T: list, R:list, A: list, RA: list, Th: list, i:int, j: int):
    am_title, am = "Average Magnitude", sum(R) / float(len(R))
    aav_title, aav = "Average Angular Velocity", min(RA) / max(T)
    ath_title, ath = "Average Theta", sum(Th) / float(len(Th))
    data = [(am_title, am), (aav_title, aav), (ath_title, ath)]

    filedir = "C:\Development\pythonwork\\Tracker\\{}-{}\\{}.txt"
    bda.write_data('Post-process Analysis', data, filedir.format(i, j, 'analysis'))

# Execution
if __name__ == "__main__":
    for i in range(3): 
        for j in range(3): 
            process(i+1, j+1)