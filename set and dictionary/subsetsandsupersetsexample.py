required_skills = ['python','github','linux']

candidates ={
    'anna' : {'java','linux','conduct','github','python','fullstack',},
    'bob' :{'github','linux','html','python','github',},
    'carol' : {'linux','javascript','pascal','c++','github',},
    'jennet' : {'pasacal','java','c++',},
    'ekani' : {'html','css','github','python',},
}

interviews = set()  #creating an empty set

for candidate,skills in candidates.items():
    if skills.issuperset(required_skills):
        interviews.add(candidate)

print(interviews)
