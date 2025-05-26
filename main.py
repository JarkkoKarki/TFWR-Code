
def get_coords():
	return [get_pos_x(), get_pos_y()]

def move_to(x1, y1):
	x = get_pos_x()
	y = get_pos_y()
	z = get_world_size()
	dx = x1 - x
	dy = y1 - y
	dx1 = abs(dx)
	dy1 = abs(dy)
	xFlip = dx != dx1
	yFlip = dy != dy1
	if dx1 > z / 2:
		dx1 = z - dx1
		xFlip = not xFlip
	if dy1 > z / 2:
		dy1 = z - dy1
		yFlip = not yFlip
	for r in range(dx1):
		if xFlip:
			move(West)
		else:
			move(East)
	for r in range(dy1):
		if yFlip:
			move(South)
		else:
			move(North)
def plant_cacti():
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type != Entities.Cactus:
		plant(Entities.Cactus)		
def sow_cacti():
	move_to(0,0)
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			use_item(Items.Water)
			plant_cacti()
			move(North)
		move(East)
def sort_cacti():
	move_to(0, 0)
    cactus_map = []
    
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            x, y = get_pos_x(), get_pos_y()
            value = measure()
            cactus_map.append((x, y, value))
            move(North)
        move(East)
    
    sorted = False
    
	while not sorted:
		sorted = True
		for j in range(get_world_size() - 1):
			for i in range(get_world_size()):
				index = i * get_world_size() + j
				if cactus_map[index][2] > cactus_map[index + 1][2]:
					move_to(cactus_map[index][0], cactus_map[index][1])
					swap(North)
					cactus_map[index] = get_pos_x(), get_pos_y(), measure()
					move_to(cactus_map[index + 1][0], cactus_map[index + 1][1])
					cactus_map[index + 1] = get_pos_x(), get_pos_y(), measure()
					sorted = False
					
		for i in range(get_world_size() - 1):
			for j in range(get_world_size()):
				index = i * get_world_size() + j
				if cactus_map[index][2] > cactus_map[(i + 1) * get_world_size() + j][2]:
					move_to(cactus_map[index][0], cactus_map[index][1])
					swap(East)
					cactus_map[index] = get_pos_x(), get_pos_y(), measure()
					move_to(cactus_map[(i + 1) * get_world_size() + j][0], cactus_map[(i + 1) * get_world_size() + j][1])
					cactus_map[(i + 1) * get_world_size() + j] = get_pos_x(), get_pos_y(), measure()
					sorted = False
		
	harvest()
	

def is_even(n):
	return n % 2 == 0

def harvest_hay(minimum):
	clear()
	minimum2x = minimum + farmed_each_time
	while num_items(Items.Hay) < minimum2x:
		for i in range(get_world_size()):
			harvest()
			move(North)
		move(East)

def harvest_wood(minimum):
	clear()
	minimum2x = minimum + farmed_each_time
	while num_items(Items.Wood) < minimum2x:
		for n in range(get_world_size()):
			n = is_even(get_pos_y())
			if n:
				if get_entity_type() != Entities.Tree:
					harvest()
					plant(Entities.Tree)
				if can_harvest():
					harvest()
					plant(Entities.Tree)
				move(North)
			else:
				harvest_bush()
				move(North)
		move(East)
		for n in range(get_world_size()):
			n = is_even(get_pos_y())
			quick_print(is_even(get_pos_y()))
			if not n:
				if get_entity_type() != Entities.Tree:
					harvest()
					plant(Entities.Tree)
				if can_harvest():
					harvest()
					plant(Entities.Tree)
				move(North)
			else:
				harvest_bush()
				move(North)
		move(East)

def harvest_carrot(minimum):
	clear()
	minimum2x = minimum + farmed_each_time
	while num_items(Items.Carrot) < minimum2x:
		for n in range(get_world_size()):
			if get_ground_type() == Grounds.Grassland:
				till()
				if get_water() < 0.7:
					use_item(Items.Water)
				plant(Entities.Carrot)	
			if can_harvest():
				harvest()
				if get_water() < 0.7:
					use_item(Items.Water)
				plant(Entities.Carrot)	
			move(North)
		move(West)
		
def harvest_pumpkin(minimum):
	clear()
	minimum2x = minimum + farmed_each_time
	while num_items(Items.Pumpkin) < minimum2x:
		b = get_world_size()**2
		quick_print(b)
		count = []
		x=0
		while len(count) < b:
			quick_print(x)
			for n in range(get_world_size()):
				if get_entity_type() == Entities.Grass:
					harvest()
					if get_water() < 0.7:
							use_item(Items.Water)
					plant(Entities.Pumpkin)
					count.append(1)
				if get_entity_type() != Entities.Pumpkin:
					plant(Entities.Pumpkin)
					if len(count) > 0:
						for x in range(len(count)):
							count.pop()
				if get_entity_type() == Entities.Pumpkin:
					count.append(1)
				if get_ground_type() == Grounds.Grassland:
					till()
					if get_water() < 0.7:
							use_item(Items.Water)
					plant(Entities.Pumpkin)	
				quick_print(count)
				move(North)
				x = len(count)
			move(East)
		for v in range(1):
			harvest()	
			
def harvest_sun(minimum):
	clear()
	minimum2x = minimum + farmed_each_time
	while num_items(Items.Power) < minimum2x:
		measures = []
		x = get_world_size()**2
		while len(measures) != x:
			quick_print(measures)
			for n in range(get_world_size()):
				if get_ground_type() == Grounds.Grassland or get_entity_type() != Entities.Sunflower:
					if get_ground_type() == Grounds.Grassland:
						till()
						if get_water() < 0.7:
							use_item(Items.Water)
						plant(Entities.Sunflower)
						measures.append(measure())
						move(North)
					else:
						plant(Entities.Sunflower)
						measures.append(measure())
						move(North)
			move(East)
		while len(measures) > 0:
			quick_print(measures)
			for n in range(get_world_size()):
				if get_entity_type() == Entities.Sunflower:
					v = measure()
					if v != max(measures):
						move(North)
					else:
						if can_harvest():
							harvest()
							measures.remove(v)
	
				else:
					move(North)
					
			move(East)
			
def harvest_sub(minimum):
	clear()
	minimum2x = minimum + farmed_each_time
	while num_items(Items.Weird_Substance) < minimum2x:
		for i in range(get_world_size()):
			harvest()
			plant(Entities.Bush)
			use_item(Items.Fertilizer)
			move(North)
		move(East)
		
def harvest_cac(minimum):
	clear()
	minimum2x = minimum + farmed_each_time
	while num_items(Items.Cactus) < minimum2x:
        sow_cacti()
        sort_cacti()
        
def harvest_bone(minimum):
	clear()
	minimum2x = minimum + farmed_each_time
	while num_items(Items.Bone) < minimum2x:
		change_hat(Hats.Straw_Hat)
		set_world_size(6)
		change_hat(Hats.Dinosaur_Hat)
		for v in range(100):
			for x in range(5):
				for i in range(2):
					move(North)
				move(East)
				for i in range(2):
					move(South)
				move(East)
			for x in range(5):
				for i in range(2):
					move(South)
				move(West)
				for i in range(2):
					move(North)
				move(West)
			move(South)
			move(South)
			
def harvest_g(minimum):
	clear()
	set_world_size(8)
	minimum2x = minimum + farmed_each_time
	directionss=[]
	while num_items(Items.Gold) < minimum2x:
		if get_entity_type() != Entities.Hedge or get_entity_type() != Entities.Treasure or get_entity_type()==Entities.Grass:
			harvest()
			plant(Entities.Bush)
			while not can_harvest():
				pass
			if can_harvest():
				use_item(Items.Weird_Substance, 25)
		if get_entity_type() == Entities.Hedge or get_entity_type() == Entities.Treasure:
			start = get_tick_count()
			x=1
			directions = [North, East, South, West]
			for i in range(6):
				while get_entity_type() != Entities.Treasure:
					current = get_tick_count()
					ab = current - start
					if ab >= 200000:
						break
					for y in range(37):
						if get_entity_type() == Entities.Treasure:
							i+=1
							if i == 6:
								harvest()
								plant(Entities.Bush)
								while not can_harvest():
									pass
								if can_harvest():
									use_item(Items.Weird_Substance, 25)
							use_item(Items.Weird_Substance, 25)
	
						while not move(directions[x]):
							x+=1
							if x == 4:
								x=0
						x-=1
						if x == -1:
							x=3
					move(directions[(x+2)%4])
					x+=1
					if x == 4:
						x=0
				use_item(Items.Weird_Substance, 10)
			harvest()
			i=0
			
while True:
	farmed_each_time = 4000
	unlock(Unlocks.Pumpkins)
	unlock(Unlocks.Speed)
	unlock(Unlocks.Cactus)
	unlock(Unlocks.Dinosaurs)
	unlock(Unlocks.Mazes)
	unlock(Unlocks.Polyculture)
	unlock(Unlocks.Simulation)
	set_world_size(10)
	values = []
	items = {
		0: num_items(Items.Hay),
		1: num_items(Items.Wood),
		2: num_items(Items.Carrot),
		3: num_items(Items.Pumpkin),
		4: num_items(Items.Power),
		5: num_items(Items.Weird_Substance),
		6: num_items(Items.Cactus),
		7: num_items(Items.Bone),
		8: num_items(Items.Gold),
		}
	for k in items:
		values.append(items[k])
	minimum = min(values)
	for i in items:
		if items[i] == minimum:
			if i == 0:
				harvest_hay(minimum)
			elif i ==1:
				harvest_wood(minimum)
			elif i ==2:
				harvest_carrot(minimum)
			elif i ==3:
				harvest_pumpkin(minimum)
			elif i ==4:
				harvest_sun(minimum)
			elif i ==5:
				harvest_sub(minimum)
			elif i ==6:
				harvest_cac(minimum)
			elif i ==7:		
				harvest_bone(minimum)
			elif i ==8:			
				harvest_g(minimum)	
    
