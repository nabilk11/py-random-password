import random;

lower = "abcdefghijklmnopqrstuvwxyz";
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
NUMBER = "0123456789";
SYMBOL = "[]{}#@!$%&*_-.";

all = lower + upper + NUMBER + SYMBOL
length = 8
random_pass = "".join(random.sample(all, length))
print("Your random password is ", random_pass)