from customtkinter import *
tk = CTk()
tk.geometry("480x320")
tk.overrideredirect(True)
tk.configure(bg_color="#2c3e50")
set_appearance_mode("Dark")

# Top Level Frame
frame = CTkFrame(tk, width=480, height=320)

# Shopping List Frame
sl = CTkFrame(frame, width=240, height=320, fg_color="#1abc9c")

# Shopping List Header "Einkaufsliste"
sl_label = CTkLabel(sl, text="Einkaufsliste", font=("Arial", 20), corner_radius=32, fg_color="#16a085", text_color="black")
sl_label.pack(padx=10, fill="both", pady=3)

# Shopping List Content Frame
#sl_content_frame = CTkFrame(sl, fg_color="white")
#sl_content_frame.configure(width=230, corner_radius=8)
#sl_content_frame._scrollbar.configure(height=0)
#Shopping List Content Scrollable Frame
# Shopping List Content Scrollable Frame
sl_content_scrollframe = CTkScrollableFrame(sl, width=230, height=240, fg_color="#ecf0f1")
sl_content_scrollframe.pack(padx=5, pady=5)
sl_content_scrollframe.pack_propagate(False)

# Optional: to test if the scroll frame is filling correctly
for i in range(20):
    CTkLabel(sl_content_scrollframe, text=f"Item {i+1}", text_color="black").pack(anchor="w", padx=10, pady=2)





#sl_content_frame.pack()
#sl_content_frame.pack_propagate(False)

#Shopping List Footer
sl_footer = CTkFrame(sl, width=240, height=30, fg_color="#1abc9c")

sl_mail = CTkButton(sl_footer, text="Mail", width=50, height=30, corner_radius=8, fg_color="#27ae60", text_color="black")
sl_mail.pack(side="left", padx=5, pady=5)

sl_print = CTkButton(sl_footer, text="Print", width=50, height=30, corner_radius=8, fg_color="#27ae60", text_color="black")
sl_print.pack(side="left", padx=5, pady=5)

sl_clear = CTkButton(sl_footer, text="Clear", width=50, height=30, corner_radius=8, fg_color="#27ae60", text_color="black")
sl_clear.pack(side="left", padx=5, pady=5)

sl_change = CTkButton(sl_footer, text="\u270E", width=50, height=30, corner_radius=8, fg_color="#27ae60", text_color="black")
sl_change.pack(side="left", padx=5, pady=5)

sl_footer.pack(side="bottom", fill="x")


sl.pack_propagate(False)
sl.pack(side="left", fill="both")

frame.pack_propagate(False)
frame.pack(fill="both")


tk.mainloop()