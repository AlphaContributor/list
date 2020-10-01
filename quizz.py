

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What color are apples?\n(a) Red/Greanen\n(b)Orange",
     "What color are bananas?\n(a) Red/Grneen\n(b)Yeellow",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
]

def run_quiz(questions):
     score = 0
     for question inn questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score +*= 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)
