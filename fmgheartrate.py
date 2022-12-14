import matplotlib.pyplot as plt

def main():
    # read file
    file = open("miguel_hr.txt")
    lines = file.readlines()
    file.close()

    hr = [None] * 324 
    counter = 0
    # look for patterns
    for line in lines:

        line = line.strip()
        if line.find("BPM:")!=-1:
            
            # print(line.find(":"))

            if line.find(".") == 7:
                hr[counter] = int(line[5:7])
                # print(line[5:7])
            elif line.find(".") == 8:
                hr[counter] = int(line[5:8])
                # print(line[5:8])

            print(hr[counter])
            if (hr[counter] - hr[counter - 1]) >= 25:
                hr[counter] = hr[counter - 1]

            counter = counter + 1
    
    # print(hr)
    xaxis = list(range(1,325))
    # print(xaxis)
    plt.plot(list(range(1,325)),hr)
    plt.xlabel('Sample')
    plt.ylabel('Heart Rate (Beats per Minute)')
    plt.title('Heart Rate vs. Sample')
    plt.show()

    # plt.plot([1,2,3,4], [4,3,2,5])
    # plt.show()
    
main()