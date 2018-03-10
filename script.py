import markovify

# Get raw text as string.
with open("input.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(text_model.make_short_sentence(140))

# Generate a setence and find out by the user if they want to tweet it.
print(text_model.make_short_sentence(140))
print('Would you like to tweet this?')
postTweet = input()
if postTweet.lower() in ['y', 'yes', 'true']:
    print('cool')
    #TODO: Do twitter implementation here