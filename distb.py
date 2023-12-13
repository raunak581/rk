#distributive law for addition: a*(b+c) = (a*b)+(a*c)
a=4
b=2
c=3

left_side = a*(b+c)
right_side = (a*b)+(a*c)

if left_side == right_side:
	print("The associative law for addition holds: {a}*({b}+{c}) = ({a}*{b}) + ({a}*{c})")
else:
	print("the distributive law for addition does not hold.")