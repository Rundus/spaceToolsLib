# --- transforms.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the physics coordinate transformations I often use

# --- The Basic rotation matricies ---
from spaceToolsLib.variables.physicsVariables import Re
from numpy import array, cos, sin, matmul, radians, sqrt, arcsin
from math import sqrt,pow,atan2,cos,sin
def Rx(angle):

    angleRad = radians(angle)
    return array([[1,0,0],
                     [0,cos(angleRad),-sin(angleRad)],
                     [0,sin(angleRad),cos(angleRad)]])
def Ry(angle):

    angleRad = radians(angle)
    return array([[cos(angleRad),0,sin(angleRad)],
                     [0,1,0],
                     [-sin(angleRad),0,cos(angleRad)]])
def Rz(angle):
    angleRad = radians(angle)
    return array([[cos(angleRad),-sin(angleRad),0],
                     [sin(angleRad),cos(angleRad),0],
                     [0,0,1]])
def R_roll(angle):
    angleRad = radians(angle)
    return array([[1,                0,                0],
                     [0, cos(angleRad), sin(angleRad)],
                     [0,-sin(angleRad), cos(angleRad)]])
def R_pitch(angle):
    angleRad = radians(angle)
    return array([[cos(angleRad), 0, -1*sin(angleRad)],
                     [0,                1, 0],
                     [sin(angleRad), 0, cos(angleRad)]])
def R_yaw(angle):
    angleRad = radians(angle)
    return array([[cos(angleRad),    sin(angleRad), 0],
                     [-1*sin(angleRad), cos(angleRad), 0],
                     [0,                   0,                1]])

def DCM(roll,pitch,yaw):
    return matmul(R_yaw(yaw),matmul(R_pitch(pitch),R_roll(roll)))

def ENUtoECEF(Lat,Long):
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
    thetaRad = radians(theta)
    phiRad = radians(phi)

    R = array([
        [sin(thetaRad)*cos(phiRad), cos(thetaRad)*cos(phiRad), -sin(phiRad)],
        [sin(thetaRad)*sin(phiRad), cos(thetaRad)*sin(phiRad),  cos(phiRad)],
        [               cos(thetaRad),                sin(thetaRad),               0]
    ])
    return R

def Rotation3D(yaw, pitch, roll):

    yawR = radians(yaw)
    pitchR = radians(pitch)
    rollR = radians(roll)
    return array([[cos(yawR)*cos(pitchR), cos(yawR)*sin(pitchR)*sin(rollR) - sin(yawR)*cos(rollR), cos(yawR)*sin(pitchR)*cos(rollR) + sin(yawR)*sin(rollR) ], [sin(yawR)*cos(pitchR), sin(yawR)*sin(pitchR)*sin(rollR) + cos(yawR)*cos(rollR), sin(yawR)*sin(pitchR)*cos(rollR) - cos(yawR)*sin(rollR)], [-1*sin(pitchR), cos(pitchR)*sin(rollR), cos(pitchR)*cos(rollR)]])

def RotationAboutAxes(theta, axX,axY,axZ):

    thetaR = radians(theta)
    return array([
    [cos(thetaR) + (axX*axX)*(1 - cos(thetaR)),    axX*axY*(1-cos(thetaR)) - axZ*sin(thetaR), axX*axZ*(1-cos(thetaR)) + axY*sin(thetaR)],
    [axY*axX*(1- cos(thetaR)) + axZ*sin(thetaR), cos(thetaR) + axY*axY*(1- cos(thetaR)),    axY*axZ*(1- cos(thetaR)) - axX*sin(thetaR)],
    [axZ*axX*(1- cos(thetaR)) - axY*sin(thetaR), axZ*axY*(1- cos(thetaR))+ axX*sin(thetaR), cos(thetaR)+axZ*axZ*(1- cos(thetaR))]
        ])

def GreatCircleDistance(lat1,lat2,long1,long2):

    return 2*Re*arcsin(sqrt( sin(radians( (lat2-lat1)/2  ))**2 + cos(radians(lat1))*cos(radians(lat2))*sin(radians( (long2-long1)/2  ))**2  ))