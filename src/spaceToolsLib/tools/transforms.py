# --- transforms.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the physics coordinate transformations I often use

# --- The Basic rotation matricies ---
from spaceToolsLib.variables.physicsVariables import Re
from numpy import array, cos, sin, matmul, radians, sqrt, arcsin
from math import sqrt,pow,atan2,cos,sin
def Rx(angle):
    """
    Build the 3x3 rotation matrix for a rotation about the X axis.

    Parameters
    ----------
    angle : float
        Rotation angle, in degrees.

    Returns
    -------
    numpy.ndarray
        3x3 rotation matrix.
    """

    angleRad = radians(angle)
    return array([[1,0,0],
                     [0,cos(angleRad),-sin(angleRad)],
                     [0,sin(angleRad),cos(angleRad)]])
def Ry(angle):
    """
    Build the 3x3 rotation matrix for a rotation about the Y axis.

    Parameters
    ----------
    angle : float
        Rotation angle, in degrees.

    Returns
    -------
    numpy.ndarray
        3x3 rotation matrix.
    """

    angleRad = radians(angle)
    return array([[cos(angleRad),0,sin(angleRad)],
                     [0,1,0],
                     [-sin(angleRad),0,cos(angleRad)]])
def Rz(angle):
    """
    Build the 3x3 rotation matrix for a rotation about the Z axis.

    Parameters
    ----------
    angle : float
        Rotation angle, in degrees.

    Returns
    -------
    numpy.ndarray
        3x3 rotation matrix.
    """
    angleRad = radians(angle)
    return array([[cos(angleRad),-sin(angleRad),0],
                     [sin(angleRad),cos(angleRad),0],
                     [0,0,1]])
def R_roll(angle):
    """
    Build the 3x3 rotation matrix for a roll rotation.

    Parameters
    ----------
    angle : float
        Roll angle, in degrees.

    Returns
    -------
    numpy.ndarray
        3x3 rotation matrix.
    """
    angleRad = radians(angle)
    return array([[1,                0,                0],
                     [0, cos(angleRad), sin(angleRad)],
                     [0,-sin(angleRad), cos(angleRad)]])
def R_pitch(angle):
    """
    Build the 3x3 rotation matrix for a pitch rotation.

    Parameters
    ----------
    angle : float
        Pitch angle, in degrees.

    Returns
    -------
    numpy.ndarray
        3x3 rotation matrix.
    """
    angleRad = radians(angle)
    return array([[cos(angleRad), 0, -1*sin(angleRad)],
                     [0,                1, 0],
                     [sin(angleRad), 0, cos(angleRad)]])
def R_yaw(angle):
    """
    Build the 3x3 rotation matrix for a yaw rotation.

    Parameters
    ----------
    angle : float
        Yaw angle, in degrees.

    Returns
    -------
    numpy.ndarray
        3x3 rotation matrix.
    """
    angleRad = radians(angle)
    return array([[cos(angleRad),    sin(angleRad), 0],
                     [-1*sin(angleRad), cos(angleRad), 0],
                     [0,                   0,                1]])

def DCM(roll,pitch,yaw):
    """
    Build the combined direction cosine matrix (DCM) from roll, pitch, and
    yaw angles, applied in yaw -> pitch -> roll order.

    Parameters
    ----------
    roll : float
        Roll angle, in degrees.
    pitch : float
        Pitch angle, in degrees.
    yaw : float
        Yaw angle, in degrees.

    Returns
    -------
    numpy.ndarray
        3x3 combined rotation matrix: R_yaw @ R_pitch @ R_roll.
    """
    return matmul(R_yaw(yaw),matmul(R_pitch(pitch),R_roll(roll)))

def ENUtoECEF(Lat,Long):
    """
    Build the 3x3 rotation matrix that transforms vectors from a local
    East-North-Up (ENU) frame to Earth-Centered, Earth-Fixed (ECEF)
    coordinates at a given latitude/longitude.

    Parameters
    ----------
    Lat : float
        Geodetic latitude, in degrees.
    Long : float
        Geodetic longitude, in degrees.

    Returns
    -------
    numpy.ndarray
        3x3 ENU-to-ECEF rotation matrix.
    """
    angleLat = radians(Lat)
    angleLong = radians(Long)

    R = array([
        [-sin(angleLong), -cos(angleLong)*sin(angleLat), cos(angleLong)*cos(angleLat)],
        [ cos(angleLong), -sin(angleLong)*sin(angleLat), sin(angleLong)*cos(angleLat)],
        [0,                               cos(angleLat),                sin(angleLat)]
    ])

    return R


def ECEF_to_Geodedic(x,y,z):

    '''
    Function to convert xyz ECEF to llh
    convert cartesian coordinate into geographic coordinate
    ellipsoid definition: WGS84
      a= 6,378,137m
      f= 1/298.257

    Input
      x: coordinate X meters
      y: coordinate y meters
      z: coordinate z meters
    Output
      lat: latitude rad
      lon: longitude rad
      h: height meters
    '''
    # --- WGS84 constants
    a = 6378137.0
    f = 1.0 / 298.257223563
    # --- derived constants
    b = a - f*a
    e = sqrt(pow(a,2.0)-pow(b,2.0))/a
    clambda = atan2(y,x)
    p = sqrt(pow(x,2.0)+pow(y,2))
    h_old = 0.0
    # first guess with h=0 meters
    theta = atan2(z,p*(1.0-pow(e,2.0)))
    cs = cos(theta)
    sn = sin(theta)
    N = pow(a,2.0)/sqrt(pow(a*cs,2.0)+pow(b*sn,2.0))
    h = p/cs - N
    while abs(h-h_old) > 1.0e-6:
        h_old = h
        theta = atan2(z,p*(1.0-pow(e,2.0)*N/(N+h)))
        cs = cos(theta)
        sn = sin(theta)
        N = pow(a,2.0)/sqrt(pow(a*cs,2.0)+pow(b*sn,2.0))
        h = p/cs - N
    llh = {'lon':clambda, 'lat':theta, 'height': h}
    return llh

def sphereToCartesian(r,theta,phi):
    """
    Build the 3x3 rotation matrix that transforms vectors from spherical
    (r, theta, phi) unit-vector components to Cartesian (x, y, z).

    Parameters
    ----------
    r : float
        Radial coordinate (unused in the rotation matrix itself, included
        for interface symmetry with spherical coordinates).
    theta : float
        Polar angle, in degrees.
    phi : float
        Azimuthal angle, in degrees.

    Returns
    -------
    numpy.ndarray
        3x3 spherical-to-Cartesian rotation matrix.
    """
    thetaRad = radians(theta)
    phiRad = radians(phi)

    R = array([
        [sin(thetaRad)*cos(phiRad), cos(thetaRad)*cos(phiRad), -sin(phiRad)],
        [sin(thetaRad)*sin(phiRad), cos(thetaRad)*sin(phiRad),  cos(phiRad)],
        [               cos(thetaRad),                sin(thetaRad),               0]
    ])
    return R

def Rotation3D(yaw, pitch, roll):
    """
    Build a combined 3D rotation matrix from yaw, pitch, and roll angles
    using a single closed-form expression (as opposed to DCM(), which
    composes Rx/Ry/Rz matrices via matrix multiplication).

    Parameters
    ----------
    yaw : float
        Yaw angle, in degrees.
    pitch : float
        Pitch angle, in degrees.
    roll : float
        Roll angle, in degrees.

    Returns
    -------
    numpy.ndarray
        3x3 combined rotation matrix.
    """

    yawR = radians(yaw)
    pitchR = radians(pitch)
    rollR = radians(roll)
    return array([[cos(yawR)*cos(pitchR), cos(yawR)*sin(pitchR)*sin(rollR) - sin(yawR)*cos(rollR), cos(yawR)*sin(pitchR)*cos(rollR) + sin(yawR)*sin(rollR) ], [sin(yawR)*cos(pitchR), sin(yawR)*sin(pitchR)*sin(rollR) + cos(yawR)*cos(rollR), sin(yawR)*sin(pitchR)*cos(rollR) - cos(yawR)*sin(rollR)], [-1*sin(pitchR), cos(pitchR)*sin(rollR), cos(pitchR)*cos(rollR)]])

def RotationAboutAxes(theta, axX,axY,axZ):
    """
    Build the 3x3 rotation matrix for a rotation by angle theta about an
    arbitrary axis (axX, axY, axZ), using the Rodrigues rotation formula.

    Parameters
    ----------
    theta : float
        Rotation angle, in degrees.
    axX, axY, axZ : float
        Components of the (unit) rotation axis vector.

    Returns
    -------
    numpy.ndarray
        3x3 rotation matrix about the given axis.
    """

    thetaR = radians(theta)
    return array([
    [cos(thetaR) + (axX*axX)*(1 - cos(thetaR)),    axX*axY*(1-cos(thetaR)) - axZ*sin(thetaR), axX*axZ*(1-cos(thetaR)) + axY*sin(thetaR)],
    [axY*axX*(1- cos(thetaR)) + axZ*sin(thetaR), cos(thetaR) + axY*axY*(1- cos(thetaR)),    axY*axZ*(1- cos(thetaR)) - axX*sin(thetaR)],
    [axZ*axX*(1- cos(thetaR)) - axY*sin(thetaR), axZ*axY*(1- cos(thetaR))+ axX*sin(thetaR), cos(thetaR)+axZ*axZ*(1- cos(thetaR))]
        ])

def GreatCircleDistance(lat1,lat2,long1,long2):
    """
    Compute the great-circle distance between two points on Earth's
    surface using the haversine formula.

    Parameters
    ----------
    lat1 : float
        Latitude of the first point, in degrees.
    lat2 : float
        Latitude of the second point, in degrees.
    long1 : float
        Longitude of the first point, in degrees.
    long2 : float
        Longitude of the second point, in degrees.

    Returns
    -------
    float
        Great-circle distance between the two points, in kilometers
        (using Earth's radius Re).
    """

    return 2*Re*arcsin(sqrt( sin(radians( (lat2-lat1)/2  ))**2 + cos(radians(lat1))*cos(radians(lat2))*sin(radians( (long2-long1)/2  ))**2  ))
