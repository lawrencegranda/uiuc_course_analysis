import numpy
import requests, json
import os


def get_data():
    with open(os.path.join('./data', 'class_hierarchy.json')) as f:
        req_data = json.load(f)["vertices"]
    # url = requests.get("https://waf.cs.illinois.edu/discovery/class_hierarchy_at_illinois/static/res/class_hierarchy.json")
    # req_data = json.loads(url.text)["vertices"]
    
    requirements = dict()
    for r in req_data:
        r["Id"] = r["Id"].strip().upper()
        requirements[r["Id"]] = dict()
        requirements[r["Id"]]["description"] = r["Description"]
        if len(r["Prerequisites"]) == 0:
            r["Prerequisites"] = ["None"]
        requirements[r["Id"]]["prerequisites"] = r["Prerequisites"]
    
    
    
    # url = requests.get("https://waf.cs.illinois.edu/discovery/every_gen_ed_at_uiuc_by_gpa/data/all_gened.json")
    # gen_ed_data = json.loads(url.text)
    
    with open(os.path.join('./data', 'all_gened.json')) as f:
        gen_ed_data = json.load(f)
    
    gen_eds = dict()
    
    for g in gen_ed_data:
        g["name"] = g["name"].strip().upper()
        gen_eds[g["name"]] = g["GenedRequirement"]
    
    
    
    # url = requests.get("https://waf.cs.illinois.edu/discovery/grade_disparity_between_sections_at_uiuc/data/out_full.json")
    # grade_data = json.loads(url.text)
    
    with open(os.path.join('./data', 'grade_per_section.json')) as f:
        grade_data = json.load(f)
        
    courses = dict()
    
    for d in grade_data:
        d['course'] = d["course"].strip().upper()
        d["title"] = d["instructors"][0]["Course Title"]
        d["size"] = d["instructors"][0]["countGPA"]
        d["avg_grade"] = round(d["instructors"][0]["avgGPA"]*10 + 53)
        d["percent_a"] = round(d["instructors"][0]["gpaDist"][0]*100/d["size"])
        
        top_ins = d["instructors"][0]["instructor"]
        
        instructors = dict()
        for a in d["instructors"]:
            instructors[a["instructor"]] = a
            
            a["percent_a"] = round(a["gpaDist"][0]*100/a["countGPA"])
            a["avg_grade"] = round(a["avgGPA"]*10 + 55)

            if(a["percent_a"] > instructors[top_ins]["percent_a"]):
                top_ins = a["instructor"]

        d["instructors"] = instructors
        d["top_instructor"] = top_ins
        d["top_percent_a"] = d["instructors"][top_ins]["percent_a"]
        d["description"] = "" if d["course"] not in requirements.keys() else requirements[d["course"]]['description']
        d["prerequisites"] = ["None found"] if d["course"] not in requirements.keys() else requirements[d["course"]]['prerequisites']
        d["general_education"] = ["None found"] if d["course"] not in gen_eds.keys() else gen_eds[d["course"]]
        
        courses[d["course"]] = dict()
        
        for k in ["course", "title", "description", "prerequisites", "general_education", "avg_grade", "percent_a", "size", "top_percent_a", "top_instructor", "instructors"]:
            courses[d["course"]][k] = d[k]
    
    
    
    

    
    return courses




if __name__ == "__main__":
    json.dump(get_data(), open("courses.json", "w"), indent=3)
