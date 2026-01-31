symptom(john, fever).
symptom(john, cough).

diagnosis(john, flu) :-
    symptom(john, fever),
    symptom(john, cough).
