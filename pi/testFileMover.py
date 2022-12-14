import os

# otuputFile = "output/bpm_data"

def save():
    num = len(os.listdir("output/"))
    otuputFile = "output/bpm_data" + "_" + str(num) + ".txt"
    print(otuputFile)
    os.system("mv output/bpm_data.txt " + otuputFile)
    

    pass

save()