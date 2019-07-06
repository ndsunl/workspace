my_name = 'Zed A. Shaw'
my_age = 35     # not a lie
my_height = 74  # inches
my_weight = 180
my_eye = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d cm tall." % (my_height * 2.54))
print("He's %d kg heavy." % (my_weight * 0.4535924))
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eye, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this Line is trick, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))