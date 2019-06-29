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

class Dog:
    def name(self):
        return "Fido"

    def _tail(self):
        # Prefixing a method with an underscore implies private scope
        return "wagging"

    def __password(self):
        return 'password' # Genius!

rover = Dog()
print(rover._Dog__password())