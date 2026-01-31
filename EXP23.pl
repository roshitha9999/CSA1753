parent(john, mary).
parent(john, paul).
parent(mary, elsa).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
