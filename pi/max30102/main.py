from heartrate_monitor import HeartRateMonitor
import time
import argparse
import os


otuputPath = "/home/pi/CE4201-IoT-FMG/pi/output/"
# def save():
#     num = len(os.listdir(otuputPath))
#     otuputFile = otuputPath+"bpm_data" + "_" + str(num) + ".txt"
#     print(otuputFile)
#     os.system("mv " + otuputFile + " " + otuputFile)
    

#     pass

# save()
parser = argparse.ArgumentParser(description="Read and print data from MAX30102")
parser.add_argument("-r", "--raw", action="store_true",
                    help="print raw data instead of calculation result")
parser.add_argument("-t", "--time", type=int, default=30,
                    help="duration in seconds to read from sensor, default 30")
args = parser.parse_args()

print('sensor starting...')
hrm = HeartRateMonitor(print_raw=args.raw, print_result=(not args.raw))
hrm.start_sensor()
try:
    time.sleep(args.time)
except KeyboardInterrupt:
    print('keyboard interrupt detected, exiting...')

hrm.stop_sensor()
print('sensor stoped!')