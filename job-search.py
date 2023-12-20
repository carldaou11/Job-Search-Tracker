#!/usr/bin/env python
# coding: utf-8
import csv
import os
from datetime import datetime
import tkinter as tk
from tkinter import ttk

def create_csv_file(file_path):
    header = ["Date", "Company", "Place", "Position", "Industry", "Link", "Cover letter", "Password", "Status"]
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

def add_job_application(file_path, application_data):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(application_data)

def view_job_applications(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def update_application_status(file_path, row_index, new_status):
    rows = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if 0 <= row_index < len(rows):
        rows[row_index][-1] = new_status  # Assuming 'Status' is the last column

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def submit_application():
    current_date = datetime.now().strftime('%Y-%m-%d')
    application_data = [
        current_date,
        company_entry.get(),
        place_entry.get(),
        position_entry.get(),
        industry_entry.get(),
        link_entry.get(),
        cover_letter_entry.get(),
        password_entry.get(),
        "Applied"  # Default status
    ]
    add_job_application(file_path, application_data)
    update_status_label("Application Submitted")

def update_status_label(message):
    status_label.config(text=message)

# GUI setup
file_path = 'job_applications.csv'

if not os.path.exists(file_path):
    create_csv_file(file_path)

root = tk.Tk()
root.title("Job Search Tracker")

# Labels
company_label = ttk.Label(root, text="Company:")
place_label = ttk.Label(root, text="Place:")
position_label = ttk.Label(root, text="Position:")
industry_label = ttk.Label(root, text="Industry:")
link_label = ttk.Label(root, text="Link:")
cover_letter_label = ttk.Label(root, text="Cover Letter:")
password_label = ttk.Label(root, text="Password:")

status_label = ttk.Label(root, text="")

# Entry widgets
company_entry = ttk.Entry(root)
place_entry = ttk.Entry(root)
position_entry = ttk.Entry(root)
industry_entry = ttk.Entry(root)
link_entry = ttk.Entry(root)
cover_letter_entry = ttk.Entry(root)
password_entry = ttk.Entry(root, show="*")  # Show asterisks for password entry

# Submit button
submit_button = ttk.Button(root, text="Submit Application", command=submit_application)

# Layout
company_label.grid(row=0, column=0, sticky="e")
place_label.grid(row=1, column=0, sticky="e")
position_label.grid(row=2, column=0, sticky="e")
industry_label.grid(row=3, column=0, sticky="e")
link_label.grid(row=4, column=0, sticky="e")
cover_letter_label.grid(row=5, column=0, sticky="e")
password_label.grid(row=6, column=0, sticky="e")

company_entry.grid(row=0, column=1)
place_entry.grid(row=1, column=1)
position_entry.grid(row=2, column=1)
industry_entry.grid(row=3, column=1)
link_entry.grid(row=4, column=1)
cover_letter_entry.grid(row=5, column=1)
password_entry.grid(row=6, column=1)

submit_button.grid(row=7, column=0, columnspan=2, pady=10)
status_label.grid(row=8, column=0, columnspan=2)

root.mainloop()
