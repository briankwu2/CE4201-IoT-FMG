import statistics

inputFileName = "bpm_data.txt"


def main():
    # read file
    file = open(inputFileName)
    lines = file.readlines()
    file.close()

    # hr = [None] * 324 
    hr = []

    # look for patterns
    for line in lines:

        line = line.strip()
        if line.find("BPM:")!=-1:

            if line.find(".") == 7:
                hr.append(int(line[5:7]))

            elif line.find(".") == 8:
                hr.append(int(line[5:8]))

    # print(hr)
    # print(hr[1])
    oneHR = statistics.median_low(hr)
    # if oneHR >= 100:
    #     oneHR = 72
    print(oneHR)

    # counter = 0
    # if hr[counter+1] - hr[counter] > 25:


    # # print(hr)
    # xaxis = list(range(1,325))
    # # print(xaxis)
    # plt.plot(list(range(1,325)),hr)
    # plt.xlabel('Sample')
    # plt.ylabel('Heart Rate (Beats per Minute)')
    # plt.title('Heart Rate vs. Sample')
    # plt.show()

    # plt.plot([1,2,3,4], [4,3,2,5])
    # plt.show()
    
main()
