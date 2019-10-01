def get_order_diff_quot(xi = [], fi = []):
    f01=(fi[1]-fi[0])/(xi[1]-xi[0])
    f12=(fi[2]-fi[1])/((xi[2]-xi[1]))
    f23=(fi[3]-fi[2])/(xi[3]-xi[2])
    f34=(fi[4]-fi[3])/(xi[4]-xi[3])
    f012=((f12-f01))/(xi[2]-xi[0])
    f123=(f23-f12)/(xi[3]-xi[1])
    f234=(f34-f23)/(xi[4]-xi[2])
    f0123=(f123-f012)/(xi[3]-xi[0])
    f1234=(f234-f123)/(xi[4]-xi[1])
    f01234=(f1234-f0123)/(xi[4]-xi[0])
    L=[fi[0],f01,f012,f0123,f01234]
    return (L)
def get_Newton_interpolation(xi=[],fi=[],x=0):
    l=get_order_diff_quot(xi, fi)
    N = l[0] + l[1] * (x - xi[0]) + l[2] * (x - xi[0]) * (x - xi[1]) + l[3] * (x - xi[0]) * (x - xi[1]) * (x - xi[2]) + l[4] * (x - xi[0]) * (x - xi[1]) * (x - xi[2]) * (x - xi[3])
    print ("{:.4f}".format(N))



XK=[0.40,0.55,0.65,0.80,0.90]
FK=[0.41075,0.57815,0.69675,0.88811,1.02652]
X=float(input())
get_Newton_interpolation(XK,FK,X)

