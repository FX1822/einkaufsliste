from customtkinter import *

app = CTk()
app.geometry("480x320")
app.configure(bg_color="#2c3e50")
set_appearance_mode("Dark")
# ich hab keine Ahnung was das tut aber es scheint nicht zu schaden.
app.overrideredirect(True)

# Hauptproblem war du machst ein frame mit width=240 und dann machst du pack und er packt es wieder kleiner
# dein code: mit Kommentaren
# sl = CTkFrame(frame, width=240, height=320, fg_color="#1abc9c")  <---- sl ist 240, oder halbe Fensterbreite
# ...
# sl_label = CTkLabel(sl, text="Einkaufsliste", font=("Arial", 20), corner_radius=32, fg_color="#16a085", text_color="black")
# sl_label.pack(padx=10, fill="both", pady=3)  <---- uh oh wir packen das label in sl, damit wir die Größe von sl geändert
# ...
# sl_content_scrollframe = CTkScrollableFrame(sl, width=230, height=240, fg_color="#ecf0f1")
# sl_content_scrollframe.pack(padx=5, pady=5) <---- jetzt packen wir das sl_content_scrollframe aber das ändert die Größe unter Umständen nochmal?
# sl_content_scrollframe.pack_propagate(False) <---- jetzt soll sich die Größe vom scrollframe nicht mehr ändern, wenn man Kinder hinzufügt,
#                                                    leider ist dir Größe schon falsch

# vermutlich kann man das auch beheben indem man immer direkt pack_propagate(False) auf allen Frames aufruft, die die Größe nicht mehr ändern sollen, bevor
# man Kinder reinpackt. Meine Lösung wäre ein linkes und rechtes Frame wenn es eh zweigeteilt sein soll
root_frame = CTkFrame(app, width=480, height=320)
root_frame.pack(fill="both", expand="True")

# Wir machen zwei Frames, wenn die sowieso genau die Hälfte haben sollen
left_frame = CTkFrame(root_frame, fg_color="#1abc9c")
right_frame = CTkFrame(root_frame, fg_color="#34495e")

left_frame.pack(side="left", fill="both", expand="True")
right_frame.pack(side="right", fill="both", expand="True") # ich glaube side ist hier eigentlich egal, haben eh nur zwei

# Wenn ich pack_propagate richtig verstehe, dann wollen wir linke und rechte Seite nicht mehr ändern, egal was wir an Kindern reinpacken
# https://stackoverflow.com/questions/9996599/tkinters-pack-propagate-method
left_frame.pack_propagate(False)
right_frame.pack_propagate(False)

CTkLabel(right_frame, text="Rechte Seite").pack(padx=20, pady=20)

# Ok ab hier kommt dein ganzer content rein
sl_label = CTkLabel(left_frame, text="Einkaufsliste", font=("Arial", 20), corner_radius=32, fg_color="#16a085", text_color="black")
sl_label.pack(padx=10, fill="x", pady=3)

sl_content_scrollframe = CTkScrollableFrame(left_frame, fg_color="#ecf0f1")
sl_content_scrollframe.pack(padx=5, pady=5, fill="both", expand=True)

for i in range(20):
    CTkLabel(sl_content_scrollframe, text=f"Item {i+1}", text_color="black").pack(anchor="w", padx=10, pady=2, fill="x")

# der footer mit vier spalten, die alle gleich groß sind
sl_footer = CTkFrame(left_frame, fg_color="transparent")
sl_footer.grid_columnconfigure((0, 1, 2, 3), weight=1)
sl_footer.pack(side="bottom", fill="x", pady=(0, 5), padx=5)

# und die vier buttons
sl_mail = CTkButton(sl_footer, text="Mail", height=30, corner_radius=8, fg_color="#27ae60", text_color="black")
sl_mail.grid(row=0, column=0, padx=(0, 5), pady=5, sticky="ew")

sl_print = CTkButton(sl_footer, text="Print", height=30, corner_radius=8, fg_color="#27ae60", text_color="black")
sl_print.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

sl_clear = CTkButton(sl_footer, text="Clear", height=30, corner_radius=8, fg_color="#27ae60", text_color="black")
sl_clear.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

sl_change = CTkButton(sl_footer, text="\u270E", height=30, corner_radius=8, fg_color="#27ae60", text_color="black")
sl_change.grid(row=0, column=3, padx=(5, 0), pady=5, sticky="ew")


app.mainloop()
