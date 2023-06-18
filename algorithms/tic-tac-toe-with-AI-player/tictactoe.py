# TO DO
''' 
# Update variable to intuitive variables
# Clean code and formatting
# improve comments

'''

from graphics import Canvas
import time
import random
import copy
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

SIZE = 100

DELAY=0.01


def main():
    #design canvas to create columns & rows 
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # set black background
    background = canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, color="black")
    
    # draw columns & rows 
    draw_columns(canvas,CANVAS_WIDTH,CANVAS_HEIGHT, color="white")
    draw_rows(canvas,CANVAS_WIDTH,CANVAS_HEIGHT,color="white")
    
    # get squares 
    list_of_boundary= boundaries()
    available_moves = boundaries()
    
    # default position
    click_x,click_y=[0,0]
    
    #Default user ID
    USER_ID=random.choice([1,2,3,4])
    #USER_ID=2
    # user list to record positions/squares chosen
    USER_1=[]
    USER_2=[]
    
    # print scores
    #user_text = canvas.create_text(1, 387,text="USER:O", color="white")
    
    
    # start game flow
    while True:
        print(USER_ID)
        if USER_ID % 2> 0 : #Switch between Players
            user_text = canvas.create_text(1, 387,text="Your turn (O)", color="white")
            while True:
                canvas.wait_for_click()
                time.sleep(DELAY)
                click_x,click_y = canvas.get_last_click()
            
                for i in list_of_boundary:
                    if round(click_x) <= (round(i[0])) and (round(click_y) <= round(i[1])):
                        x_dim, y_dim = center_point(i[0], i[1])
                        break
                # check if move in available moves
                if i in available_moves:
                    canvas.delete(user_text)
                    break
                else:
                    game_error_pop_up(canvas,time)
                    
            # user generates circle
            circle = canvas.create_oval(x_dim, y_dim, x_dim+SIZE, y_dim+SIZE, color="white")
            dent_circle = create_hole(canvas, x_dim, y_dim, SIZE ,"black")
            
            # update user choices
            USER_1,available_moves = update_choice(USER_1,available_moves,i)
            
        else:
            #AI turn informational text 
            cpu_text = canvas.create_text(370, 387,text="AI's Turn (X)", color= "white")
            # get random choice from cpu
            #cpu_choice = random.choice(available_moves)
            cpu_choice = cpu_player(canvas,list_of_boundary, available_moves,USER_1,USER_2)
            cpu_x_dim,cpu_y_dim = cpu_choice
            
            cpu_x_dim,cpu_y_dim =round(cpu_x_dim)-CANVAS_WIDTH*(1/6)-(SIZE/2), round(cpu_y_dim)-CANVAS_HEIGHT*(1/6)-(SIZE/2)
            
            time.sleep(DELAY*20)
            text = canvas.create_text(cpu_x_dim+(SIZE/7),cpu_y_dim, text='X', font_size=SIZE+20, font="Lato", color="white")
            
            canvas.delete(cpu_text)
            # up


            USER_2,available_moves =update_choice(USER_2,available_moves,cpu_choice)
        print(list_of_boundary)
        # Increment & Switch between users
        USER_ID+=1
        print("User 1 : ",USER_1)
        print("User 2 : ",USER_2)
        

        # generate game outcome
        game_end,_,result,winning_sequence = game_outcome(USER_1, USER_2)
        
        print("winning sequence: ", winning_sequence)
    
        if game_end=="yes":
            break
        if len(result)==0 and len(available_moves)==0:
            result="A Draw !"
            print("Draw !")
            break
    draw_winning_sequence(canvas, result,winning_sequence)    
    display_result(canvas, result)

    time.sleep(DELAY)
        #click = canvas.get_last_click()
        
def draw_winning_sequence(canvas, result,winning_sequence):
    if result == "You win!":
        for i in winning_sequence:
            x_dim, y_dim = center_point(i[0], i[1])
            circle = canvas.create_oval(x_dim, y_dim, x_dim+SIZE, y_dim+SIZE, color="green")
            dent_circle = create_hole(canvas, x_dim, y_dim, SIZE ,"black")
        
        
    elif result == "AI wins!":
        for i in winning_sequence:
            cpu_x_dim,cpu_y_dim = i
            cpu_x_dim,cpu_y_dim =round(cpu_x_dim)-CANVAS_WIDTH*(1/6)-(SIZE/2), round(cpu_y_dim)-CANVAS_HEIGHT*(1/6)-(SIZE/2)
            text = canvas.create_text(cpu_x_dim+(SIZE/7),cpu_y_dim, text='X', font_size=SIZE+20, font="Lato", color="red")

def display_result(canvas, result):
    '''Display final result after game ends
    '''
    if result == "You win!":
        color = "white"
    elif result == "AI wins!":
        color = "white"
    else:
        color = "yellow"
        
    canvas.create_text((CANVAS_WIDTH/2)-80, (CANVAS_HEIGHT/2)-20, result, font='Lato', font_size = 50, color=color)
        
def corner_move(canvas,list_of_boundary):
    corner_move=[]
    for i in range(len(list_of_boundary)):
        if i in [0,2,6,8]:
            corner_move.append(list_of_boundary)
            
    return corner_move[0]
        


def cpu_player(canvas,list_of_boundary, available_moves,USER_1,USER_2):
    corner_moves = corner_move(canvas,list_of_boundary)
    available_moves_ = copy.deepcopy(available_moves)
    if available_moves == list_of_boundary:
        return [266.66666666666663, 266.66666666666663]
    elif ([266.66666666666663, 266.66666666666663] not in 
    available_moves) and (len(available_moves)==8) :
        return random.choice(corner_moves)
        
    elif len(USER_1)>=2:
        user_moves = copy.deepcopy(USER_1)
        ai_moves = copy.deepcopy(USER_2)
        user_dummy=[[1,1],[2,2],[3,4]]
        
        #Check winning position for AI and chose that move
        for i in available_moves:
            user_dummy
            ai_moves.append(i)
            best_move= game_outcome(user_dummy,ai_moves)[1]
            #print("debug: ", best_move)
            if best_move is not None:
                return best_move
                break
            ai_moves = ai_moves[:-1]
        
        # check winning position for User and block that move
        if best_move is None:
            for i in available_moves:
                user_moves.append(i)
                ai_moves.append(i)
                best_move= game_outcome(user_moves, ai_moves)[1]
                #print("debug: ", best_move)
                if best_move is not None:
                    return best_move
                    break
                user_moves = user_moves[:-1]
                ai_moves = ai_moves[:-1]
        
        if best_move is None:
            return random.choice(available_moves)
    elif [266.66666666666663, 266.66666666666663] in available_moves:
        return [266.66666666666663, 266.66666666666663] 
        
    else:
        return random.choice(available_moves)


def game_error_pop_up(canvas,time):

    pop_up = canvas.create_text((CANVAS_WIDTH/2)-120, (CANVAS_HEIGHT/2)-20, 'CHOOSE EMPTY SQUARE', font='Lato', font_size = 20, color='red')
    time.sleep(DELAY)
    canvas.delete(pop_up)

def create_hole(canvas, x_dim, y_dim,size,color):
    x1, y1, x2, y2 = x_dim+(SIZE*1/8), y_dim+(SIZE*1/8), x_dim+SIZE-(SIZE*1/8), y_dim+SIZE-(SIZE*1/8)
    canvas.create_oval(x1, y1, x2,y2, color)
    
def center_point(x_coord, y_coord):
    ''' Center the shapes in the middle of each square
    '''
    x_centred, y_centred= round(x_coord)-CANVAS_WIDTH*(1/6)-(SIZE/2), round(y_coord)-CANVAS_HEIGHT*(1/6)-(SIZE/2)
    return x_centred, y_centred

def update_choice(user,squares_available,i):
    ''' add players choice and reduce overall choices left
    '''
    user.append(i)
    squares_available.remove(i)
    
    return user,squares_available
    
def game_outcome(USER_1, USER_2):
    winning_combination =[[[266.66666666666663, 133.33333333333331], 
    [266.66666666666663, 266.66666666666663], 
    [266.66666666666663, 400]],
    [[133.33333333333331, 133.33333333333331], 
    [133.33333333333331, 266.66666666666663], 
    [133.33333333333331, 400]], 
    [[400, 133.33333333333331], 
    [400, 266.66666666666663], 
    [400, 400]],
    [[400, 133.33333333333331],
    [266.66666666666663, 266.66666666666663], 
    [133.33333333333331, 400]],
    [[133.33333333333331, 133.33333333333331], 
    [266.66666666666663, 266.66666666666663], 
    [400, 400]],
    [[133.33333333333331, 266.66666666666663], 
    [266.66666666666663, 266.66666666666663], 
    [400, 266.66666666666663]],
    [[133.33333333333331, 400], 
    [266.66666666666663, 400], 
    [400, 400]],
    [[133.33333333333331, 133.33333333333331], 
    [266.66666666666663, 133.33333333333331], 
    [400, 133.33333333333331]]]
        
    winning_sequence=None
    outcome=""
    best_move_priority = None
    best_move = None
    game_end = "no"
    for i in winning_combination:
        player2_win_combo=0
        for k in USER_2:
            if k in i:
                player2_win_combo+=1
        
        if player2_win_combo ==3:
            outcome = "AI wins!"
            print("AI wins!")
            winning_sequence=i
            game_end= "yes"
            best_move_priority = USER_2[-1]
            break
        
        
        player1_win_combo=0
        for j in USER_1:
            if j in i:
                player1_win_combo+=1

        if player1_win_combo ==3:
            outcome = "You win!"
            print("You win!")
            winning_sequence=i
            game_end="yes"
            best_move = USER_1[-1] 
            break
    if best_move_priority is not None:
        best_move=best_move_priority
    
    return game_end,best_move,outcome,winning_sequence
    
def boundaries():
    #upper limits
    x_points = [CANVAS_WIDTH*(1/3),CANVAS_WIDTH*(2/3),CANVAS_WIDTH]
    y_points = [CANVAS_HEIGHT*(1/3),CANVAS_HEIGHT*(2/3),CANVAS_HEIGHT]
    
    square_coordinates=[]
    for i in x_points:
        for j in y_points:
            square_coordinates.append([i,j])
    return square_coordinates
        
def draw_columns(canvas,canvas_width,canvas_height,color):
    y1= 10
    y2= canvas_height-10
    
    column_line1 = canvas.create_line(canvas_width*(1/3), y1, canvas_width*(1/3), y2, color)
    column_line2 = canvas.create_line(canvas_width*(2/3), y1, canvas_width*(2/3), y2, color)
    
def draw_rows(canvas,canvas_width,canvas_height,color):
    x1=10
    x2=canvas_width-10
    
    row_line1 = canvas.create_line(x1, canvas_height*(1/3), x2, canvas_height*(1/3), color)
    row_line2 = canvas.create_line(x1, canvas_height*(2/3), x2, canvas_height*(2/3), color)

if __name__ == '__main__':
    main()
