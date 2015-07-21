import ROOT
from EcalTiming.EcalTiming.txt2tree import txt2tree


def getCalibFromTree(tree):
	calibMap = dict()
	for event in tree:
		calibMap[event.rawid] = event.time
	return calibMap

def getCalib():
	input = "/afs/cern.ch/user/p/phansen/public/ecal-timing/dump_EcalTimeCalibConstants_v07_offline__since_00204623_till_4294967295.dat"

	calibMap = dict()
	with open(input,'r') as f:
		for line in f:
			line = line.split()
			time = float(line[3])
			rawid = int(line[5])
			calibMap[rawid] = time

	return calibMap

if __name__ == "__main__":
	print "hi"
	calib = getCalib();
	print len(calib)

