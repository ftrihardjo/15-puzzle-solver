from heapq import *
def manhattan(candidate, solved, size):
    res = 0
    for i in range(size*size):
        if candidate[i] != 0 and candidate[i] != solved[i]:
            ci = solved.index(candidate[i])
            y = (i // size) - (ci // size)
            x = (i % size) - (ci % size)
            res += abs(y) + abs(x)
    return res

def linear_conflicts(candidate, solved, size):

    def count_conflicts(candidate_row, solved_row, size, ans=0):
        counts = [0 for x in range(size)]
        for i, tile_1 in enumerate(candidate_row):
            if tile_1 in solved_row and tile_1 != 0:
                for j, tile_2 in enumerate(candidate_row):
                    if tile_2 in solved_row and tile_2 != 0:
                        if tile_1 != tile_2:
                            if (solved_row.index(tile_1) > solved_row.index(tile_2)) and i < j:
                                counts[i] += 1
                            if (solved_row.index(tile_1) < solved_row.index(tile_2)) and i > j:
                                counts[i] += 1
        if max(counts) == 0:
            return ans * 2
        else:
            i = counts.index(max(counts))
            candidate_row[i] = -1
            ans += 1
            return count_conflicts(candidate_row, solved_row, size, ans)

    res = manhattan(candidate, solved, size)
    candidate_rows = [[] for y in range(size)] 
    candidate_columns = [[] for x in range(size)] 
    solved_rows = [[] for y in range(size)] 
    solved_columns = [[] for x in range(size)] 
    for y in range(size):
        for x in range(size):
            idx = (y * size) + x
            candidate_rows[y].append(candidate[idx])
            candidate_columns[x].append(candidate[idx])
            solved_rows[y].append(solved[idx])
            solved_columns[x].append(solved[idx])
    for i in range(size):
            res += count_conflicts(candidate_rows[i], solved_rows[i], size)
    for i in range(size):
            res += count_conflicts(candidate_columns[i], solved_columns[i], size)
    return res
class Node:
  def __init__(self,cost,position,step):
    self.cost = cost
    self.position = list(position)
    self.step = step
  def __lt__(self,node):
    return self.cost < node.cost
def solution(position):
  goal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
  if position == goal:
    return []
  initial = list(position)
  heap = []
  parents = {}
  x = position.index(0)//4
  y = position.index(0)%4
  if y:
    parent = list(position)
    n = position[x*4+y-1]
    position[x*4+y-1] = position[x*4+y]
    position[x*4+y] = n
    cost = 2*linear_conflicts(position,goal,4)+manhattan(position,goal,4)+1
    if tuple(position) not in parents.keys():
      heappush(heap,Node(cost,position,1))
      parents[tuple(position)] = (parent,n)
    n = position[x*4+y-1]
    position[x*4+y-1] = position[x*4+y]
    position[x*4+y] = n
  if x:
    parent = list(position)
    n = position[x*4+y-4]
    position[x*4+y-4] = position[x*4+y]
    position[x*4+y] = n
    cost = 2*linear_conflicts(position,goal,4)+manhattan(position,goal,4)+1
    if tuple(position) not in parents.keys():
      heappush(heap,Node(cost,position,1))
      parents[tuple(position)] = (parent,n)
    n = position[x*4+y-4]
    position[x*4+y-4] = position[x*4+y]
    position[x*4+y] = n
  if x < 3:
    parent = list(position)
    n = position[x*4+y+4]
    position[x*4+y+4] = position[x*4+y]
    position[x*4+y] = n
    cost = 2*linear_conflicts(position,goal,4)+manhattan(position,goal,4)+1
    if tuple(position) not in parents.keys():
      heappush(heap,Node(cost,position,1))
      parents[tuple(position)] = (parent,n)
    n = position[x*4+y+4]
    position[x*4+y+4] = position[x*4+y]
    position[x*4+y] = n
  if y < 3:
    parent = list(position)
    n = position[x*4+y+1]
    position[x*4+y+1] = position[x*4+y]
    position[x*4+y] = n
    cost = 2*linear_conflicts(position,goal,4)+manhattan(position,goal,4)+1
    if tuple(position) not in parents.keys():
      heappush(heap,Node(cost,position,1))
      parents[tuple(position)] = (parent,n)
    n = position[x*4+y+1]
    position[x*4+y+1] = position[x*4+y]
    position[x*4+y] = n
  while True:
    p = heappop(heap)
    position = p.position
    step = p.step
    if position != goal:
      x = position.index(0)//4
      y = position.index(0)%4
      if y:
        parent = list(position)
        n = position[x*4+y-1]
        position[x*4+y-1] = position[x*4+y]
        position[x*4+y] = n
        cost = 2*linear_conflicts(position,goal,4)+manhattan(position,goal,4)+step
        if tuple(position) not in parents.keys():
          heappush(heap,Node(cost,position,1+step))
          parents[tuple(position)] = (parent,n)
        n = position[x*4+y-1]
        position[x*4+y-1] = position[x*4+y]
        position[x*4+y] = n
      if x:
        parent = list(position)
        n = position[x*4+y-4]
        position[x*4+y-4] = position[x*4+y]
        position[x*4+y] = n
        cost = 2*linear_conflicts(position,goal,4)+manhattan(position,goal,4)+step
        if tuple(position) not in parents.keys():
          heappush(heap,Node(cost,position,1+step))
          parents[tuple(position)] = (parent,n)
        n = position[x*4+y-4]
        position[x*4+y-4] = position[x*4+y]
        position[x*4+y] = n
      if x < 3:
        parent = list(position)
        n = position[x*4+y+4]
        position[x*4+y+4] = position[x*4+y]
        position[x*4+y] = n
        cost = 2*linear_conflicts(position,goal,4)+manhattan(position,goal,4)+step
        if tuple(position) not in parents.keys():
          heappush(heap,Node(cost,position,1+step))
          parents[tuple(position)] = (parent,n)
        n = position[x*4+y+4]
        position[x*4+y+4] = position[x*4+y]
        position[x*4+y] = n
      if y < 3:
        parent = list(position)
        n = position[x*4+y+1]
        position[x*4+y+1] = position[x*4+y]
        position[x*4+y] = n
        cost = 2*linear_conflicts(position,goal,4)+manhattan(position,goal,4)+step
        if tuple(position) not in parents.keys():
          heappush(heap,Node(cost,position,1+step))
          parents[tuple(position)] = (parent,n)
        n = position[x*4+y+1]
        position[x*4+y+1] = position[x*4+y]
        position[x*4+y] = n
    else:
      answer = []
      while position != initial:
        answer.append(parents[tuple(position)][1])
        position = parents[tuple(position)][0]
      return answer[::-1]
