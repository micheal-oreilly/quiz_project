# class User:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#         print("New user created...")
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "Mihi")
# user_2 = User("002", "Bobby")
#
# user_1.follow(user_2)
#
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)


from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)
