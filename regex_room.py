# multiple choice regex, show user regex pattern and give them a choice between A,B,C on what it will match
# change via github

def regex_room():
    questions = get_questions()

    for question in questions:
        print(f"Which piece of text does this pattern match in Regex? {question["pattern"]}")
        for options in question["options"].items():
            for op, option in options:
                print
        answer = input("Well? ")
        if answer == question["answer"]:
            print("CORRECT")
        else:
            print("WRONG!")






def get_questions():
    questions = [
        {
            "pattern": "^k.{5}t",
            "answer": "a",
            "options": {
                "a": "kubernetes",
                "b": "kubectl",
                "c": "kubelet" #answer
            }
            

        },
        {
            "pattern": "(.{3})( )([a-z]{3})",
            "answer": "b",
            "options": {
                "a": "git addg",
                "b": "git commit",
                "c": "git push"
                }

        }
    ]
    
    return questions 

