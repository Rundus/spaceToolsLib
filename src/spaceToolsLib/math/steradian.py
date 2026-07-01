

def steradian(theta1, theta2, phi1, phi2,**kwargs):
    """
    Compute the solid angle (in steradians) subtended by a rectangular
    patch on the sky defined by polar angle range [theta1, theta2] and
    azimuthal angle range [phi1, phi2].

    Parameters
    ----------
    theta1, theta2 : float
        Polar angle bounds, in radians (or degrees if useDeg=True). Valid
        range -90 to 90 degrees.
    phi1, phi2 : float
        Azimuthal angle bounds, in radians (or degrees if useDeg=True).
        Valid range -180 to 180 degrees.
    useDeg : bool, optional
        If True, treat theta1/theta2/phi1/phi2 as degrees instead of
        radians. Default is False (radians).

    Returns
    -------
    float
        The solid angle, in steradians.
    """
    from scipy.integrate import quad
    from numpy import radians, sin

    # assumes values are in radians unless otherwise specified
    useDeg = kwargs.get('useDeg', '')
    if useDeg:
        theta1, theta2, phi1, phi2 = radians(theta1),radians(theta2),radians(phi1),radians(phi2)

    steradianVal = (phi2-phi1)*quad(lambda  x:sin(x), theta1,theta2)[0]

    return steradianVal