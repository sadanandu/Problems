class Square(object):

    def __init__(self, row, col, data):

        self.row_id = row

        self.col_id = col

        self.data = data

        self.left, self.right, self.up, self.down = None, None, None, None



    def __iter__(self):

        return iter([self.left, self.right, self.up, self.down])



class Maze(object):

    def __init__(self, locs):

        self.map = locs

        self.col_bound = len(locs[0])

        self.row_bound = len(locs)



    def squarize(self):

        #for left right dec/inc col num

        #for up down dec/inc row num

        for row_id, each_row in enumerate(self.map):

            for col_id, each_item in enumerate(each_row):

                s = Square(row_id, col_id, each_item)

                self.map[row_id][col_id] = s



        for row_id, each_row in enumerate(self.map):

            for col_id, each_item in enumerate(each_row):

               #setleft

                if self.in_boundry(row_id, col_id-1):

                    each_item.left = self.map[row_id][col_id-1]

                #setright

                if self.in_boundry(row_id, col_id + 1):

                    each_item.right = self.map[row_id][col_id+1]

                #setup

                if self.in_boundry(row_id-1, col_id):

                    each_item.up = self.map[row_id-1][col_id]

                #setdown

                if self.in_boundry(row_id+1, col_id):

                    each_item.down = self.map[row_id+1][col_id]





    def in_boundry(self, row, col):

        if 0<= row < self.row_bound and 0 <= col < self.col_bound:

            return True

        return False



    def get_square_with_value(self, val):

        for row_id, each_row in enumerate(self.map):

            for col_id, each_item in enumerate(each_row):

                if each_item.data == val:

                    return each_item



    def get_value(self, row, col):

        return self.map[row][col]



    def traverse(self):

        for each_row in self.map:

            print([each.data  for each in each_row ])



##    def print_maze(self):

##        for each_row in self.map:



##        row_num = 0

##        for rows in locs:

##            col_num = 0

##            for item in row:

##                sq = Square(row_num, col_num)

##                sq.data = item

##                maze_obj.squares.append(sq)

##                col_num += 1

##            row_num += 1



        #0     #1  #2   #3    #4   #5  #6   #7

locs=  [['*', '*', '*', '*', '*', '',  '' , ''],  #0

       ['*',  '', '', '', '*', '',     '',  ''],      #1

       ['*',  'S', '*', '*', '*',   '','' , ''],   #2

       ['*',  '', '', '', '*',     '*','*',  '*'],   #3

       ['*',  '', '*', '', '',     '', '' , '*'],     #4

       ['*',  '', '', '', '*',     '', '' , '*'],     #5

       ['*',  '*', '*', '*', '*',  '', 'E' , '*'], #6

       ['',  '', '', '', '*',     '*', '*' , '*']]    #7


        #0     #1  #2   #3    #4   #5  #6   #7

locs1=  [['*', '*', '*', '*', '*', '',  '' , ''],  #0

       ['*',  '', '', '', '*', '',     '',  ''],      #1

       ['*',  'S', '*', '*', '*',   '','' , ''],   #2

       ['*',  '', '', '', '*',     '*','*',  '*'],   #3

       ['*',  '', '*', '', '',     '', '' , '*'],     #4

       ['*',  '', '', '', '*',     '', '' , '*'],     #5

       ['*',  '*', '*', '*', '*',  '', 'E' , '*'], #6

       ['',  '', '', '', '*',     '*', '*' , '*']]    #7




maze_obj =Maze(locs1)

maze_obj.squarize()

#maze_obj.traverse()

s = maze_obj.get_square_with_value('S')

e = maze_obj.get_square_with_value('E')

#print s.data, s.left, s.right, s.up, s.down

#print e.data, e.left, e.right, e.up, e.down

reached = False
path = [s]

def is_there_a_path(start_square, end_square, path):
    global reached
    if not reached:

        for each_link in start_square:
            '''print('In ', start_square.row_id, start_square.col_id, start_square.data)
            print('now path is')
            for each in path:
                print(each.data, '(', each.row_id,',', each.col_id, ')')'''
            if each_link:
                if each_link == end_square:
                    reached = True
                    path.append(each_link)
                    return path

                if each_link.data != '*':
                    
                    if each_link not in path:
                        path.append(each_link)
                        #print('going through', each_link.row_id, each_link.col_id, each_link.data)
                        ret = is_there_a_path(each_link, end_square, path)
                        #print('got out from ', each_link.row_id, each_link.col_id, each_link.data)
                        if ret == None:
                            path.pop(-1)
                            #print('now path is')
                            #for each in path:
                            #    print(each.data, '(', each.row_id,',', each.col_id, ')')
                        else:
                            return ret
                    else:
                        pass
                        #print('skipping because this where i came from', each_link.row_id, each_link.col_id)
                else:
                    pass
                    #print('skipping because of *', each_link.row_id, each_link.col_id)
        return None

p = is_there_a_path(s, e, path)
if p:
    for each in p:
        print(each.data, '(', each.row_id,',', each.col_id, ')')
else:
    print('No path')
