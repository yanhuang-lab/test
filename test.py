#!/opt/anaconda3/envs/conda-py310/bin/python3

#testtest

def add_underscores(word):
    new_word = "_"
    for i in range(len(word)):
        # test change
        new_word = new_word + word[i] + "_"
    return new_word

word = "Python"
print(add_underscores(word))
