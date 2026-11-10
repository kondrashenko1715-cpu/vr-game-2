extends RigidBody3D

var is_grabbed = false
var grabbing_hand: Node3D = null
var last_position = Vector3.ZERO
var throw_velocity = Vector3.ZERO

func _ready():
	# Настраиваем космическое трение, чтобы куб плавно останавливался по инерции
	linear_damp = 1.2
	angular_damp = 1.2

func _physics_process(delta):
	if is_grabbed and grabbing_hand:
		# Кубик послушно следует за координатами вашей VR-руки
		global_position = grabbing_hand.global_position
		
		# Рассчитываем скорость взмаха руки для будущей инерции
		if delta > 0:
			throw_velocity = (global_position - last_position) / delta
		last_position = global_position

# Эта функция сработает, когда луч от руки Pico 4 наведется на куб и вы зажмете передний триггер
func _on_touch_down(hand_node: Node3D):
	is_grabbed = true
	grabbing_hand = hand_node
	freeze = true # Временно отключаем физику на время удержания рукой
	last_position = global_position

# Эта функция сработает, когда вы отпустите переднюю кнопку контроллера
func _on_touch_up():
	if is_grabbed:
		is_grabbed = false
		freeze = false # Возвращаем куб в невесомость
		grabbing_hand = null
		
		# ПЕРЕДАЕМ ИМПУЛЬС: Кубик летит вперед со скоростью броска вашей руки!
		linear_velocity = throw_velocity
