



def apl_rainbow_black0_cmap(**kwargs):

    showColorbar = kwargs.get('showColorbar',False)

    red = [0, 0, 1, 2, 3, 5, 6, 6, 7, 8, 9, 10, 12, 12, 14, 14, 15, 16, 16, 16, 16, 17, 17, 18, 18, 18, 18, 18, 18, 18,
           18, 17,
           16, 16, 16, 15, 14, 13, 12, 11, 10, 9, 9, 8, 7, 7, 6, 5, 4, 3, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 4, 4, 5, 6, 7, 8, 10, 11, 12, 12, 14, 14, 15, 17, 20, 24, 26, 29, 31,
           33, 36,
           40, 45, 46, 50, 54, 58, 60, 63, 68, 73, 79, 86, 91, 94, 101, 109, 117, 124, 128, 132, 136, 140, 144, 151,
           154, 158,
           162, 166, 171, 173, 176, 179, 183, 186, 189, 191, 193, 195, 197, 199, 202, 206, 210, 212, 214, 216, 218, 219,
           220, 220,
           222, 222, 223, 225, 226, 227, 228, 228, 229, 230, 231, 232, 233, 234, 234, 235, 236, 236, 237, 238, 239, 241,
           242, 243,
           243, 244, 245, 245, 247, 247, 248, 248, 248, 248, 249, 249, 249, 250, 250, 250, 250, 249, 249, 249, 249, 249,
           249, 249,
           248, 248, 248, 247, 247, 246, 245, 245, 244, 243, 243, 242, 241, 241, 240, 239, 238, 237, 237, 236, 235, 234,
           233, 233,
           232, 231, 230, 229, 228, 227, 225, 224, 223, 222, 220, 218, 217, 216, 215, 214, 214, 213, 211, 211, 211, 210,
           209, 208,
           207, 206, 205, 204, 204, 202, 200]
    green = [0, 0, 0, 2, 3, 4, 5, 6, 7, 8, 8, 9, 11, 11, 12, 14, 16, 17, 19, 21, 23, 25, 27, 28, 29, 33, 36, 39, 41, 43,
             46, 48, 50,
             53, 56, 59, 61, 65, 70, 72, 75, 78, 82, 87, 91, 94, 97, 100, 104, 108, 111, 114, 116, 119, 121, 124, 126,
             129, 131,
             133, 134, 137, 140, 142, 144, 147, 149, 150, 152, 155, 157, 158, 160, 162, 163, 164, 165, 167, 168, 170,
             171, 172, 173,
             175, 176, 178, 179, 180, 182, 184, 186, 187, 189, 190, 192, 193, 195, 198, 200, 201, 202, 203, 204, 206,
             208, 208, 209,
             210, 212, 213, 215, 216, 217, 218, 220, 222, 224, 226, 227, 228, 230, 231, 232, 234, 236, 238, 239, 239,
             240, 241, 241,
             242, 242, 242, 242, 242, 242, 241, 241, 239, 238, 237, 236, 234, 233, 232, 230, 229, 227, 225, 223, 221,
             221, 219, 216,
             213, 209, 206, 203, 200, 196, 191, 187, 185, 183, 180, 179, 176, 174, 170, 168, 165, 161, 157, 154, 153,
             152, 150, 148,
             147, 144, 143, 142, 140, 138, 136, 133, 131, 129, 126, 124, 122, 120, 118, 116, 115, 113, 110, 109, 108,
             106, 102, 98,
             96, 94, 90, 87, 86, 83, 81, 79, 77, 75, 74, 73, 71, 69, 67, 66, 64, 63, 61, 60, 58, 56, 53, 54, 62, 65, 69,
             74, 78, 81,
             86, 86, 91, 97, 98, 95, 94, 90, 90, 85, 85, 85, 81, 80, 77, 75, 73, 70, 67, 60, 62, 70, 70]
    blue = [100, 106, 111, 117, 122, 128, 138, 149, 154, 160, 165, 171, 176, 176, 181, 187, 192, 198, 203, 208, 212,
            217, 221, 226,
            231, 235, 240, 244, 249, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
            254, 252, 249,
            246, 244, 241, 238, 235, 232, 230, 227, 224, 221, 219, 217, 216, 213, 211, 208, 205, 202, 200, 197, 194,
            191, 188, 186,
            183, 180, 177, 175, 172, 169, 166, 164, 161, 158, 155, 153, 150, 147, 144, 141, 139, 136, 133, 130, 128,
            125, 122, 119,
            117, 114, 111, 108, 106, 103, 100, 97, 94, 94, 92, 89, 86, 84, 81, 78, 75, 73, 70, 67, 64, 62, 59, 56, 53,
            50, 48, 45,
            42, 39, 37, 34, 31, 28, 26, 23, 20, 17, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 9, 14, 17, 21, 26, 29, 33, 37, 41, 45, 49, 53, 57, 62, 65, 69, 74,
            78, 81,
            86, 86, 91, 97, 102, 105, 109, 114, 117, 121, 126, 126, 131, 136, 140, 143, 147, 152, 155, 159, 164, 167,
            171]

    cbarColors = [[red[i], green[i], blue[i]] for i in range(len(red))]
    def rgb2hex(r,g,b):
        return "#{:02x}{:02x}{:02x}".format(r,g,b)

    # --- create the colorbar ---
    import matplotlib
    cbarColorHex = [rgb2hex(*val) for val in cbarColors]
    cm = matplotlib.colors.ListedColormap(cbarColorHex, name='apl_rainbow_black0')

    if showColorbar:
        import numpy as np
        import matplotlib.pyplot as plt

        x,y,c = zip(*np.random.rand(30,3)*4-2)
        plt.scatter(x,y,c=c, cmap=cm)
        plt.colorbar()
        plt.show()

    return cm
