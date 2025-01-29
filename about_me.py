import json

# Load the JSON file
with open("D:/books/par code/khaled.json", "r") as file:
    cv_data = json.load(file)

def get_info(query):
    query = query.lower()
    
    if "name" in query:
        return cv_data["name"]
    
    elif "profession" in query:
        return cv_data["profession"]
    
    elif "contact" in query:
        return json.dumps(cv_data["contact"], indent=2)
    
    elif "experience" in query:
        return json.dumps(cv_data["experience"], indent=2)
    
    elif "projects" in query:
        return json.dumps(cv_data["projects"], indent=2)
    
    elif "skills" in query:
        return json.dumps(cv_data["skills"], indent=2)
    
    elif "strengths" in query:
        return json.dumps(cv_data["strengths"], indent=2)
    
    elif "certificates" in query:
        return json.dumps(cv_data["certificates"], indent=2)
    
    elif "languages" in query:
        return json.dumps(cv_data["languages"], indent=2)
    
    else:
        return "Sorry, I don't have information on that."

# Example usage
while True:
    question = input("What would you like to know about Khaled? (or type 'exit' to quit): ")
    if question.lower() == "exit":
        break
    answer = get_info(question)
    print(answer)





# https://github.com/balapriyac/data-science-tutorials/