import math
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt

#Calculate time on air (ms)
def ToA(bw, sf, pl, cr):
    #The use of explicit header is considered disabled
    IH = 0
    #The Low Data Rate Optimization is considered enabled
    DE = 1
    temp = (math.ceil((8*pl - 4*sf + 28 + 16 - 20*IH)/(4*(sf - 2*DE))))*(cr + 4)
    n_payload = 8 + max(temp, 0)
    t_preamble = (4.25 + 8)*(2**sf/bw)
    t_payload = n_payload*(2**sf/bw)
    t_on_the_air = t_preamble + t_payload
    return float(format(t_on_the_air, '.2f'))

def plot():
    yaxis = []
    for i in range(7, 13):
        t = []
        t.append(ToA(125, i, 0, 1))
        t.append(ToA(125, i, 16, 1))
        t.append(ToA(125, i, 32, 1))
        t.append(ToA(125, i, 51, 1))
        yaxis.append(t)

    xaxis = [0, 16, 32, 51]

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    host.set_xlim(0, 60)
    host.set_ylim(0, 1650)

    host.set_xlabel("Payload [bytes]")
    host.set_ylabel("ToA [ms]")

    for i in range(len(yaxis)):
        host.plot(xaxis, yaxis[i], label="SF = " + str(i+7))
        plt.scatter(xaxis, yaxis[i], color="gray", s=20, marker="x")

    host.legend()
    plt.draw()
    plt.show()

print("Bandwidth = 125 KHz       code rate = 1 kb/sec")
plot()