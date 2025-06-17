# einkaufsliste
Kleines Programm mit Customtkinter für das UI


falsch.png: Falsche Proportionen, die durch den Scrollframe entstehen
richtig.png: Richtige Proportionen, wobei der Scrollframe auskommentiert ist

Vermutung: Scrollframe hat ein Problem mit parenting (dem Frame "sl" als parent)
Lösung: Internet, ChatGPT und die Option über Canvas statt Frame replizieren das Problem, bringen aber keine Lösung
