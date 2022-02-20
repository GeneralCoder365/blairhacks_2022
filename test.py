import json

tags = '{"skills": ["computer science", "cs", "math"], "interests": ["machine learning", "probability"], "type_of_opportunity": ["courses"], "in_person_online": "all", "location": "Rockville MD USA"}'



print(dict(json.loads(tags)))