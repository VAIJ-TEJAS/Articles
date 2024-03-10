    def on_button_click(self, text):
        if text == '=':
                    try:
                        result = eval(self.entry.get())
                        self.entry.delete(0, tk.END)
                        self.entry.insert(tk.END, str(result))
                    except Exception as e:
                        messagebox.showerror("Error", "Invalid Input")
    
                elif text == 'C':
                    self.entry.delete(0, tk.END)
    
                else:
                    self.entry.insert(tk.END, text)