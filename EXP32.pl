
match(_, []).

match([X|T1], [X|T2]) :-
    match(T1, T2).

match([_|T], P) :-
    match(T, P).
