# class PracticeClass:
#     def method_with_defaults(a, b = 'default value'):
#         return [a,b]
#     def method_with_var_args(*args):
#         return args
#     def function_with_the_same_name(self, a, b):
#         return a + b

#     def test_functions_without_self_arg_are_global_functions(self):
#         def function_with_the_same_name(a, b):
#             return a * b

# a = PracticeClass.function_with_the_same_name(3,4)
# print(a)
# a = method_with_defaults(1)
# print (a)
# a = PracticeClass.method_with_var_args()
# print(a)

# a = PracticeClass.method_with_var_args('one')
# print(a)

# class Dog:
#     def name(self):
#         return "Fido"

#     def _tail(self):
#         # Prefixing a method with an underscore implies private scope
#         return "wagging"

#     def __password(self):
#         return 'password' # Genius!

# rover = Dog()
# print(rover._Dog__password())


# # i = 1
# # result = 1
# # while i <= 10:
# #     result = result * i
# #     i += 1

# # print(result)

# # i = 1
# # result = 1
# # while True:
# #     if i > 10: break
# #     result = result * i
# #     i += 1
# # print(result)


# # i = 0
# # result = []
# # while i < 10:
# #     i += 1
# #     if (i % 2) == 0: continue
# #     result.append(i)
# # print(result)

# round_table = [
#             ("Lancelot", "Blue"),
#             ("Galahad", "I don't know!"),
#             ("Robin", "Blue! I mean Green!"),
#             ("Arthur", "Is that an African Swallow or European Swallow?")
#         ]
# result = []
# for knight, answer in round_table:
#     result.append("Contestant: '" + knight + "'   Answer: '" + answer + "'")

# print(result[2])
# highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']
# there_can_only_be_only_one = set(highlanders)
# print(there_can_only_be_only_one)
# print(set())

from koans import triangle

print(triangle.triangle(1,2,3))
it = iter(range(1,6))

total = 0

for num in it:
    total += num

print(total)