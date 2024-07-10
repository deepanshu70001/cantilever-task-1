import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = self.load_contacts()

        # Create GUI components
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(row=2, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=3, column=1)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=3, column=2)

        self.contacts_listbox = tk.Listbox(root, width=40)
        self.contacts_listbox.grid(row=4, column=0, columnspan=3)

        self.update_contacts_list()

    def load_contacts(self):
        try:
            with open("contacts.txt", "r") as f:
                contacts = [line.strip() for line in f.readlines()]
            return contacts
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open("contacts.txt", "w") as f:
            for contact in self.contacts:
                f.write(contact + "\n")

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone and email:
            contact = f"{name} - {phone} - {email}"
            self.contacts.append(contact)
            self.save_contacts()
            self.update_contacts_list()
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            if name and phone and email:
                contact = f"{name} - {phone} - {email}"
                self.contacts[selected_index] = contact
                self.save_contacts()
                self.update_contacts_list()
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please fill in all fields")
        else:
            messagebox.showerror("Error", "Please select a contact to update")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            self.contacts.pop(selected_index)
            self.save_contacts()
            self.update_contacts_list()
        else:
            messagebox.showerror("Error", "Please select a contact to delete")

    def update_contacts_list(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, contact)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()