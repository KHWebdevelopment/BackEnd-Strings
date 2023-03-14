# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
""" PART 1 """
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)
print(scorers)

report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"
print(report)

""" PART 2 """
player = "Frank Rijkaard"

first_name = player[:player.find(" ")]
print(first_name)

last_name = player[player.find(" ") +1:]
print(last_name)
last_name_len = len(last_name)
print(last_name_len)

name_short = f"{player[0]}. {last_name}"
print(name_short)

first_name_len = len(first_name)
chant_1 = (first_name + "!" + " ") * first_name_len
chant = chant_1[:-1]

print(chant)

good_chant = chant[-1] != " "
print(good_chant)
print(2 != 3)
print(2 != 2)


