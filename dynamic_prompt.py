from sys import argv

program_name, user_name = argv
prompt = "> "

print "You are %s and i am %s" % (user_name, program_name)
print "Do you like my minimalistic appearance, %s" % user_name
like = raw_input(prompt)
if like == "yes":
    like = "And it seems you really like me"

print "And how old are you btw? "
age = raw_input(prompt)

print """Okay! You are %r and
you're %r years old. %s""" % (user_name, age, like)
