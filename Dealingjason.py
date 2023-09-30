import json


def read_data(filename):

    try:
        filobject = open(filename, 'r')
    except Exception as e:
        print(e)
        return False

    else:
        data = filobject.read()
        # print(data)
        data = json.loads(data)
        filobject.close()
        return data  # dict


def save_data_to_json(filename, data_to_save):
    # 1- read file content
    old_data= read_data(filename)  # dict
    """
        {
            "data": [
            
                {}, {}
            ]
        }
    
    """
    old_data["data"].append(data_to_save)

    # old data now contains ---> all the old and the new data
    try:
        filobject = open(filename, 'w')
    except Exception as e:
        print(e)
        return False

    else:
        data = json.dumps(old_data, indent=2)
        filobject.write(data)
        filobject.close()
        return True  # dict

def json_to_save(filename,jsonobj):
    try:
        filobject = open(filename, 'w')
    except Exception as e:
        print(e)
        return False
    else:
        data = json.dumps(jsonobj, indent=2)
        filobject.write(data)
        filobject.close()
        return True  # dict

if __name__=='__main__':
    # data=read_data('users.json')
    # print(type(data))
    save_data_to_json('users.json', {"name":"Abdulrahman", "track":"python"})
