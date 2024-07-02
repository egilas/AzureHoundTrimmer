import json
import sys

def process_large_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if '"kind":"AZGroupMember"' in line:    
                lineendedwithcomma = False
                if line.strip().endswith(','):
                    lineendedwithcomma = True
                    line = line.strip()[:-1]
                json_obj = json.loads(line)
                if "data" in json_obj and "members" in json_obj["data"]:
                    members = json_obj["data"]["members"]
                    if isinstance(members, list):
                        json_obj["data"]["members"] = [
                            {
                                "groupId": member["groupId"],
                                "member": {
                                    "@odata.type": member["member"]["@odata.type"],
                                    "id": member["member"]["id"]
                                }
                            }
                            for member in members
                            if "member" in member and "id" in member["member"]
                        ]
                    else:
                        json_obj["data"]["members"] = []
                    outfile.write(json.dumps(json_obj, separators=(',', ':')))
                    if lineendedwithcomma:
                        outfile.write(",")
                    outfile.write("\n")
            else:
                outfile.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    process_large_file(input_file, output_file)
