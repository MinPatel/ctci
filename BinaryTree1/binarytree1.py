from test import testEqual

def binarytree(r):
    return [r,[],[]]

def insert_left(r,new_value):
    t = r.pop(1)
    if len(t) > 1:
        r.insert(1,[new_value,t,[]])
    else:
        r.insert(1,[new_value,[],[]])
    return r

def insert_right(r, new_value):
    t = r.pop(2)
    if len(t) > 1:
        r.insert(2,[new_value,[],t])
    else:
        r.insert(2,[new_value,[],[]])
    return r

def get_root(r):
    return r[0]

def set_root(r, new_value):
    r[0] = new_value

def get_left_child(r):
    return r[1]

def get_right_child(r):
    return r[2]


r = binarytree('a')
print(r)
insert_left(r,'b')
insert_right(r[1],'d')
insert_right(r,'c')
insert_right(r[2],'f')
insert_left(r[2],'e')
#print(r)
set_root(r,'g')
#print(r)

testEqual(get_root(get_right_child(r)),'c')
testEqual(get_root(get_right_child(get_left_child(r))),'d')
testEqual(get_root(get_right_child(get_right_child(r))),'f')

