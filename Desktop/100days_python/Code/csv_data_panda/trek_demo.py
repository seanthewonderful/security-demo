import pandas


ent_list = []
with open("enterprise.txt", 'r') as ent:
    for lines in ent:
        line = lines.rstrip().split(',')
        name, rank, role, species = line
        ent_dict = {
            "name": name,
            "rank": rank,
            "role": role,
            "species": species
        }
        ent_list.append(ent_dict)
        

def find_trekkie(name):
    for each in ent_list:
        if each["name"] == name:
            print(f"""
                  Name: {each['name']}
                  Rank: {each['rank']}
                  Role: {each['role']}
                  Species: {each['species']}
                  """)
        

find_trekkie("Worf")