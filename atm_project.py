# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:11:53 2024

@author: Latitude
"""
import tkinter as tk
from tkinter import Frame, PanedWindow, messagebox
from tkinter.font import Font
from atm_backend import Backend


class Frontend:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM")
        self.root.geometry("600x450")
        self.backend = Backend()
        self.custom_font = Font(family="Helvetica", size=18, weight="bold")
        self.create_splash_screen()

    def on_enter(self, e):
        e.widget['background'] = 'lightblue'

    def on_leave(self, e):
        e.widget['background'] = 'SystemButtonFace'

    def on_focus_in(self, event):
        event.widget.config(bg='lightblue')

    def on_focus_out(self, event):
        event.widget.config(bg='white')

    def create_splash_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.splash_frame = Frame(self.root, width=600, height=450, bg="lightblue")
        self.splash_frame.pack_propagate(False)
        self.splash_frame.pack()

        splash_label = tk.Label(self.splash_frame, text=" Automation Teller Machine ", borderwidth=0.5, relief="solid", font=self.custom_font)
        splash_label.pack(expand=True)

        # Schedule the splash screen to disappear after 2000 milliseconds (2 seconds)
        self.root.after(2000, self.show_main_window)

    def show_main_window(self):
        self.splash_frame.destroy()
        self.main_window_acc()

    def main_window_acc(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.mainpaned = PanedWindow(self.root, orient=tk.VERTICAL)
        self.mainpaned.pack(fill=tk.BOTH, expand=1)

        self.upperpaned = Frame(self.mainpaned, bg='lightblue', height=200)
        self.mainpaned.add(self.upperpaned)

        self.lowerpaned = Frame(self.mainpaned, height=800)
        self.mainpaned.add(self.lowerpaned)

        self.heading = tk.Label(self.upperpaned, text='Account No', font=self.custom_font)
        self.heading.pack()

        self.cardlabel = tk.Label(self.lowerpaned, text='Account No', font=("Arial", 16))
        self.cardlabel.pack(pady=20)

        self.card_entry = tk.Entry(self.lowerpaned, width=20, relief="ridge", borderwidth=2, font=("Arial", 16))
        self.card_entry.pack()
        self.card_entry.bind("<FocusIn>", self.on_focus_in)
        self.card_entry.bind("<FocusOut>", self.on_focus_out)

        self.submit = tk.Button(self.lowerpaned, text="Submit", font=("Arial", 16), relief="groove", width=10, command=self.submit_account)
        self.submit.pack(pady=20)
        self.submit.bind("<Enter>", self.on_enter)
        self.submit.bind("<Leave>", self.on_leave)
        self.root.bind('<Return>', lambda event: self.submit_account())  # Using a lambda to call the function

    def submit_account(self):
        account_no = self.card_entry.get()
        error_msg = self.backend.validate_account(account_no)
        if error_msg:
            messagebox.showinfo("Error", error_msg)
            self.card_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Success", "Account No Accepted!")
            self.mainwindow_pin()

    def mainwindow_pin(self):
        for widget in self.lowerpaned.winfo_children():
            widget.destroy()
        for widget in self.upperpaned.winfo_children():
            widget.destroy()

        self.heading = tk.Label(self.upperpaned, text='Enter PIN', font=self.custom_font)
        self.heading.pack()

        self.pinlabel = tk.Label(self.lowerpaned, text='PIN', font=("Arial", 16))
        self.pinlabel.pack(pady=20)

        self.pin_entry = tk.Entry(self.lowerpaned, show='*',relief="ridge", borderwidth=2, width=20, font=("Arial", 16), border=2)
        self.pin_entry.pack()
        self.pin_entry.bind("<FocusIn>", self.on_focus_in)
        self.pin_entry.bind("<FocusOut>", self.on_focus_out)

        self.submit = tk.Button(self.lowerpaned, text="Submit", font=("Arial", 16), relief="groove", width=10, command=self.submit_pin)
        self.submit.pack(pady=20)
        self.submit.bind("<Enter>", self.on_enter)
        self.submit.bind("<Leave>", self.on_leave)
        self.root.bind('<Return>', self.submit_pin)

    def submit_pin(self, event=None):
        pin_no = self.pin_entry.get()
        error_msg = self.backend.validate_pin(pin_no)
        if error_msg:
            messagebox.showinfo("error", error_msg)
            self.card_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Success", "Pin No Accepted!")
            self.Main_menu()

    def Main_menu(self):
        for widget in self.lowerpaned.winfo_children():
            widget.destroy()
        for widget in self.upperpaned.winfo_children():
            widget.destroy()

        self.heading = tk.Label(self.upperpaned, text='Select Option', font=self.custom_font)
        self.heading.pack()

        self.addcash = tk.Button(self.lowerpaned, text="Deposit",  relief="groove",font=("Arial", 16), width=15, command = self.deposit_cash)
        self.addcash.grid( column= 2, row = 1,pady=20, padx = 60)
        self.addcash.bind("<Enter>", self.on_enter)
        self.addcash.bind("<Leave>", self.on_leave)

        self.withdraw = tk.Button(self.lowerpaned, text="Withdraw", relief="groove",font=("Arial", 16), width=15, command = self.withdraw)
        self.withdraw.grid( column= 2, row = 2,pady=20, padx = 60)
        self.withdraw.bind("<Enter>", self.on_enter)
        self.withdraw.bind("<Leave>", self.on_leave)

        self.chack_balance = tk.Button(self.lowerpaned, text="Chack Balance",relief="groove", font=("Arial", 16), width=15,command= self.chack_balance_fn)
        self.chack_balance.grid(column=2, row=3, pady=20, padx=60)
        self.chack_balance.bind("<Enter>", self.on_enter)
        self.chack_balance.bind("<Leave>", self.on_leave)

        self.statement = tk.Button(self.lowerpaned, text="Check Statement",relief="groove", font=("Arial", 16), width=15, command=self.chech_statement)
        self.statement.grid(column= 2, row=4, pady=20, padx=60)
        self.statement.bind("<Enter>", self.on_enter)
        self.statement.bind("<Leave>", self.on_leave)

        self.acount_info = tk.Button(self.lowerpaned, text="Account Info Update",relief="groove", font=("Arial", 16), width=15, command=self.update_info_fn)
        self.acount_info.grid(column=4, row=1, pady=20, padx=30)
        self.acount_info.bind("<Enter>", self.on_enter)
        self.acount_info.bind("<Leave>", self.on_leave)

        self.transfer = tk.Button(self.lowerpaned, text=" Fund Transfer",relief="groove", font=("Arial", 16), width=15, command=self.fund_transfer_fn)
        self.transfer.grid(column=4, row=2, pady=20, padx=30)
        self.transfer.bind("<Enter>", self.on_enter)
        self.transfer.bind("<Leave>", self.on_leave)

        self.change_pin = tk.Button(self.lowerpaned, text=" Change PIN",relief="groove", font=("Arial", 16), width=15, command=self.change_pin_fn)
        self.change_pin.grid(column=4, row=3, pady=20, padx=30)
        self.change_pin.bind("<Enter>", self.on_enter)
        self.change_pin.bind("<Leave>", self.on_leave)

        self.back = tk.Button(self.lowerpaned, text=" Exit",relief="groove", font=("Arial", 16), width=15, command=self.create_splash_screen)
        self.back.grid(column=4, row=4, pady=20, padx=30)
        self.back.bind("<Enter>", self.on_enter)
        self.back.bind("<Leave>", self.on_leave)

    def deposit_cash(self):
        for widget in self.lowerpaned.winfo_children():
            widget.destroy()
        for widget in self.upperpaned.winfo_children():
            widget.destroy()

        self.heading = tk.Label(self.upperpaned, text='Deposit cash', font=self.custom_font)
        self.heading.pack()

        self.label = tk.Label(self.lowerpaned, text="Enter Money", font=("Arial", 16), )
        self.label.pack(pady=10)

        self.money = tk.Entry(self.lowerpaned, width=20, relief="ridge", borderwidth=2, font=("Arial", 16), border=2,)
        self.money.pack()
        self.money.bind("<FocusIn>", self.on_focus_in)
        self.money.bind("<FocusOut>", self.on_focus_out)

        self.withdrawmony = tk.Button(self.lowerpaned, text="Deposit cash", relief="groove", font=("Arial", 16), width=15,command=self.deposit_fn)
        self.withdrawmony.pack(pady=20)
        self.withdrawmony.bind("<Enter>", self.on_enter)
        self.withdrawmony.bind("<Leave>", self.on_leave)

        self.back = tk.Button(self.lowerpaned, text=" Exit", relief="groove", font=("Arial", 16), width=15, command=self.Main_menu)
        self.back.pack(pady=20)
        self.back.bind("<Enter>", self.on_enter)
        self.back.bind("<Leave>", self.on_leave)

    def deposit_fn(self):
        amount = float(self.money.get())
        error_msg = self.backend.validate_deposit(amount)
        if error_msg:
            messagebox.showinfo("error", error_msg)
            self.money.delete(0, tk.END)
        else:
            messagebox.showinfo("success", error_msg)
            self.Main_menu()

    def withdraw(self):
        for widget in self.lowerpaned.winfo_children():
            widget.destroy()
        for widget in self.upperpaned.winfo_children():
            widget.destroy()

        self.heading = tk.Label(self.upperpaned, text='Withdraw cash', font=self.custom_font)
        self.heading.pack()

        self.label = tk.Label(self.lowerpaned, text = "Enter Money", font = ("Arial", 16),)
        self.label.pack(pady = 10)

        self.money1 = tk.Entry(self.lowerpaned, width=20,relief="ridge", borderwidth=2, font=("Arial", 16), border=2)
        self.money1.pack()
        self.money1.bind("<FocusIn>", self.on_focus_in)
        self.money1.bind("<FocusOut>", self.on_focus_out)

        self.withdrawmony = tk.Button(self.lowerpaned, text="Withdraw cash",relief="groove", font=("Arial", 16), width=15, command=self.withdraw_fn)
        self.withdrawmony.pack(pady=20)
        self.withdrawmony.bind("<Enter>", self.on_enter)
        self.withdrawmony.bind("<Leave>", self.on_leave)
        self.back = tk.Button(self.lowerpaned, text=" Exit",relief="groove", font=("Arial", 16), width=15, command=self.Main_menu)
        self.back.pack(pady=20)
        self.back.bind("<Enter>", self.on_enter)
        self.back.bind("<Leave>", self.on_leave)

    def withdraw_fn(self):
        amount = float(self.money1.get())
        error_msg = self.backend.validate_withdraw(amount)
        if error_msg:
            messagebox.showinfo("Error", error_msg)
            self.money1.delete(0, tk.END)
        else:
            messagebox.showinfo("Success", "Withdraw success")
            self.money.delete(0, tk.END)
            self.Main_menu()

    def chack_balance_fn(self):
        for widget in self.lowerpaned.winfo_children():
            widget.destroy()
        for widget in self.upperpaned.winfo_children():
            widget.destroy()

        self.heading = tk.Label(self.upperpaned, text='Chack Balance', font=self.custom_font)
        self.heading.pack()

        tk.Label(self.lowerpaned, text = f'Balance is ${self.backend.balance}', font=("Arial", 16)).pack(pady = 20)
        print(f"Balance: {self.backend.balance}")
        self.back = tk.Button(self.lowerpaned, text="Back",relief="groove", font=("Arial", 16), width=15, command=self.Main_menu)
        self.back.pack(pady=20)

    def chech_statement(self):
        global amount
        for widget in self.lowerpaned.winfo_children():
            widget.destroy()
        for widget in self.upperpaned.winfo_children():
            widget.destroy()

        self.heading = tk.Label(self.upperpaned, text='Chech Statement', font=self.custom_font)
        self.heading.pack()

        statement = (
        f"Your recent transactions:\n"
        f"1. Deposit: ${self.backend.deposit_amount}\n"
        f"2. Withdrawal: ${self.backend.withdraw_amount}\n"
        f"3. Transferred amount: ${self.backend.transfer_amount}\n"
        f"4. Total: ${self.backend.balance}"
        )
        tk.Label(self.lowerpaned, text = statement, font=("Arial", 16), anchor="w", justify="left").pack(pady = 20)
        self.back = tk.Button(self.lowerpaned, text="Back",relief="groove", font=("Arial", 16), width=15, command=self.Main_menu)
        self.back.pack(pady=20)
        self.back.bind("<Enter>", self.on_enter)
        self.back.bind("<Leave>", self.on_leave)

    def change_pin_fn(self):
        for widget in self.lowerpaned.winfo_children():
            widget.destroy()
        for widget in self.upperpaned.winfo_children():
            widget.destroy()

        self.heading = tk.Label(self.upperpaned, text='Change PIN', font=self.custom_font)
        self.heading.pack()

        tk.Label(self.lowerpaned, text = "Old PIN", font=("Arial", 16)).pack(pady = 10)
        self.old_pin = tk.Entry(self.lowerpaned, border=2,width=20,relief="ridge", borderwidth=2, font=("Arial", 16),)
        self.old_pin.pack(pady = 10)
        self.old_pin.bind("<FocusIn>", self.on_focus_in)
        self.old_pin.bind("<FocusOut>", self.on_focus_out)

        tk.Label(self.lowerpaned, text = "New PIN", font=("Arial", 16)).pack(pady = 10)
        self.chpin = tk.Entry(self.lowerpaned, border=2,width=20,relief="ridge", borderwidth=2, font=("Arial", 16),)
        self.chpin.pack(pady = 10)
        self.chpin.bind("<FocusIn>", self.on_focus_in)
        self.chpin.bind("<FocusOut>", self.on_focus_out)

        tk.Label(self.lowerpaned, text = " Confirm New PIN", font=("Arial", 16)).pack(pady = 10)
        self.rechpin = tk.Entry(self.lowerpaned, border=2,width=20,relief="ridge", borderwidth=2, font=("Arial", 16),)
        self.rechpin.pack(pady = 10)
        self.rechpin.bind("<FocusIn>", self.on_focus_in)
        self.rechpin.bind("<FocusOut>", self.on_focus_out)
        
        self.changepin = tk.Button(self.lowerpaned, text=" Reset",relief="groove", font=("Arial", 16), width=15,command=self.change_pin)
        self.changepin.pack(pady=10)
        self.changepin.bind("<Enter>", self.on_enter)
        self.changepin.bind("<Leave>", self.on_leave)
        self.back = tk.Button(self.lowerpaned, text=" Exit",relief="groove", font=("Arial", 16), width=15, command=self.Main_menu)
        self.back.pack(pady=10)
        self.back.bind("<Enter>", self.on_enter)
        self.back.bind("<Leave>", self.on_leave)

    def change_pin(self):
        oldpin = self.old_pin.get()
        reset_pin = self.chpin.get()
        confirm_reset_pin = self.rechpin.get()
        error_msg = self.backend.validate_change_pin(oldpin, reset_pin, confirm_reset_pin)
        if error_msg:
            messagebox.showinfo("error", error_msg)
        else:
            messagebox.showinfo("Success", error_msg)
            self.Main_menu()

    def update_info_fn(self):
        for widget in self.lowerpaned.winfo_children():
            widget.destroy()
        for widget in self.upperpaned.winfo_children():
            widget.destroy()
            
        self.heading = tk.Label(self.upperpaned, text='Account Information Update', font=self.custom_font)
        self.heading.pack()
        
        self.phone_label = tk.Label(self.lowerpaned, text='Phone Number', font=("Arial", 16))
        self.phone_label.pack(pady=10)
        
        self.phone_entry = tk.Entry(self.lowerpaned, width=20,relief="ridge", borderwidth=2, font=("Arial", 16), border=2)
        self.phone_entry.pack(pady=5)
        self.phone_entry.bind("<FocusIn>", self.on_focus_in)
        self.phone_entry.bind("<FocusOut>", self.on_focus_out)
        
        self.email_label = tk.Label(self.lowerpaned, text='Email Address', font=("Arial", 16))
        self.email_label.pack(pady=10)
        
        self.email_entry = tk.Entry(self.lowerpaned, width=20,relief="ridge", borderwidth=2, font=("Arial", 16), border=2)
        self.email_entry.pack(pady=5)
        self.email_entry.bind("<FocusIn>", self.on_focus_in)
        self.email_entry.bind("<FocusOut>", self.on_focus_out)
        
        self.update_btn = tk.Button(self.lowerpaned, text="Update",relief="groove", font=("Arial", 16), width=15, command=self.update_info)
        self.update_btn.pack(pady=20)
        self.update_btn.bind("<Enter>", self.on_enter)
        self.update_btn.bind("<Leave>", self.on_leave)
        self.back = tk.Button(self.lowerpaned, text=" Exit",relief="groove", font=("Arial", 16), width=15, command=self.Main_menu)
        self.back.pack(pady=20)
        self.back.bind("<Enter>", self.on_enter)
        self.back.bind("<Leave>", self.on_leave)

    def update_info(self):
        email = self.email_entry.get()
        phone_number = self.phone_entry.get()
        error_msg = self.backend.validate_and_update_info(email, phone_number)
        if error_msg:
            messagebox.showinfo("error", error_msg)
        else:
            messagebox.showinfo("Success", "Information updated successfully!")
            self.Main_menu()
        
    def fund_transfer_fn(self):
        for widget in self.lowerpaned.winfo_children():
            widget.destroy()
        for widget in self.upperpaned.winfo_children():
            widget.destroy()
            
        self.heading = tk.Label(self.upperpaned, text='Fund Transfer', font=self.custom_font)
        self.heading.pack()
            
        self.acc_label = tk.Label(self.lowerpaned, text='Recipient Account No', font=("Arial", 16))
        self.acc_label.pack(pady=10)
        
        self.acc_entry = tk.Entry(self.lowerpaned, width=20,relief="ridge", borderwidth=2, font=("Arial", 16), border=2)
        self.acc_entry.pack(pady=5)
        self.acc_entry.bind("<FocusIn>", self.on_focus_in)
        self.acc_entry.bind("<FocusOut>", self.on_focus_out)
        
        self.amount_label = tk.Label(self.lowerpaned, text='Amount', font=("Arial", 16))
        self.amount_label.pack(pady=10)
        
        self.amount_entry = tk.Entry(self.lowerpaned, width=20,relief="ridge", borderwidth=2, font=("Arial", 16), border=2)
        self.amount_entry.pack(pady=5)
        self.amount_entry.bind("<FocusIn>", self.on_focus_in)
        self.amount_entry.bind("<FocusOut>", self.on_focus_out)
        
        self.transfer_btn = tk.Button(self.lowerpaned, text="Transfer",relief="groove", font=("Arial", 16), width=15, command=self.transfer_funds)
        self.transfer_btn.pack(pady=20)
        self.transfer_btn.bind("<Enter>", self.on_enter)
        self.transfer_btn.bind("<Leave>", self.on_leave)
        self.back = tk.Button(self.lowerpaned, text=" Exit",relief="groove", font=("Arial", 16), width=15, command=self.Main_menu)
        self.back.pack(pady=20)
        self.back.bind("<Enter>", self.on_enter)
        self.back.bind("<Leave>", self.on_leave)

    def transfer_funds(self):
        recipient_acc = self.acc_entry.get()
        amount = self.amount_entry.get()
        error_msg = self.backend.validate_and_transfer_funds(recipient_acc, amount)
        if error_msg:
            messagebox.showinfo("error", error_msg)
        else:
            messagebox.showinfo("Success", "Funds transferred successfully!")
            self.Main_menu()


if __name__ == "__main__":
    root = tk.Tk()
    app = Frontend(root)
    root.mainloop()
