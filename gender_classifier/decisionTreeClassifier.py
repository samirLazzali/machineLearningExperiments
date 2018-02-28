#import 
from sklearn import tree
import csv


#######################################################################
#
#	Get data set (https://osf.io/66fvm/) :
#	https://www.youtube.com/watch?v=T5pRlIbr6gg&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU
#######################################################################

data_set = []
with open('wo_men.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
   	for row in spamreader:
   		data_set.append(row)

#######################################################################
#
#	Clean data set :
#
#######################################################################

#exclude header
header = data_set[0] 
#['time', 'sex', 'height', 'shoe_size']
del data_set[0]

bruit = [] # tore index of 'NA' elements
# divide data_set in data and label
trainning_set = [];label = []

for item in range(len(data_set)):
	for element in range(len(data_set[item])):
		if data_set[item][element] == 'NA':
			#stro index of 'NA'
			bruit.append(item)
	# remove date 
	del data_set[item][0]

	#  smooth data's unity (m to cm)
	if data_set[item][1] != 'NA':
		if float(data_set[item][1]) < 10:
			data_set[item][1] = float(data_set[item][1]) * 100

	#append data to their array
	trainning_set.append([data_set[item][1],data_set[item][2]])
	label.append(data_set[item][0])

# remove NA elements from index
for item_del in bruit:
	del data_set[item_del]
	del trainning_set[item_del]
	del label[item_del]

#######################################################################
#
#	Building tree
#
#######################################################################

#for i in range(len(trainning_set)):
#	print trainning_set[i], ' - ', label[i]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(trainning_set, label)

prediction = clf.predict([['175', '41.0']]) #175 - 41 => man | 175 - 40 => women
#print header
print prediction