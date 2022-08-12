
# My Code

# Get names from invite list into a list
# with open(r'.\Input\Names\invited_names.txt') as f:
#     names = f.readlines()
#     clean_names = []
#     for name in names:
#         clean_names.append(name.strip())
#
# # Replace [name] with a name
# with open(r'.\Input\Letters\starting_letter.txt') as f:
#     message = f.readlines()
#     for x in clean_names:
#         new_name = message[0].replace('[name]', f'{x}')
# # Write the new invites
#         my_string = ''
#         for y in message[1:]:
#             my_string += y
#         with open(rf".\Output\ReadyToSend\{x}'s invite.txt",
#                   'w') as finish_file:
#             finish_file.write(new_name)
#             finish_file.write(my_string)


# Instructors code

PLACEHOLDER = '[name]'

with open(r'.\Input\Names\invited_names.txt') as names:
    names = names.readlines()

with open(r'.\Input\Letters\starting_letter.txt') as letter_file:
    message = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = message.replace(PLACEHOLDER, stripped_name)
        with open(rf".\Output\ReadyToSend\{stripped_name}'s invite.txt", 'w') as finish_file:
            finish_file.write(new_letter)