# Job-Search-Tracker
This Python script provides a simple job search tracker with a graphical user interface using Tkinter. The application allows users to input details about job applications, such as the company name, position, and application status. The data is stored in a CSV file, and the program includes functionalities to add new job applications, view existing ones, and update application status. The user-friendly GUI makes it easy to track and manage job search activities.
# Function Definitions
 1. create_csv_file(file_path): Creates a CSV file with a predefined header if it doesn't exist.
 2. add_job_application(file_path, application_data): Appends a new row with job application data to the CSV file.
 3. view_job_applications(file_path): Reads and prints all rows from the CSV file.
 4. update_application_status(file_path, row_index, new_status): Updates the status of a job application at the specified row index in the CSV file.
 5. submit_application(): Gets data from GUI input fields, adds a new job application to the CSV file, and updates the status label.
 6. update_status_label(message): Updates the text of the status label in the GUI.
