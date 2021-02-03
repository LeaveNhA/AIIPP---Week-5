# Implementation of classic arcade game Pong

import simplegui
import random

default_player_data = {'position': 0, 'score': 0, 'velocity': 0}

def generate_player_data(values):
    new_data = default_player_data.copy()
    new_data.update(values)
    return new_data

# initialize globals - pos and vel encode vertical info for paddles
GAME_CONSTANTS = {
    'screen': {
        'width': 600,
        'height': 400,
    },
    'game': {
        'velocity': 1.1,
        'ballRadius': 20,
        
        'left': False,
        'right': True,
        
        'speed': {'horizontal': [120, 240], 'vertical': [60, 180]}
    },
    'players': {
        'padWidth': 8,
        'padHeight': 80,
    },

    }

game_data = {
            'scores': [0, 0],
            'players': [default_player_data.copy(), default_player_data.copy()], # initialized!
            'ball': {'position': [0, 0], 'velocity': [], 'direction': 0} # this will be initialized!
            }

def spawn_ball(direction):
    # initialize ball position:
    game_data['ball']['position'] = [GAME_CONSTANTS['screen']['width'] / 2,
                                     GAME_CONSTANTS['screen']['height'] / 2]
    # initialize ball velocity:
    game_data['ball']['velocity'] = [random.randrange(*GAME_CONSTANTS['game']['speed']['horizontal']),
                                     random.randrange(*GAME_CONSTANTS['game']['speed']['vertical'])]
    
    if direction == GAME_CONSTANTS['game']['right']:
        game_data['ball']['velocity'][1] = -game_data['ball']['velocity'][1]
    if direction == GAME_CONSTANTS['game']['left']:
        game_data['ball']['velocity'][0] = -game_data['ball']['velocity'][0]
        game_data['ball']['velocity'][1] = -game_data['ball']['velocity'][1]
        
# define event handlers
def new_game():
    # Function scope calculations:
    starting_position = GAME_CONSTANTS['screen']['height'] / 2 # one value for all players!
    
    # re-initialize score:
    game_data['scores'] = [0, 0]
    # initialize players:
    game_data['players'] = [ generate_player_data({'position': starting_position}), generate_player_data({'position': starting_position}) ]
    # spawning ball:
    spawn_ball(random.choice([GAME_CONSTANTS['game']['left'], GAME_CONSTANTS['game']['right']]))

def draw(canvas):
    # it can be read like,
    # ------------------screen----width--
    w = GAME_CONSTANTS['screen']['width']			# screen width
    h = GAME_CONSTANTS['screen']['height']			# screen height
    pw = GAME_CONSTANTS['players']['padWidth']		# pad width
    ph = GAME_CONSTANTS['players']['padHeight']		# pad width
    br = GAME_CONSTANTS['game']['ballRadius']		# ball radius
    bp = game_data['ball']['position']				# ball position
    hpw = pw / 2									# half pad width
    hph = ph / 2									# half pad height
        
    # drawing lines:
    canvas.draw_line([w / 2, 0], [w / 2, h], 1, "White")
    canvas.draw_line([pw, 0],[pw, h], 1, "White")
    canvas.draw_line([w - pw, 0],[w - pw, h], 1, "White")
    
    # update ball position:
    if bp[1] <= br or bp[1] >= h - br:  
        game_data['ball']['velocity'][1] = - game_data['ball']['velocity'][1] # negative the position
        
    if bp[0] <= br:
        if game_data['players'][0]['position'] - hph <= bp[1] <= game_data['players'][0]['position'] + hph:
            game_data['ball']['velocity'][0] = -game_data['ball']['velocity'][0]
            game_data['ball']['velocity'][0] *= GAME_CONSTANTS['game']['velocity']
            game_data['ball']['velocity'][1] *= GAME_CONSTANTS['game']['velocity']
        else:
            spawn_ball(GAME_CONSTANTS['game']['right'])
            game_data['scores'][1] += 1
            
    if bp[0] >= w - br:
        if game_data['players'][1]['position'] - hph <= bp[1] <= game_data['players'][1]['position'] + hph:
            game_data['ball']['velocity'][0] = -game_data['ball']['velocity'][0]
            game_data['ball']['velocity'][0] *= GAME_CONSTANTS['game']['velocity']
            game_data['ball']['velocity'][1] *= GAME_CONSTANTS['game']['velocity']
        else:
            spawn_ball(GAME_CONSTANTS['game']['left'])
            game_data['scores'][0] += 1
            
    # handle velocity:
    game_data['ball']['position'][0] += game_data['ball']['velocity'][0] / 100
    game_data['ball']['position'][1] += game_data['ball']['velocity'][1] / 100
    
    # draw ball:
    canvas.draw_circle(bp, br, 2, "Red", "White")
    
    if hph <= game_data['players'][0]['position'] + game_data['players'][0]['velocity'] <= h - hph:
        game_data['players'][0]['position'] += game_data['players'][0]['velocity']
    if hph <= game_data['players'][1]['position'] + game_data['players'][1]['velocity'] <= h - hph:
        game_data['players'][1]['position'] += game_data['players'][1]['velocity']
    
    # draw paddles:
    # player 1:
    canvas.draw_line([0, game_data['players'][0]['position'] + hph],
                     [0, game_data['players'][0]['position'] - hph], pw, "White")
    # player 2:
    canvas.draw_line([w, game_data['players'][1]['position'] + hph],
                     [w, game_data['players'][1]['position'] - hph], pw, "White")
    
    # draw scores, after the score is calculated.
    canvas.draw_text(str(game_data['scores'][0]) + "     " + str(game_data['scores'][1]), (w / 2 - 36, 40), 30, "Green")      
    
        
def keydown(key):
    # player 1:
    if key == simplegui.KEY_MAP['s']:  
        game_data['players'][0]['velocity'] = 3
    elif key == simplegui.KEY_MAP['w']:  
        game_data['players'][0]['velocity'] = -3  
    # player 2:
    elif key == simplegui.KEY_MAP['up']:  
        game_data['players'][1]['velocity'] = -3  
    elif key == simplegui.KEY_MAP['down']:  
        game_data['players'][1]['velocity'] = 3

def keyup(key):
    # player 1:
    if key == simplegui.KEY_MAP['s']:
        game_data['players'][0]['velocity'] = 0
    elif key == simplegui.KEY_MAP['w']:  
        game_data['players'][0]['velocity'] = 0
    # player 2:
    elif key == simplegui.KEY_MAP['up']:  
        game_data['players'][1]['velocity'] = 0
    elif key == simplegui.KEY_MAP['down']:  
        game_data['players'][1]['velocity'] = 0
    
# create frame
frame = simplegui.create_frame("Pong", GAME_CONSTANTS['screen']['width'], GAME_CONSTANTS['screen']['height'])
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart_button = frame.add_button('Restart', new_game, 100)

# start frame
new_game()
frame.start()
