import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
class ClubZoneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CLUBZONE")
        self.root.geometry("800x500")
        self.root.iconbitmap(default="C:/Users/mohis/Downloads/icologo (2).ico")  # Using forward slashes
        self.root.resizable(False, False)  # Disallow resizing
        conn = sqlite3.connect("Events.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS events (event_name TEXT NOT NULL,club_name TEXT NOT NULL, event_date DATE NOT NULL)''')
        conn.close()

        # Load and place background image
        self.setup_background(r"C:\Users\mohis\Downloads\Untitled design.png")  # Using forward slashes

        # Create login frames
        self.create_login_frames()

    def setup_background(self, path):
        image = Image.open(path)
        resize_image = image.resize((800, 500))  # Adjusted size to match window size
        self.img = ImageTk.PhotoImage(resize_image)

        label1 = tk.Label(self.root, image=self.img)
        label1.place(x=0, y=0)  # Use place instead of pack

    def create_login_frames(self):
        # STUDENT
        self.student_login_frame = tk.Frame(self.root, bg='tan', bd=5)
        self.student_login_frame.place(x=100, y=100, width=280, height=230)
        tk.Label(self.student_login_frame, text="Student Login", font=("Arial", 16)).place(x=50, y=10)
        tk.Label(self.student_login_frame, text="Username:").place(x=10, y=50)
        self.student_username_entry = tk.Entry(self.student_login_frame)
        self.student_username_entry.place(x=100, y=50, width=150)
        tk.Label(self.student_login_frame, text="Password:").place(x=10, y=80)
        self.student_password_entry = tk.Entry(self.student_login_frame, show="*")
        self.student_password_entry.place(x=100, y=80, width=150)
        tk.Button(self.student_login_frame, text="student login", command=self.student_login).place(x=110, y=130)

        # COORDINATOR
        self.coordinator_login_frame = tk.Frame(self.root, bg='tan', bd=5)
        self.coordinator_login_frame.place(x=410, y=100, width=280, height=230)
        tk.Label(self.coordinator_login_frame, text="Coordinator Login", font=("Arial", 16)).place(x=50, y=10)
        tk.Label(self.coordinator_login_frame, text="Username:").place(x=10, y=50)
        self.coordinator_username_entry = tk.Entry(self.coordinator_login_frame)
        self.coordinator_username_entry.place(x=100, y=50, width=150)
        tk.Label(self.coordinator_login_frame, text="Password:").place(x=10, y=80)
        self.coordinator_password_entry = tk.Entry(self.coordinator_login_frame, show="*")
        self.coordinator_password_entry.place(x=100, y=80, width=150)
        tk.Button(self.coordinator_login_frame, text="coordinator login", command=self.coordinator_login).place(x=110, y=130)

    def student_login(self):
        username = self.student_username_entry.get()
        password = self.student_password_entry.get()
        if username and password:
            conn = sqlite3.connect("student_login.db")
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM student WHERE Username=? AND Password=?', (username, password))
            user = cursor.fetchone()
            conn.close()
            if user:
                messagebox.showinfo("Success", f"Welcome, {username}!")
                self.show_student_page()
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        else:
            messagebox.showerror("Error", "Enter both username and password.")
        

        # # Check student authentication
        # message = self.is_student_authenticated(username, password)
        # # Display result message
        # messagebox.showinfo("Login Result", message)

        # # If login successful, show student page
        # if message == "Login successful":
        #     self.show_student_page()

    def coordinator_login(self):
        username = self.coordinator_username_entry.get()
        password = self.coordinator_password_entry.get()
        if username and password:
            conn = sqlite3.connect("coordinator_login.db")
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM coordinator WHERE Username=? AND Password=?', (username, password))
            user = cursor.fetchone()
            conn.close()
            if user:
                messagebox.showinfo("Success", f"Welcome, {username}!")
                self.show_student_page()
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        else:
            messagebox.showerror("Error", "Enter both username and password.")
        self.show_coordinator_page()   

        # Check coordinator authentication
        #message = self.is_coordinator_authenticated(username, password)
        # Display result message
        #messagebox.showinfo("Login Result", message)

        # If login successful, show coordinator page
        #if message == "Login successful":
           # self.show_coordinator_page()

    """def is_student_authenticated(self, username, password):
        # Dummy authentication logic, replace with your actual logic
        if username == "student" and password == "password":
            return "Login successful"
        else:
            return "Invalid username or password"

    def is_coordinator_authenticated(self, username, password):
        # Dummy authentication logic, replace with your actual logic
        if username == "coordinator" and password == "password":
            return "Login sureturn "Invalid username or password" """

    def show_student_page(self):
        # Hide login frame and show student page
        self.student_login_frame.place_forget()
        # Create and place the student page frame
        self.student_page_frame = tk.Frame(self.root, bd=5)
        self.student_page_frame.place(x=100, y=100, width=600, height=300)
        button_font = ("Arial", 13) 

        # Load the image
        image = Image.open(r"C:\Users\mohis\Desktop\picture_culbzone\Screenshot 2024-03-02 215317.png")
        resize_image = image.resize((600, 300))  # Adjust size to match frame size
        self.img_student = ImageTk.PhotoImage(resize_image)

        # Create a label with the image
        label = tk.Label(self.student_page_frame, image=self.img_student)
        label.place(relx=0.5, rely=0.5, anchor="center")

        # Add other widgets like labels, buttons, etc.
        tk.Label(self.student_page_frame, text="Welcome Student!", font=("Arial", 16)).place(relx=0.5, rely=0.1, anchor="center")
        tk.Label(self.student_page_frame, text="Select Club:", font=("Arial", 12)).place(relx=0.5, rely=0.35, anchor="center")
        clubs = ["Rythamic thunders", "Style and slay", "Happy Club", "Mathelets club", "Empathy club", "Tekne club", "Spalsh out club", "photography culb", "Singing culb ", "Rock me Fab club"]
        self.club_selection = ttk.Combobox(self.student_page_frame, values=clubs)
        self.club_selection.place(relx=0.5, rely=0.5, anchor="center")
        tk.Button(self.student_page_frame, text="Submit", command=self.open_club_page, font=button_font).place(relx=0.5, rely=0.65, anchor="center")
        tk.Button(self.student_page_frame, text="Events", command=self.open_events_page, font=button_font).place(relx=0.5, rely=0.8, anchor="center")
        tk.Button(self.student_page_frame, text="Back", command=self.create_login_frames, font=button_font).place(relx=0.95, rely=0.95, anchor="se")  # Adjusted rely and anchor positions

    def show_coordinator_page(self):
        # Hide login frame and show coordinator page
        self.coordinator_login_frame.place_forget()
        # Create and place the coordinator page frame
        self.coordinator_page_frame = tk.Frame(self.root, bd=5)
        self.coordinator_page_frame.place(x=100, y=100, width=600, height=300)

        # Load and resize the background image
        background_image = Image.open(r"C:\Users\mohis\Desktop\picture_culbzone\Screenshot 2024-03-02 215317.png")
        resized_background = background_image.resize((600, 300))
        self.background_img = ImageTk.PhotoImage(resized_background)

        # Create a label with the background image
        background_label = tk.Label(self.coordinator_page_frame, image=self.background_img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Expand to cover the entire frame

        # Add heading
        tk.Label(self.coordinator_page_frame, text="Event Handling", font=("Arial", 20, "bold")).place(relx=0.5, rely=0.1, anchor="center")
        button_font = ("Arial", 13) 
        # Add labels and entry fields
        tk.Label(self.coordinator_page_frame, text="Event Name:",font=button_font).place(relx=0.3, rely=0.3, anchor="center")
        self.event_name_entry = tk.Entry(self.coordinator_page_frame,font=button_font)
        self.event_name_entry.place(relx=0.7, rely=0.3, anchor="center")

        tk.Label(self.coordinator_page_frame, text="Club Name:",font=button_font).place(relx=0.3, rely=0.45, anchor="center")
        self.club_name_entry = tk.Entry(self.coordinator_page_frame,font=button_font)
        self.club_name_entry.place(relx=0.7, rely=0.45, anchor="center")

        tk.Label(self.coordinator_page_frame, text="Event Date:",font=button_font).place(relx=0.3, rely=0.6, anchor="center")
        self.event_date_entry = tk.Entry(self.coordinator_page_frame,font=button_font)
        
        self.event_date_entry.place(relx=0.7, rely=0.6, anchor="center")
        
        # Add submit button
        submit_button = tk.Button(self.coordinator_page_frame, text="Submit",command=lambda: self.submit_event(),font=button_font)
        submit_button.place(relx=0.5, rely=0.8, anchor="center")

        # Add back button
        
        tk.Button(self.coordinator_page_frame, text="Back", command=self.create_login_frames,font=button_font).place(relx=0.95, rely=0.95, anchor="se")  # Adjusted rely and anchor positions

    def submit_event(self):
        event_name=self.event_name_entry.get()
        club_name=self.club_name_entry.get()
        event_date=self.event_date_entry.get()
        if event_name and club_name and event_date:
            conn = sqlite3.connect("Events.db")
            cursor = conn.cursor()
            cursor.execute('INSERT INTO events VALUES (?, ?, ?)', [event_name, club_name, event_date])
            conn.commit()
            conn.close()
            messagebox.showinfo("Event Submission",f"Event '{event_name}' for Club '{club_name}' on {event_date} submitted successfully!")
        else:
            messagebox.showerror("Error", "Enter all data.")

        # Your logic to handle event submission goes here
        #messagebox.showinfo("Event Submission", f"Event '{event_name}' for Club '{club_name}' on {event_date} submitted successfully!")

    def destroy_student_page(self):
        # Destroy student page frame
        if hasattr(self,'student_page_frame'):
            self.student_page_frame.destroy()
        # Reset background
        # Display login frames
        self.student_login_frame.place(x=100, y=100, width=300, height=200)
        self.coordinator_login_frame.place(x=410, y=100, width=300, height=200)

    def open_club_page(self):
        selected_club = self.club_selection.get()

        # Hide the student page frame
        self.student_page_frame.place_forget()

        # Create and place the club page frame
        self.club_page_frame = tk.Frame(self.root, bd=5, bg='white')
        self.club_page_frame.place(x=100, y=100, width=600, height=400)  # Adjusted height

        # Add club-specific content
        tk.Label(self.club_page_frame,text = "Club Description",font=("Arial",14,"bold")).place(relx=0.5,rely=0.15,anchor="center") 

        # Add club description label
        club_description = self.get_club_description(selected_club)
        description_label = tk.Label(self.club_page_frame, text=club_description, font=("Arial", 12), wraplength=550, justify='left')
        description_label.place(relx=0.5, rely=0.2, anchor="center") 
        # Adjusted rely position

        # Add coordinator details table
        coordinator_details = self.get_coordinator_details(selected_club)
        tk.Label(self.club_page_frame, text="Coordinator Details", font=("Arial", 12, "bold")).place(relx=0.5, rely=0.45, anchor="center")  # Adjusted rely position
        for i, detail in enumerate(coordinator_details, start=1):
            tk.Label(self.club_page_frame, text=detail, font=("Arial", 12)).place(relx=0.5, rely=0.5 + i * 0.05, anchor="center")  # Adjusted rely position

        # Add button to close club page
        button_font = ("Arial", 13)    
        tk.Button(self.club_page_frame, text="Close", command=self.close_club_page).place(relx=0.5, rely=0.95, anchor="center")
        tk.Button(self.club_page_frame, text="Back", command=self.show_student_page,font=button_font).place(relx=0.95, rely=0.95, anchor="se")  # Adjusted rely and anchor positions

    def close_club_page(self):
        self.club_page_frame.destroy()

    """def show_events(self):
        # Hide student page frame
        self.student_page_frame.place_forget()

        # Create and place events page frame
        self.events_page_frame = tk.Frame(self.root,bg="tan", bd=5)
        self.events_page_frame.place(x=100, y=100, width=600, height=300)

        # Add events content
        tk.Label(self.events_page_frame, text="Current Events", font=("Arial", 16)).place(relx=0.5, rely=0.1, anchor="center")
        tk.Label(self.events_page_frame, text="Events for all clubs are currently: Event A, Event B, Event C.", font=("Arial", 12)).place(relx=0.5, rely=0.2, anchor="center")
        conn = sqlite3.connect("Events.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT event_name,club_name,event_date FROM events''')
        table=cursor.fetchall()
        conn.close()
        tree_frame = tk.Frame(self.root, width=500, height=200)
        tree_frame.place(x=110, y=150)
        tree = ttk.Treeview(tree_frame)
        columns = [column[0] for column in cursor.description]
        print(columns)
        tree["columns"] = columns
        for col in columns:
            tree.column(col, anchor="center",width=130)
            tree.heading(col, text=col)
        for row in table:
            tree.insert("","end",values=row)
        tree.pack()
        button_font = ("Arial",13)
        tk.Button(self.events_page_frame, text="Back", command=self.show_student_page,font=button_font).place(relx=0.95, rely=0.95, anchor="se")  # Adjusted rely and anchor positions"""
    def show_events(self):
    # Hide student page frame
        self.student_page_frame.place_forget()

    # Create and place events page frame
        self.events_page_frame = tk.Frame(self.root, bg="tan", bd=5)
        self.events_page_frame.place(x=100, y=100, width=600, height=300)

    # Add events content
        tk.Label(self.events_page_frame, text="Current Events", font=("Arial", 16)).place(relx=0.5, rely=0.1, anchor="center")
        #tk.Label(self.events_page_frame, text="Events for all clubs are currently: Event A, Event B, Event C.", font=("Arial", 12)).place(relx=0.5, rely=0.2, anchor="center")
        conn = sqlite3.connect("Events.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT event_name, club_name, event_date FROM events''') 
        table = cursor.fetchall()
        conn.close()

        tree_frame = tk.Frame(self.root, width=500, height=200)
        tree_frame.place(x=110, y=150)
        tree = ttk.Treeview(tree_frame)
        columns = [column[0] for column in cursor.description if column[0]]
         # Specify the columns directly
        tree["columns"] = columns
        for col in columns:
            tree.column(col, anchor="center", width=130)
            tree.heading(col, text=col)
        for row in table:
            tree.insert("", "end", values=row)
            tree.pack()

        button_font = ("Arial", 11)
        tk.Button(self.events_page_frame, text="Back", command=self.show_student_page, font=button_font).place(relx=0.98, rely=0.92, anchor="ne")  # Adjusted rely and anchor positions

    def open_events_page(self):
        self.show_events()

    def get_club_description(self, club):
        # Dummy club descriptions, replace with actual descriptions
        descriptions = {
            "Rythmic thunders": """Rythmic Thunders
            Rythmic thunders is a club focused on promoting music and dance.
            ,We Do Dancing events and flash mobs,It Is a place where you can learn dance and enjoy a lot and we can create a beautiful memories here.
            If you are intrested you can join us ,the contact details of coordinator are given below
""",
            "Style and slay": """Style and Slay
            Style and slay is a fashion club aimed at exploring latest trends in fashion.
            We Do Modeling and design some trendy fashions and we conduct ramp walks basing on different themes
            you can develop your fashion sense by joining here
             If you are intrested you can join us ,the contact details of coordinator are given below
""",
            "Happy Club": """Happy Club
            Happy Club is dedicated to spreading positivity and happiness among students.
            It is a psychological club of svecw,it contains so many courses realted to psychology such as anger management
            If you are intrested you can join us ,the contact details of coordinator are given below""",
            "Mathelets club": """Mathelets club
            Mathelets club is for students passionate about mathematics.
            it is a maths club of svecw,it is under the maths department,we conduct some events releated to maths,you can learn a lot from this club
            If you are intrested you can join us ,the contact details of coordinator are given below
""",
            "Empathy club": """Empathy Club
            Empathy club focuses on fostering empathy and understanding among students.
            If you are intrested you can join us ,the contact details of coordinator are given below
""",
            "Tekne club": """Tekne Club
            Tekne club is for tech enthusiasts interested in coding and technology.
            where you can gain knowldge about new emerging technologies and you  writings will be published in magazine and link with some famous IIT and NIT
             If you are intrested you can join us ,the contact details of coordinator are given below.
""",
            "Spalsh out club": """Splash out
            Spalsh out club is all about acting and creation.
            If you are intrested you can join us ,the contact details of coordinator are given below""",
            "photography culb": """Photography Club
            Photography club is for photography enthusiasts to explore and learn.
             Capture moments and express creativity through photography.
             If you are intrested you can join us ,the contact details of coordinator are given below.


""",
            "Singing culb": """Singing club
            Singing club is for students who love to sing and perform.
            it contains so many courses realted to music such as guitar,dmp,piano,violen,you will enjoy a lot
            If you are intrested you can join us ,the contact details of coordinator are given below
            """,
            "Rock me Fab club": """Rock me Fab
             Rock me Fab club is for volunteers to jam and enjoy and manage events.
              It is a organizing club of svecw,we can organize all events held in the svecw,by joining in this club you can develope your leader ship qualities and commanding skills
              If you are intrested,you can join us ,the contact details of coordinator are given below.
             """
        }
        return descriptions.get(club, "Description not available")

    def get_coordinator_details(self, club):
        # Dummy coordinator details, replace with actual details
        details = {
            "Rythamic thunders": [
                ["Coordinator 1: Rithu","Branch:  CSE","Year : 2nd year", "phn no: 923-456-7890"],
                
            ],
            "Style and slay": [
                ["Coordinator 1: Pravallika","Branch :ECE","Year :3rd Year","phn no:821-654-0987"],
                
            ],
            "Happy club": [
                
                ["Coordinator 3: Anusha","Branch : EEE", "Year : 3rd Year", "phn no :956-789-0123"],
            ],
            "Mathelets club": [
                
                ["Coordinator 3: Joyshna","Branch: CSE","year :2nd Year","phn no: 889-012-3456"],
            ],
            "Empathy club": [
               
                ["Coordinator 2: Sravanthi","Branch : ECE", "Year :3rd Year","phn no: 987-654-3210"],
                
            ],
             "Tekne club": [
                
                ["Coordinator 2: Sindhu","Branch: Mech","Year :4th Year", "phn no:954-987-0123"],
               
            ],
            "Spalsh out club": [
                ["Coordinator 1: saniyha","Branch:  CSE","Year : 2nd year", "phn no: 923-456-7890"],
                
            ],
            "photography culb": [
                ["Coordinator 1: Priya","Branch :CsE","Year :3rd Year","phn no:821-654-0987"],
                
            ],
            "Singing culb": [
                ["Coordinator 1: Gamya","Branch:  CSE","Year : 2nd year", "phn no: 923-456-7890"],
                
            ],
            "Rock me Fab club": [
               
                ["Coordinator 3: Trisha","Branch: CSE","year :2nd Year","phn no: 889-012-3456"],
            ]
        }
        return details.get(club, [])

def main():
    root = tk.Tk()
    app = ClubZoneApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()