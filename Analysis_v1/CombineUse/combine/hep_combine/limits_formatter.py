import json
import argparse

## Command Line Options
parser = argparse.ArgumentParser(description='Run Card Settings')
parser.add_argument('-i', '--input', help='Input from CombineHarvester.', type=str,
                    default="../limits.json")

args = parser.parse_args()
json_file = args.input

with open(json_file, "r") as read_file:
	data = json.load(read_file)

LU_list = [float(LU) for LU in data]
LU_list.sort()

output_file = "limits_unp_info.txt"
with open(output_file, "w") as write_file:
	write_file.write("# x, y, -2, +2, -1, +1 \n")
	for lu in LU_list:
		string = "{0} {1} {2} {3} {4} {5} \n".format(int(lu), data[str(lu)]["exp0"], data[str(lu)]["exp-2"], data[str(lu)]["exp+2"], data[str(lu)]["exp-1"], data[str(lu)]["exp+1"])
		write_file.write(string)
		print string
