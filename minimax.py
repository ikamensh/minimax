from math import inf


def evaluate(node):
    return node.value or 0

def minimax(node, depth, maximisingPlayer):
    children = node.children
    if depth == 0 or len(children) == 0:
        return evaluate(node)

    if maximisingPlayer:
        values = [minimax(x, depth - 1, False) for x in children]
        return max(values)
    else:
        values = [minimax(x, depth - 1, True) for x in children]
        return min(values)


class Node:
    def __init__(self, value=None, children=None):
        if not value:
            assert len(children) > 0

        self.value = value
        self.children = children or []

    def __repr__(self):
        if self.children:
            return f"a node with {len(self.children)} children"
        else:
            return f"{self.value}"


branch_a = Node(children=[
                Node(children=[
                    Node(children=[Node(10),
                                   Node(inf)]),
                    Node(children=[Node(5)])
                ]),
                Node(children=[
                    Node(children=[Node(-10)])
                ])
            ])

sub_c = Node(children=[
                    Node(children=[Node(7),
                                   Node(5)]),
                    Node(children=[Node(-inf)])
                ])

sub_d = Node(children=[
                    Node(children=[Node(-7),
                                   Node(-5)])
                ])

branch_b = Node(children=[sub_c, sub_d])



start = Node(children=[
            branch_a,
            branch_b
        ])


print(minimax(start, 10, True))
#
print(minimax(branch_a,10,False))

print(minimax(branch_b,10,False))

print(minimax(sub_c,10,True))

print(minimax(sub_d,10,True))



# ez = Node(children=[Node(-7),Node(-5)])
#
# print(minimax(ez, 10, True))
#
# print(minimax(ez, 10, False))



