

def steradian(theta1, theta2, phi1, phi2,**kwargs):
    from scipy.integrate import quad
    from numpy import radians, sin

    '''
    theta1,theta 2 - Polar angle, in radians. Valid from -90 to 90 degrees, if kwarg "useDeg == True".
    phi1,phi 2 - Azimuthal angle, in radians. Valid from -180 to 180 degrees, if kwarg "useDeg == True". 
    '''


    # assumes values are in radians unless otherwise specified
    useDeg = kwargs.get('useDeg', '')
    if useDeg:
        theta1, theta2, phi1, phi2 = radians(theta1),radians(theta2),radians(phi1),radians(phi2)

    steradianVal = (phi2-phi1)*quad(lambda  x:sin(x), theta1,theta2)[0]

    return steradianVal