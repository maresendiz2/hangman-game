from methods_help import method_help
from functions import function
from returnStuff import returnS
from function_interactions import *
method_help()
function()
returnS()


sticks = ["-", "--", "---", "----", "-----"]
my_mix = mix(sticks)

try1 = try_your_luck()
print(try1)

verify_my_try(my_mix, try1)