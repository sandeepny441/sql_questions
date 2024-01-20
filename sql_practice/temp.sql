import json
from collections import defaultdict
import pandas as pd

# Set the number of top items to display
k = 3
file_name = 'score_recs.data'

def read_json(file_name):
    """
    Reads a JSON file and returns a dictionary with scores as keys and lists of IDs as values.
    """
    result = defaultdict(list)
    with open(file_name, encoding='utf-8') as fp:
        for line in fp:
            if line and line.strip():
                score = line[:line.find(":")].strip()
                score = int(score)
                
                obj = line[line.find(":") + 1:]
                try:
                    obj = json.loads(obj)
                    result[score].append(obj['id'])
                except Exception:
                    result[score] = None
    return result

def generate_output(result):
    """
    Generates a JSON output from the result dictionary containing the top k scores and corresponding IDs.
    """
    result = dict(result)
    df = pd.DataFrame(sorted(result.items(), key=lambda x: x[0], reverse=True)[:k],
                      columns=['Score', 'Id'])
    
    if df['Id'].isnull().sum() > 0 or df['Score'].isnull().sum() > 0:
        raise Exception("Invalid JSON format. No JSON object could be decoded. THIS IS NOT JSON.")
    else:
        output = [{"Score": row[0], "Id": row[1][-1]} for row in df.values]
        output_json = json.dumps(output)
        return output_json

# Process the input file and generate output
try:
    json_obj = read_json(file_name)
    output_json = generate_output(json_obj)
    print(output_json)
except Exception as e:
    print(f"An error occurred: {e}")


