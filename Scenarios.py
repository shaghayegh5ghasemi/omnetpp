from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt

def Received_Packets_Ratio(totalReceivedPackets, sentPackets):
    temp = 0
    for i in range(len(sentPackets)):
        temp += sentPackets[i]
    if temp == 0:
        return None
    return totalReceivedPackets[0]/temp

def Energy_Consumption(totalReceivedPackets, totalEnergyConsumed):
    temp = 0
    for i in range(len(totalEnergyConsumed)):
        temp += totalEnergyConsumed[i]
    if totalReceivedPackets[0] != 0:
        return temp/totalReceivedPackets[0]
    return None


def get_lines_with(input_str, substr):
    lines = []
    for line in input_str.strip().split('\n'):
        if substr in line:
            lines.append(line)
    return lines

def sca_line(fname, substr):
    f_contents = open(fname, 'r').read()
    return get_lines_with(f_contents, substr)

#we need special parameters for each node, GW and server to calculate  Received_Packets_Ratio and Energy_Consumption
def get_parameters(path, substr):
    temp_substr = sca_line(path, substr)
    parameter = []
    for i in range(len(temp_substr)):
        temp = temp_substr[i].split(" ")
        parameter.append(float(temp[-1]))
    return parameter

def plot(ts, sp, en):
    xaxis = [15, 30]
    ratio = [Received_Packets_Ratio(ts[0], sp[0]), Received_Packets_Ratio(ts[1], sp[1])]
    energy = [Energy_Consumption(ts[0], en[0]), Energy_Consumption(ts[1], en[1])]
    print("Received Packets Ratio:")
    print(ratio)
    print("Energy Consumption:")
    print(energy)
    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()
    offset = 30
    new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    par2.axis["right"] = new_fixed_axis(loc="right", axes=par2, offset=(offset, 0))

    par2.axis["right"].toggle(all=True)
    host.set_xlim(15, 30)
    if ratio[0] != None:
        host.set_ylim(ratio[1] - 0.5, ratio[0] + 0.5)
    else:
        host.set_ylim(0, 2)
    if energy[0] != None:
        par2.set_ylim(energy[0] - 0.5, energy[1] + 0.5)
    else:
        par2.set_ylim(0, 2)

    host.set_xlabel("Number Of Nodes")
    host.set_ylabel("Received Packets Ratio")
    par2.set_ylabel("Energy Consumption")

    if ratio != None:
        p1, = host.plot(xaxis, ratio, label="Received Packets Ratio", linewidth=5)
    if energy != None:
        p2, = par2.plot(xaxis, energy, label="Energy Consumption", linewidth=5)



    host.legend()

    host.axis["left"].label.set_color(p1.get_color())
    par2.axis["right"].label.set_color(p2.get_color())

    plt.draw()
    plt.show()


node_15 = "Scenario-15.sca"
node_30 = "Scenario-16.sca"

sendPackets = []
totalEnergyConsumed = []
totalReceivedPackets = []

sendPackets.append(get_parameters(node_15, "sentPackets"))
sendPackets.append(get_parameters(node_30, "sentPackets"))

totalEnergyConsumed.append(get_parameters(node_15, "totalEnergyConsumed"))
totalEnergyConsumed.append(get_parameters(node_30, "totalEnergyConsumed"))

totalReceivedPackets.append(get_parameters(node_15, "totalReceivedPackets"))
totalReceivedPackets.append(get_parameters(node_30, "totalReceivedPackets"))

print("sendPackets for 15 nodes: ")
print(sendPackets[0])
print("sendPackets for 30 nodes: ")
print(sendPackets[1])

print("totalEnergyConsumed for 15 nodes: ")
print(totalEnergyConsumed[0])
print("totalEnergyConsumed for 30 nodes: ")
print(totalEnergyConsumed[1])

print("totalReceivedPackets for 15 nodes: ")
print(totalReceivedPackets[0])
print("totalReceivedPackets for 30 nodes: ")
print(totalReceivedPackets[1])

plot(totalReceivedPackets, sendPackets, totalEnergyConsumed)






