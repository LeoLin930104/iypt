import math
from matplotlib import pyplot

# Import Function
def import_data(filedir: str) -> list:
    f = open(filedir, "r")
    t = f.readline()
    t = t[:len(t)-1]
    arr = []
    for x in f: arr.append(float(x[:len(x)-1]))
    return arr

# Display Function
def display(title: str, xlabel: str, ylabel: str, X: list, Y: list):
    pyplot.title(title)
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)
    pyplot.plot(X, Y)
    pyplot.show()

# Calculate Magnitude
def magnitude(T: list, X: list, Y: list) -> list:
    R = []
    for i, t in enumerate(T): R.append(math.sqrt(X[i]**2+Y[i]**2))
    return R

# Calculate Rotational Angle
def angle(T: list, X: list, Y: list) -> list:
    A = []
    for i, t in enumerate(T):
        if X[i] > 0 and Y[i] >= 0:
            A.append( math.degrees( math.atan2( Y[i], X[i] ) ) )
        elif X[i] < 0 and Y[i] >= 0:
            A.append( math.degrees( math.atan2( Y[i], X[i] ) ) )
        elif X[i] < 0 and Y[i] <= 0:
            A.append( math.degrees( math.atan2( Y[i], X[i] ) ) )
        elif X[i] > 0 and Y[i] <= 0:
            A.append( math.degrees( math.atan2( Y[i], X[i] ) ) )
        else:
            print("Error In Angle Calculation: Break...")
            break
    return A

# Calculate Continuous Rotational Angle 
def rotational_angle(A: list) -> list:
    RA = []
    step = 0
    for i, x in enumerate(A):
        RA.append(A[i] - 360 * step)
        if i == len(A)-1: break
        elif x < A[i+1]: step += 1
    return RA

# Calculate Theta Correspond to Radius
def theta(R: list, RADIUS: float) -> list:
    Th = []
    for i, r in enumerate(R):
        Th.append( math.degrees( math.asin( r/RADIUS ) ) )
    return Th

# Writing Data into New File
def write_data(title: str, data: list, filedir: str) -> None:
    f = open(filedir, 'w')
    f.write(title + "\n")
    for d in data: f.write(str(d) + "\n")
