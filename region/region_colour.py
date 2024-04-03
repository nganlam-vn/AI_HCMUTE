from simpleai.search import CspProblem, backtrack
import cv2
import numpy as np

def constraint_func(names, values):
    return values[0] != values[1]

if __name__ == '__main__':
    # Specify the variables
    names = ('Mark', 'Julia', 'Steve', 'Amanda', 'Brian',
             'Joanne', 'Derek', 'Allan', 'Michelle', 'Kelly', 'Chris')

    names_point = [(65, 84), (409, 103), (50, 310), (280, 264), (684, 85), (476, 462),
                   (515, 288), (3, 486), (159, 492), (723, 299), (728, 480)]

    # Define the possible colors
    colors_available = ['red', 'green', 'blue', 'gray']
    colors = dict((name, ['red', 'green', 'blue', 'gray']) for name in names)

    # Define the constraints
    constraints = [
        (('Mark', 'Julia'), constraint_func),
        (('Mark', 'Steve'), constraint_func),
        (('Julia', 'Steve'), constraint_func),
        (('Julia', 'Amanda'), constraint_func),
        (('Julia', 'Derek'), constraint_func),
        (('Julia', 'Brian'), constraint_func),
        (('Steve', 'Amanda'), constraint_func),
        (('Steve', 'Allan'), constraint_func),
        (('Steve', 'Michelle'), constraint_func),
        (('Amanda', 'Michelle'), constraint_func),
        (('Amanda', 'Joanne'), constraint_func),
        (('Amanda', 'Derek'), constraint_func),
        (('Brian', 'Derek'), constraint_func),
        (('Brian', 'Kelly'), constraint_func),
        (('Joanne', 'Michelle'), constraint_func),
        (('Joanne', 'Amanda'), constraint_func),
        (('Joanne', 'Derek'), constraint_func),
        (('Joanne', 'Kelly'), constraint_func),
        (('Joanne', 'Chris'), constraint_func),
        (('Derek', 'Kelly'), constraint_func),
        (('Derek', 'Chris'), constraint_func),
        (('Kelly', 'Chris'), constraint_func),
    ]

    # Solve the problem
    problem = CspProblem(names, colors, constraints)
    # Print the solution
    result = backtrack(problem)

    print('\nColor mapping:\n')
    for k, v in result.items():
        print(k, '==>', v)

    # Load the image
    image = cv2.imread('regions.jpg', cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print("Error: Unable to load the image.")
    else:
        M, N = image.shape

        # Phan nguong mau trang den (0 va 255)
        val, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        image_s = image.copy()

        # Convert to color image
        image_s = cv2.cvtColor(image_s, cv2.COLOR_GRAY2BGR)

        mau_xam = [(10, 10, 10), (50, 50, 50), (100, 100, 100), (150, 150, 150)]
        mau_RGB = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (128, 128, 128)]

        mask = np.zeros((M + 2, N + 2), np.uint8)

        for k, v in result.items():
            vi_tri_point = names.index(k)
            point = names_point[vi_tri_point]
            vi_tri_mau = colors_available.index(v)
            mau = mau_xam[vi_tri_mau]
            cv2.floodFill(image, mask, point, mau)

        for x in range(0, M):
            for y in range(0, N):
                r = image[x, y]
                if r > 0:
                    r = (r, r, r)
                    vi_tri = mau_xam.index(r)
                    mau = mau_RGB[vi_tri]
                    image_s[x, y, :] = mau

        for k, v in result.items():
            vi_tri_point = names.index(k)
            point = names_point[vi_tri_point]
            cv2.putText(image_s, names[vi_tri_point], (point[0], point[1]), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (255, 255, 255), 2)

        cv2.imshow('Image', image_s)
        cv2.waitKey()
