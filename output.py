import hardware

arm_speed = 0

def led_on():
	print("Called led_on()")
	pass

def led_off():
	print("Called led_off()")
	pass

def led_fast_blink():
	print("Called led_fast_blink()")
	pass

def led_slow_blink():
	print("Called led_slow_blink()")
	pass

def move_head():
	print("Called move_head()")
	pass

def dont_move_head():
	print("Called dont_move_head()")
	pass

def puke():
	print("Called puke()")
	pass

def dont_puke():
	print("Called dont_puke()")
	pass

def set_arm_speed(speed):
	print("Called set_arm_speed()")
	arm_speed = speed
	pass

def get_arm_speed():
	print("Called get_arm_speed()")
	return arm_speed

def shout():
	print("Called shout()")
	pass

def dont_shout():
	print("Called dont_shout()")
	pass



led_off()
dont_move_head()
dont_move_head()
dont_move_head()
set_arm_speed(0)