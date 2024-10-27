# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:06:46 2024

@author: Latitude
"""


class Backend:
    def __init__(self):
        self.balance = 10000.0
        self.withdraw_amount = 0.0
        self.deposit_amount = 0.0
        self.transfer_amount = 0.0
        self.pin_no = '1111'
        self.account_no = '1234567890'  
        self.countdown_id = None
        self.email = None
        self.phone_number = None

    def validate_account(self, account_no):

        if not account_no:
            return "Please fill Account Number"
        elif len(account_no) != 10 or not account_no.isdigit():
            return "Account Number must contain 10 digits."
        elif account_no != self.account_no:
            return "Wrong Account Number"
        
        return None

    def validate_pin(self, pin_no):

        if not pin_no:
            return "please fill the PIN"
        elif len(pin_no) != 4 or not pin_no.isdigit():
            return "Pin no must contain 4 digits"
        elif pin_no != self.pin_no:
            return "Worng PIN"

    def validate_deposit(self, amount):

        if amount <= 0:
            return "Deposit amount must be positive."
        
        self.balance += amount
        self.deposit_amount = amount

        return f"Deposited ${amount:.2f} successfully. New balance: ${self.balance:.2f}"

    def validate_withdraw(self, amount):

        if amount <= 0:
            return "Withdrawal amount must be positive."
        elif amount > self.balance:
            return "Insufficient funds for this withdrawal."
        elif amount > 10000:
            return "Limit of your withdrawal amount is: 10,000."
        
        self.balance -= amount
        self.withdraw_amount = amount

        return "Amount withdrawn successfully!"

    def validate_change_pin(self, oldpin, reset_pin, confirm_reset_pin):

        if oldpin != self.pin_no:
            return "Old PIN is incorrect."
        elif reset_pin != confirm_reset_pin:
            return "New PIN and Confirm PIN do not match."
        elif len(reset_pin) != 4:
            return "New PIN must be exactly 4 digits long."
        elif not reset_pin.isdigit():
            return "New PIN must contain only digits."
        else:
            self.pin_no = reset_pin  
            return "Pin changed successfully!"

    def validate_and_update_info(self, email, phone_number):
        
        if not email:
            return "Email cannot be empty."
        elif "@" not in email or "." not in email.split("@")[-1]:
            return "Invalid email format."

        if not phone_number:
            return "Phone number cannot be empty."
        elif not phone_number.isdigit() or len(phone_number) != 10:
            return "Phone number must be 10 digits long."

        self.email = email
        self.phone_number = phone_number

        return "Information updated successfully."

    

    def validate_and_transfer_funds(self, recipient_acc, amount):

        if not recipient_acc:
            return "Recipient account cannot be empty."
        elif not recipient_acc.isdigit() or len(recipient_acc) != 10:  # Example account format
            return "Invalid recipient account format."

        try:
            amount = float(amount)
            if amount <= 0:
                return "Transfer amount must be greater than zero."
        except ValueError:
            return "Please enter a valid amount."

        if amount > self.balance:
            return f"Insufficient funds. Your current balance is ${self.balance:.2f}."

        self.balance -= amount
        self.last_transfer = amount

        return f"Transferred ${amount:.2f} to account {recipient_acc} successfully. New balance: ${self.balance:.2f}"
