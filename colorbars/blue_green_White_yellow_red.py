

def blue_green_white_yellow_red_cmap(**kwargs):

    showColorbar = kwargs.get('showColorbar',False)

    index= [  0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49 , 50 , 51 , 52 , 53 , 54 , 55 , 56 , 57 , 58 , 59 , 60 , 61 , 62 , 63 , 64 , 65 , 66 , 67 , 68 , 69 , 70 , 71 , 72 , 73 , 74 , 75 , 76 , 77 , 78 , 79 , 80 , 81 , 82 , 83 , 84 , 85 , 86 , 87 , 88 , 89 , 90 , 91 , 92 , 93 , 94 , 95 , 96 , 97 , 98 , 99 , 100 , 101 , 102 , 103 , 104 , 105 , 106 , 107 , 108 , 109 , 110 , 111 , 112 , 113 , 114 , 115 , 116 , 117 , 118 , 119 , 120 , 121 , 122 , 123 , 124 , 125 , 126 , 127 , 128 , 129 , 130 , 131 , 132 , 133 , 134 , 135 , 136 , 137 , 138 , 139 , 140 , 141 , 142 , 143 , 144 , 145 , 146 , 147 , 148 , 149 , 150 , 151 , 152 , 153 , 154 , 155 , 156 , 157 , 158 , 159 , 160 , 161 , 162 , 163 , 164 , 165 , 166 , 167 , 168 , 169 , 170 , 171 , 172 , 173 , 174 , 175 , 176 , 177 , 178 , 179 , 180 , 181 , 182 , 183 , 184 , 185 , 186 , 187 , 188 , 189 , 190 , 191 , 192 , 193 , 194 , 195 , 196 , 197 , 198 , 199 , 200 , 201 , 202 , 203 , 204 , 205 , 206 , 207 , 208 , 209 , 210 , 211 , 212 , 213 , 214 , 215 , 216 , 217 , 218 , 219 , 220 , 221 , 222 , 223 , 224 , 225 , 226 , 227 , 228 , 229 , 230 , 231 , 232 , 233 , 234 , 235 , 236 , 237 , 238 , 239 , 240 , 241 , 242 , 243 , 244 , 245 , 246 , 247 , 248 , 249 , 250 , 251 , 252 , 253 , 254 , 255  ]
    red= [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 6 , 17 , 28 , 39 , 50 , 61 , 72 , 83 , 94 , 105 , 117 , 126 , 136 , 146 , 156 , 166 , 171 , 178 , 185 , 192 , 198 , 204 , 209 , 215 , 221 , 227 , 232 , 238 , 244 , 249 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 254 , 253 , 252 , 251 , 250 , 249 , 247 , 244 , 241 , 239 , 237 , 234 , 229 , 224 , 220 , 215 , 211 , 207 , 202 , 198 , 193 , 189 , 184 , 180 , 176 , 171 , 167 , 162 , 158 , 154 , 149 , 145 , 140 , 136 , 132 , 127  ]
    green= [  0 , 2 , 4 , 6 , 8 , 10 , 12 , 13 , 15 , 17 , 19 , 22 , 25 , 28 , 32 , 35 , 39 , 42 , 48 , 53 , 57 , 62 , 67 , 73 , 78 , 82 , 86 , 90 , 94 , 99 , 103 , 107 , 110 , 113 , 116 , 119 , 122 , 125 , 128 , 131 , 133 , 136 , 139 , 142 , 145 , 148 , 151 , 153 , 156 , 159 , 162 , 164 , 165 , 166 , 168 , 169 , 170 , 171 , 173 , 174 , 175 , 176 , 178 , 179 , 180 , 181 , 183 , 184 , 185 , 186 , 187 , 189 , 190 , 191 , 192 , 194 , 195 , 196 , 197 , 199 , 200 , 201 , 202 , 204 , 205 , 206 , 207 , 209 , 210 , 211 , 212 , 213 , 215 , 216 , 217 , 218 , 220 , 221 , 222 , 223 , 225 , 226 , 227 , 228 , 230 , 231 , 232 , 233 , 234 , 236 , 237 , 238 , 239 , 241 , 242 , 243 , 244 , 246 , 247 , 248 , 249 , 251 , 252 , 253 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 253 , 250 , 248 , 246 , 243 , 241 , 238 , 236 , 234 , 231 , 229 , 227 , 224 , 222 , 220 , 217 , 215 , 213 , 210 , 208 , 205 , 203 , 201 , 198 , 196 , 194 , 191 , 189 , 187 , 184 , 182 , 179 , 177 , 175 , 172 , 170 , 168 , 165 , 163 , 161 , 158 , 156 , 153 , 151 , 149 , 146 , 144 , 142 , 139 , 137 , 135 , 132 , 130 , 128 , 125 , 123 , 120 , 118 , 116 , 113 , 111 , 109 , 106 , 104 , 102 , 99 , 97 , 94 , 92 , 90 , 87 , 85 , 83 , 80 , 78 , 76 , 73 , 71 , 68 , 66 , 64 , 61 , 59 , 57 , 54 , 52 , 50 , 47 , 45 , 43 , 40 , 38 , 35 , 33 , 31 , 28 , 26 , 24 , 21 , 19 , 17 , 14 , 12 , 9 , 7 , 5 , 2 , 0  ]
    blue= [  124 , 130 , 137 , 143 , 149 , 155 , 162 , 168 , 174 , 181 , 187 , 193 , 197 , 202 , 206 , 211 , 215 , 220 , 224 , 227 , 231 , 234 , 237 , 241 , 243 , 245 , 248 , 250 , 252 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 255 , 254 , 252 , 251 , 249 , 247 , 245 , 244 , 242 , 240 , 238 , 237 , 235 , 233 , 232 , 230 , 228 , 226 , 225 , 223 , 221 , 220 , 218 , 216 , 214 , 213 , 211 , 209 , 207 , 206 , 204 , 202 , 201 , 199 , 197 , 195 , 194 , 192 , 190 , 188 , 187 , 185 , 183 , 183 , 182 , 182 , 182 , 181 , 181 , 181 , 181 , 180 , 180 , 179 , 180 , 181 , 182 , 182 , 183 , 183 , 185 , 187 , 189 , 190 , 193 , 196 , 199 , 203 , 206 , 210 , 213 , 216 , 220 , 223 , 227 , 230 , 235 , 240 , 245 , 249 , 255 , 255 , 246 , 238 , 230 , 222 , 214 , 206 , 198 , 191 , 183 , 175 , 167 , 159 , 151 , 143 , 135 , 127 , 119 , 111 , 103 , 95 , 87 , 79 , 71 , 64 , 56 , 48 , 40 , 32 , 24 , 16 , 8 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0  ]

    cbarColors = [[red[i], green[i], blue[i]] for i in range(len(index))]
    def rgb2hex(r,g,b):
        return "#{:02x}{:02x}{:02x}".format(r,g,b)

    # --- create the colorbar ---
    import matplotlib
    cbarColorHex = [rgb2hex(*val) for val in cbarColors]
    cm = matplotlib.colors.ListedColormap(cbarColorHex, name='blue_green_white_yellow_red')

    if showColorbar:
        import numpy as np
        import matplotlib.pyplot as plt

        x,y,c = zip(*np.random.rand(30,3)*4-2)
        plt.scatter(x,y,c=c, cmap=cm)
        plt.colorbar()
        plt.show()

    return cm