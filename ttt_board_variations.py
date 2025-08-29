def print_board1():
    ...
    print("\n_|__|_\n_|__|_\n |  |\n")
   
    x = "X"
    y = "O"

    ######################
    # STARTING CONDITION #
    ######################
    
    empty_board = f"""
         |     |     
         |     |     
    _____|_____|_____
         |     |     
         |     |     
    _____|_____|_____
         |     |     
         |     |     
         |     |     

    """
    print(empty_board)

    ####################
    # FINISHED EXAMPLE #
    ####################

    ttt = f"""
         |     |     
      {x}  |  {y}  |  {y}     
    _____|_____|_____
         |     |     
      {y}  |  {x}  |  {y}     
    _____|_____|_____
         |     |     
      {y}  |  {y}  |  {x}     
         |     |     

    """
    print(ttt)

    ##############
    # NAVIGATION #
    ##############

    row = (1,2,3) #input would be R1, R2, R3
    row_nav = ("left", "middle" ,"right")
    column = (1,2,3) #input would be C1, C2, C3
    column_nav = ("top", "center", "bot")

    player_choice = (1,2,3,4,5,6,7,8,9)
    x = "X"
    o = "O"
    e = " "
    v1, v2, v3, v4, v5, v6, v7, v8, v9 = (x, x, o, o, o, x, x, o, x)

    ttt = f"""
         |     |     
      {v1}  |  {v2}  |  {v3}     
    _____|_____|_____
         |     |     
      {v4}  |  {v5}  |  {v6}     
    _____|_____|_____
         |     |     
      {v7}  |  {v8}  |  {v9}     
         |     |     

    """
    print(ttt)
    v = (e, e, e, e, e, e, e, e, e)
    
    ttt = f"""
         |     |     
      {v[0]}  |  {v[1]}  |  {v[2]}     
    _____|_____|_____
         |     |     
      {v[3]}  |  {v[4]}  |  {v[5]}     
    _____|_____|_____
         |     |     
      {v[6]}  |  {v[7]}  |  {v[8]}     
         |     |     

    """
    print(ttt)

print_board1()

def print_board2(v = (' ',)*9):

    ttt = f"""
         |     |     
      {v[0]}  |  {v[1]}  |  {v[2]}     
    _____|_____|_____
         |     |     
      {v[3]}  |  {v[4]}  |  {v[5]}     
    _____|_____|_____
         |     |     
      {v[6]}  |  {v[7]}  |  {v[8]}     
         |     |     

    """
    print(ttt)

x = "X"
o = "O"
e = " "

print_board2(v = (x, "a", e, e, e, e, e, e, e))
    
print_board2()
