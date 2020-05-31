from fderiv import fderiv as fd
import numpy as np


def main():
    x = np.arange(0, 1, 0.1)
    N = len(x)
    y = np.sin(x)
    yp, ypp = fd.fd5pt(x, y)
    ytrue = np.cos(x)
    print("Result", yp, "\n yp diff = ", yp - ytrue, "\n diff=", y - ypp)


if __name__ == "__main__":
    main()
