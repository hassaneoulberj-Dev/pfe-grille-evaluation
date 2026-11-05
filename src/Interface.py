import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import customtkinter
from tkinter import Canvas, Scrollbar, Frame, VERTICAL, RIGHT, LEFT, BOTH, Y, NW , HORIZONTAL , NO , CENTER , END,PhotoImage,filedialog
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import filedialog
import pandas as pd
import mysql.connector
from tkinter import messagebox
from fpdf import FPDF
import os
import win32print
import tempfile , sys


# Set the appearance mode
ctk.set_appearance_mode("light")



root = ctk.CTk()
root.title("La Grille")
root.geometry("1200x675")
root.configure(bg='#f0f0f0')  
# Désactiver le bouton de maximisation
root.resizable(False, False)  # Désactive le redimensionnement de la fenêtre


# Function to get the path of the resource files (for PyInstaller)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



############################################################################LEFTBAR############################################################################


def left_barre(frame):
    # Use relative path to the image
    script_dir = os.path.dirname(__file__)  # Get the directory of the script
    image_path = os.path.join(script_dir, "03.png")  # Construct the full path to the image

    if os.path.exists(image_path):
        bg_image = PhotoImage(file=image_path)
        image_label = tk.Label(frame, image=bg_image)
        image_label.pack(side='top', fill='y')
        frame.image = bg_image  # Keep a reference to prevent garbage collection
    else:
        print(f"Error: The image {image_path} does not exist.")

def comment_fuctions():
 


 def create_entries(parent, num_rows, num_columns, column_titles, enseignants):
    entries = []

    # Load and configure background image
    script_dir = os.path.dirname(__file__)  # Get script directory
    image_path = os.path.join(script_dir, "0.png")

    if os.path.exists(image_path):
        bg_image = PhotoImage(file=image_path)
        image_label = tk.Label(parent, image=bg_image)
       
        image_label.image = bg_image
        
        image_label.grid(row=num_rows-1, column=1, padx=0, pady=5)
    else:
        print(f"Error: The image {image_path} does not exist.")
        return

    # Create a container for the table
    table_container = tk.Frame(parent, bg='#f0f0f0')
    table_container.grid(row=1, column=1, padx=100, pady=40)

    # Create column headers
    for index, title in enumerate(column_titles):
        label = ctk.CTkLabel(table_container, text=title, font=("Helvetica", 12, "bold"),
                             corner_radius=10, text_color="white", fg_color="#333")
        label.grid(row=0, column=index + 1, padx=10, pady=5, sticky="ew")

    # Create rows of entries
    for row in range(num_rows):
        row_entries = []
        # Add a label for the non-editable ID
        id_label = ctk.CTkLabel(table_container, text=f"ID: {enseignants[row][0]}", font=("Helvetica", 12),
                                corner_radius=10, text_color="white", fg_color="#333")
        id_label.grid(row=row + 1, column=0, padx=10, pady=5, sticky="ew")
        row_entries.append(id_label)

        # Create entries for other information
        for col in range(1, num_columns):
            entry = ctk.CTkEntry(table_container, placeholder_text=f"Nomber {column_titles[col - 1]}", corner_radius=10)
            entry.grid(row=row + 1, column=col, padx=10, pady=5, sticky="ew")
            row_entries.append(entry)
        entries.append(row_entries)

    table_container.configure(borderwidth=0, relief="groove")

    return entries


 def max_column_and_row(data):
    # Convert strings to floats and find the maximum values in each column
    max_values = [max(map(float, column)) for column in zip(*data)]
    # Find the indices of the rows that contain the maximum values
    max_rows = []
    for i, column in enumerate(zip(*data)):
        for j, value in enumerate(column):
            if float(value) == max_values[i]:
                max_rows.append(j)
                break
    return max_values, max_rows
 


 return {
        'create_entries': create_entries,
        'max_column_and_row': max_column_and_row
       
    }


############################################################################Page############################################################################



def creer_page(root):


    page = tk.Frame(root, bg='white')
    page.pack(fill='both', expand=True)


    # Use relative path to the image
    script_dir = os.path.dirname(__file__)  # Get the directory of the script
    image_path = os.path.join(script_dir, "01.png")  # Construct the full path to the image

    if os.path.exists(image_path):
        bg_image = PhotoImage(file=image_path)
        image_label = tk.Label(page, image=bg_image)
        image_label.pack(side='top', fill='y')
        page.image = bg_image  # Keep a reference to prevent garbage collection
    else:
        print(f"Error: The image {image_path} does not exist.")
    # Create a frame that will contain the rest of the widgets


    # Function to handle the "Suivant" button click
    def suivant():
        page.pack_forget()
        # Ensure that the function creer_page0 is defined somewhere in your code
        creer_page0(root)

    # Button to retrieve data
    button_suivant = ctk.CTkButton(page, text="Suivant", command=suivant, fg_color='#000000',corner_radius=0)
    button_suivant.pack()
    button_suivant.place(x=530,y=623)

    return page  # Return the created frame



############################################################################PAGE 0############################################################################



def creer_page0(root):
    


    # Create a frame that will contain the rest of the widgets
    page0 = tk.Frame(root, bg='white')
    page0.pack(fill='both', expand=True)

    # Use relative path to the image
    script_dir = os.path.dirname(__file__)  # Get the directory of the script
    image_path = os.path.join(script_dir, "02.png")  # Construct the full path to the image

    if os.path.exists(image_path):
        bg_image = PhotoImage(file=image_path)
        image_label = tk.Label(page0, image=bg_image)
        image_label.pack(side='top', fill='y')
        page0.image = bg_image  # Keep a reference to prevent garbage collection
    else:
        print(f"Error: The image {image_path} does not exist.")
   
#####################################################################################################Cette partie si pour la choise de la grade


   # Function to update the selected option for option menu 1
    def update_selected_option1(value):
      global selected_option1
      selected_option1 = value
      print(f"Selected option 1: {selected_option1}")

   # Function to update the selected option for option menu 2
    def update_selected_option2(value):
     global selected_option2
     selected_option2 = value
     print(f"Selected option 2: {selected_option2}")

    
 
    # Option menu 1
    options1 = ["MCA", "MCH", "PES"]
    option_menu1 = ctk.CTkOptionMenu(page0, values=options1, command=update_selected_option1,fg_color='#bbbbba',corner_radius=0,text_color='black')
    option_menu1.place(x=((600)), y=340)
    option_menu1.set(options1[0])  # Set the default value and trigger the command

   # Option menu 2
    options2 = ["A to B", "B to C", "C to D"]
    option_menu2 = ctk.CTkOptionMenu(page0, values=options2, command=update_selected_option2,fg_color='#bbbbba',corner_radius=0,text_color='black')
    option_menu2.place(x=600, y=370)
    option_menu2.set(options2[0])  # Set the default value and trigger the command


##########################################################################################################


# Function to handle the "Submit" button click
    def submit():
        global cursor
        # Retrieve user input for database connection
        user = user_entry.get()
        password = password_entry.get()
        database ="grille"  # Retrieve the database name

        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(host='localhost', user=user, password=password, database=database)
            cursor = conn.cursor()

            # Calculer les lignes en fonction des choix de l'utilisateur
            calculate_rows(selected_option1, selected_option2)

            # Close the cursor and the connection
            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            result_label.configure(text=f"Connection failed: {e}")
        




    user_entry = ctk.CTkEntry(page0, placeholder_text="Enter User", corner_radius=0, width=120)
    user_entry.place(x=460, y=340)

    password_entry = ctk.CTkEntry(page0, placeholder_text="Password", show="*", corner_radius=0, width=120)
    password_entry.place(x=460, y=370)




    def calculate_rows(grade, type_garde):
       global num_rows
       global enseignants
       global date_effet
     
       try:
          # Exécuter la requête SQL directement sur la base de données MySQL
          cursor.execute("SELECT COUNT(*) FROM enseignant WHERE grade = %s AND type_garde = %s", (grade, type_garde))
          num_rows = cursor.fetchone()[0]
          result_label.configure(text=f"Result: {num_rows}")
          cursor.execute("SELECT id, nom, prenom FROM enseignant WHERE grade = %s AND type_garde = %s", (grade, type_garde))
          enseignants = cursor.fetchall()
          cursor.execute("SELECT date_effet FROM enseignant WHERE grade = %s AND type_garde = %s", (grade, type_garde))
          date_effet=cursor.fetchall()
 
       except Exception as e:
        result_label.configure(text=f"Query failed: {e}")



# Button to submit choices and calculate rows
    button_submit = ctk.CTkButton(page0, text="Submit", command=submit, fg_color='#000000', corner_radius=0)
    button_submit.place(x=520, y=440)


# Créer le label pour afficher les résultats (peut être déplacé à l'endroit approprié si nécessaire)
    result_label = ctk.CTkLabel(page0, text="  Result:   ", font=("Helvetica", 28, "roman"), fg_color='#ececec', corner_radius=0, text_color='black')
    result_label.place(x=940, y=390)
 



  # Function to handle the "Suivant" button click
    def suivant():
        page0.pack_forget()
        creer_page1(root,page0)


    # Button to retrieve data
    button_suivant = ctk.CTkButton(page0, text="Suivant", command=suivant, fg_color='#000000',corner_radius=0)
    button_suivant.pack()
    button_suivant.place(x=530,y=625)

    return page0
 



############################################################################PAGE 1############################################################################



def creer_page1(root,page0):

    # Create a frame that will contain the rest of the widgets
 page1 = ctk.CTkFrame(root,fg_color='#f0f0f0')
 page1.pack(fill='both', expand=True)
 


 left_barre(page1)
 label = customtkinter.CTkLabel(page1, text='\nA1 - Production pédagogique (10 points)\n',font=("Helvetica", 20, "bold"),text_color='black') 
 label.fg = "#f0f0f0"
 label.pack()  


 # Create a canvas and scrollbar
 canvas = Canvas(page1)
 scrollbar = Scrollbar(page1, orient=VERTICAL, command=canvas.yview)
 scrollable_frame = Frame(canvas)

 # Configure the canvas
 scrollable_frame.bind(
     "<Configure>",
     lambda e: canvas.configure(
         scrollregion=canvas.bbox("all")
     )
 )
 canvas.create_window((0, 0), window=scrollable_frame, anchor=NW)
 canvas.configure(yscrollcommand=scrollbar.set) 


 # Pack the canvas and scrollbar into the window
 canvas.pack(side="left", fill="both", expand=True)
 scrollbar.pack(side="right", fill="y")





    # Function to retrieve data from all entry widgets
 def retrieve_data(entries):
        data = []

        # Flag to check if there is any empty entry
        empty_entry_found = False

        for row_entries in entries:
            row_data = []
            for entry in row_entries:
                if isinstance(entry, ctk.CTkEntry):
                    value = entry.get()
                    if value == "":  # Check if the entry is empty
                        empty_entry_found = True
                        break  # Break out of the inner loop if an empty entry is found
                    row_data.append(value)
            if empty_entry_found:
                break  # Break out of the outer loop if an empty entry is found
            data.append(row_data)

        if empty_entry_found:
            # Display error message and stop further processing
            messagebox.showerror("Erreur", "Veuillez remplir toutes les cases avant de continuer.")
            return None

        try:
            # Call the function to get the maximum of each column and the corresponding rows
            max_values, max_rows = functions['max_column_and_row'](data)
            # Print or use the max_values and max_rows as needed
            print("Maximum values of each column:", max_values)
            print("Rows containing the maximum values:", max_rows)
            calculer_somme_des_scores(max_values, data)
            return data
        except ValueError as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")
            return None


 
 # Récupère les fonctions depuis comment_fuctions
 functions = comment_fuctions()
 column_titles = ["Ouvrages", "Polycopiés d’enseignement", "Supports et procédés", "Supports NTIC"]

 entries = functions["create_entries"](scrollable_frame, num_rows, len(column_titles)+1, column_titles,enseignants) 




 def ouvrages(max_values,data):
    first_col_max = (max_values[0])
    scores=[]
    for row in data:
       score = (float(row[0]) * 4) / first_col_max
       scores.append(score)
       print(score)
    return scores

 def polycopies_denseignement(max_values, data):
    second_col_max = max_values[1]
    scores = []
    for row in data:
        score = (float(row[1]) * 3) / second_col_max
        scores.append(score)
        print(score)
    return scores

 def tous_supports_et_procedes_selectionnes(max_values, data):
    third_col_max = max_values[2]
    scores = []
    for row in data:
        score = (float(row[2]) * 2) / third_col_max
        scores.append(score)
        print(score)
    return scores

 def supports_ntic(max_values, data):
    fourth_col_max = max_values[3]
    scores = []
    for row in data:
        score = (float(row[3]) * 1) / fourth_col_max
        scores.append(score)
        print(score)
    return scores

 def calculer_somme_des_scores(max_values, data):
    scores_ouvrages = ouvrages(max_values, data)
    scores_polycopies = polycopies_denseignement(max_values, data)
    scores_tous_supports = tous_supports_et_procedes_selectionnes(max_values, data)
    scores_ntic = supports_ntic(max_values, data)

    global total_scores1
    total_scores1 = []

    for i in range(len(data)):
        total_score =scores_ouvrages[i]+scores_polycopies[i] + scores_tous_supports[i] + scores_ntic[i]
        total_scores1.append(total_score)
        print(f'Total Score for row {i+1}: {total_score}')
    return total_scores1





 
 def suivant():
    data = retrieve_data(entries)
    if data is not None:  # Proceed only if all entries are filled
       page1.pack_forget()
       creer_page2(root, page1)

# Button to retrieve data
 button_suivant = ctk.CTkButton(scrollable_frame, text="Suivant", command=suivant , fg_color='#000000',corner_radius=0)
 button_suivant.grid(row=num_rows+1, column=len(column_titles)-3, padx=2, pady=1)


 def retour():
     page1.pack_forget()
     page0.pack(fill="both", expand=1)

 button_retour = ctk.CTkButton(scrollable_frame, text="Précédent", command=retour , fg_color='#000000',corner_radius=0)
 button_retour.grid(row=num_rows+2, column=len(column_titles)-3, padx=2, pady=1)


 
 
 


 return page1



############################################################################PAGE 2############################################################################



def creer_page2(root,  page1):


  page2 = ctk.CTkFrame(root, fg_color='#f0f0f0')
  page2.pack(fill="both", expand=True)
  left_barre(page2)



  label = customtkinter.CTkLabel(page2, text='\nA2 – Encadrement pédagogique ( 20 points ):\n',font=("Helvetica", 20, "bold"),text_color='black') 
  label.fg = "#f0f0f0"
  label.pack()  
  canvas1 = Canvas(page2,bg='#f0f0f0')
  scrollbar = Scrollbar(page2, orient=VERTICAL, command=canvas1.yview)
  scrollbar2 = Scrollbar(page2, orient=HORIZONTAL , command=canvas1.xview)
  scrollable_frame1= Frame(canvas1)

 # Configure the canvas
  scrollable_frame1.bind(
     "<Configure>",
     lambda e: canvas1.configure(
         scrollregion=canvas1.bbox("all")
     )
 )
  canvas1.create_window((0, 0), window=scrollable_frame1, anchor=NW)
  canvas1.configure(yscrollcommand=scrollbar.set) 

  canvas1.configure(xscrollcommand=scrollbar2.set)

  scrollbar2.pack(side="bottom", fill="x") 


 # Pack the canvas and scrollbar into the window
  canvas1.pack(side="left", fill="both", expand=True)
  scrollbar.pack(side="right", fill="y")




   # Function to retrieve data from all entry widgets
  def retrieve_data(entries):
        data = []

        # Flag to check if there is any empty entry
        empty_entry_found = False

        for row_entries in entries:
            row_data = []
            for entry in row_entries:
                if isinstance(entry, ctk.CTkEntry):
                    value = entry.get()
                    if value == "":  # Check if the entry is empty
                        empty_entry_found = True
                        break  # Break out of the inner loop if an empty entry is found
                    row_data.append(value)
            if empty_entry_found:
                break  # Break out of the outer loop if an empty entry is found
            data.append(row_data)

        if empty_entry_found:
            # Display error message and stop further processing
            messagebox.showerror("Erreur", "Veuillez remplir toutes les cases avant de continuer.")
            return None

        try:
            # Call the function to get the maximum of each column and the corresponding rows
            max_values, max_rows = functions['max_column_and_row'](data)
            # Print or use the max_values and max_rows as needed
            print("Maximum values of each column:", max_values)
            print("Rows containing the maximum values:", max_rows)
            calculer_somme_des_scores(max_values, data)
            return data
        except ValueError as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")
            return None
        

# Définissez les titres des colonnes
  column_titles1 = ["Cours", "TD", "TP", "TT","PFE : Licence", "PFE :Master/\ncycle d’ingénieur", "Membre de jury","Stage :Master/\ncycle d’ingénieur", "Autres", "Encadrement \n de RH"]
  functions = comment_fuctions()

    # Appel de la fonction another_function avec la référence retournée
  entries1 = functions["create_entries"](scrollable_frame1, num_rows, len(column_titles1)+1, column_titles1,enseignants) 



  def calculer_somme_des_lignes(entries1):
    sommes = []  # Liste pour stocker les sommes de chaque ligne
    # Define your fixed multipliers here
    multipliers = [3, 2, 1, 1]  # Example multipliers for the 4 entries

    for row_entries in entries1:
        # Filtrer les widgets d'entrée dans la rangée
        input_entries = [entry for entry in row_entries if isinstance(entry, ctk.CTkEntry)]
        # Calculer la somme des 4 premières colonnes après multiplication
        somme = sum(float(entry.get()) * multipliers[i] for i, entry in enumerate(input_entries[:4]) if entry.get().strip())
        sommes.append(somme)  # Ajouter la somme à la liste des sommes
    print(sommes)  # Afficher la liste des sommes dans la console pour vérification

    return sommes

    
# Function to calculate normalized scores based on the maximum sum
  def Enseignement(sommes):
    if not sommes:
        return []  # Return an empty list if sommes is empty
    first_col_max = max(sommes)
    note_Enseignement = [(float(somme) * 7 / first_col_max) for somme in sommes]
    for score in note_Enseignement:
        print(score)
    return note_Enseignement  # Make sure to return the calculated scores


  def PFE_licence(max_values, data):
    fifth_col_max = max_values[4]
    scores = []

    for row in data:
       score = (float(row[4]) * 3) / fifth_col_max
       scores.append(score)
       print(score)
    return scores
    

  def PFE_Master_Cycle(max_values,data):
    sixth_col_max = max_values[5]
    scores = []
      
    for row in data:
       score = (float(row[5]) * 4) / sixth_col_max
       scores.append(score)
       print(score)
    return scores
  

  def MEMBRE_Jury(max_values,data):
    seventh_col_max = max_values[6]
    scores = []
      
    for row in data:
       score = (float(row[6]) * 1) / seventh_col_max
       scores.append(score)
       print(score)
    return scores
    

  def Stage_Master_cycle(max_values,data ):
    eighth_col_max = max_values[7]
    scores = [] 
      
    for row in data:
       score = (float(row[7]) * 3) / eighth_col_max
       scores.append(score)
       print(score)
    return scores

  def Autre(max_values,data):
    ninth_col_max = max_values[8]
    scores = []
      
    for row in data:
       score = (float(row[8]) * 1) / ninth_col_max
       scores.append(score)
       print(score)
    return scores
  

  def RH(max_values,data):
    tenth_col_max = max_values[9]
    scores = []
      
    for row in data:
       score = (float(row[9]) * 1) / tenth_col_max
       scores.append(score)
       print(score)
    return scores
  

  def calculer_somme_des_scores(max_values, data):
    sommes = calculer_somme_des_lignes(entries1)
    scores_Enseignement= Enseignement(sommes)
    scores_PFE_licence = PFE_licence(max_values, data)
    scores_PFE_Master_Cycle = PFE_Master_Cycle(max_values, data)
    scores_MEMBRE_Jury = MEMBRE_Jury(max_values, data)
    scores_Stage_Master_cycle = Stage_Master_cycle(max_values, data)
    scores_Autre = Autre(max_values, data)
    scores_RH = RH(max_values, data)
    global total_scores2
    total_scores2 = []
    for i in range(len(data)):
        total_score = (scores_Enseignement[i] + scores_PFE_licence[i] + scores_PFE_Master_Cycle[i] + 
               scores_MEMBRE_Jury[i] + scores_Stage_Master_cycle[i] + scores_Autre[i] + 
               scores_RH[i])
        total_scores2.append(total_score)
        print(f'Total Score for row {i+1}: {total_score}')
    return total_scores2








  #button Suivante 
  def suivant():
     page2.pack_forget()
     retrieve_data(entries1)
     creer_page3(root,page2)

     

     # Button to retrieve data
# Button to retrieve data
  button_suivant = ctk.CTkButton(scrollable_frame1, text="Suivant", command=suivant , fg_color='#000000',corner_radius=0)
  button_suivant.grid(row=num_rows+1, column=1, columnspan=3, padx=2, pady=1)


  def retour():
      page2.pack_forget()
      page1.pack(fill="both", expand=1)

  
  button_retour = ctk.CTkButton(scrollable_frame1, text="Précédent", command=retour , fg_color='#000000',corner_radius=0)
  button_retour.grid(row=num_rows+2, column=1, columnspan=3, padx=2, pady=1)



  return page2


 

############################################################################PAGE3############################################################################



def creer_page3(root,  page2):

  page3 = ctk.CTkFrame(root, fg_color='#f0f0f0')
  page3.pack(fill="both", expand=True)

  
  left_barre(page3)



  label = customtkinter.CTkLabel(page3, text='\n A3– Responsabilités pédagogiques et administratives ( 20 points ):\n',font=("Helvetica", 20, "bold"),text_color='black') 
  label.fg = "#f0f0f0"
  label.pack()  

    


  canvas1 = Canvas(page3)
  scrollbar = Scrollbar(page3, orient=VERTICAL, command=canvas1.yview)
  scrollbar2 = Scrollbar(page3, orient=HORIZONTAL , command=canvas1.xview) 

  scrollable_frame= Frame(canvas1)
 

 # Configure the canvas
  scrollable_frame.bind(
     "<Configure>",
     lambda e: canvas1.configure(
         scrollregion=canvas1.bbox("all")
     )
 )
  canvas1.create_window((0, 0), window=scrollable_frame, anchor=NW)

  canvas1.configure(yscrollcommand=scrollbar.set) 

  canvas1.configure(xscrollcommand=scrollbar2.set)

  scrollbar2.pack(side="bottom", fill="x") 

 # Pack the canvas and scrollbar into the window
  canvas1.pack(side="left", fill="both", expand=True)
  scrollbar.pack(side="right", fill="y")



# Function to retrieve data from all Entry widgets
  def retrieve_data(entries):
    data = []
    for row_entries in entries:
        row_data = []

        for entry in row_entries:
            if isinstance(entry, ctk.CTkEntry):
                row_data.append(entry.get())
        data.append(row_data)

    # Call the function to get the maximum of each column and the corresponding rows
    max_values, max_rows = functions['max_column_and_row'](data)
    # Print or use the max_values and max_rows as needed
    print("Maximum values of each column:", max_values)
    print("Rows containing the maximum values:", max_rows)
    calculer_somme_des_scores(max_values, data)



  column_titles1 = ["responsable \nD’un départemen", "responsable\nD’une filière", "responsable\nD’un module", "Membre du collège ","responsable:\nformation universitaire","membre:\nconseil de l’établissement", "membre:\nconseil de l’Université", "Membre:la commission\n scientifique","Membre des commissions\nd’évaluation"]
  functions = comment_fuctions()
  entries1 = functions["create_entries"](scrollable_frame, num_rows, len(column_titles1)+1, column_titles1,enseignants) 




  def Rs_département(max_values,data):
    scores = []
      
    for row in data:
       score = (float(row[0]) * 4)
       scores.append(score)
       print(score)
    return scores
  
  def Rs_filière(max_values,data):
    scores = []
          
    for row in data:
       score = (float(row[1]) * 3)
       scores.append(score)
       print(score)
    return scores

  def Rs_module(max_values,data):
    scores = []
      
    for row in data:
       score = (float(row[2]) * 1)
       scores.append(score)
       print(score)
    return scores
  
  def Membre_du_collège(max_values,data):
    scores = []
      
    for row in data:
       score = (float(row[3]) * 1)
       scores.append(score)
       print(score)
    return scores

  def Rs_formation_universitaire(max_values,data):
    scores = []
    
    for row in data:
       score = (float(row[4]) * 1)
       scores.append(score)
       print(score)
    return scores
  
  def conseil_établissement (max_values,data):
    scores = []
      
    for row in data:
       score = (float(row[5]) * 3)
       scores.append(score)
       print(score)
    return scores
  
  def conseil_Université (max_values,data):
    scores = []
      
    for row in data:
       score = (float(row[6]) * 3)
       scores.append(score)
       print(score)
    return scores

  def commission_scientifique (max_values,data):
    scores = []

    for row in data:
       score = (float(row[7]) * 3)
       scores.append(score)
       print(score)
    return scores
    
  def  commissions_évaluation(max_values,data):
    scores = []

    for row in data:
       score = (float(row[8]) * 1)
       scores.append(score)
       print(score)
    return scores

  def calculer_somme_des_scores(max_values, data):
    scores_Rs_département= Rs_département(max_values,data)
    scores_Rs_filière= Rs_filière(max_values, data)
    scores_Rs_module = Rs_module(max_values, data)
    scores_Membre_du_collège = Membre_du_collège(max_values, data)
    scores_Rs_formation_universitaire = Rs_formation_universitaire(max_values, data)
    scores_conseil_établissement = conseil_établissement(max_values, data)
    scores_conseil_Université = conseil_Université(max_values, data)
    scores_commission_scientifique = commission_scientifique(max_values, data)
    scores_commissions_évaluation = commissions_évaluation(max_values, data)
    global total_scores3
    total_scores3 = []
    for i in range(len(data)):
        total_score = (scores_Rs_département[i] + scores_Rs_filière[i] + scores_Rs_module[i] + 
               scores_Membre_du_collège[i] + scores_Rs_formation_universitaire[i] + scores_conseil_établissement[i] + 
               scores_conseil_Université[i]+scores_commission_scientifique[i]+scores_commissions_évaluation[i])
        total_scores3.append(total_score)
        print(f'Total Score for row {i+1}: {total_score}')
    return total_scores3




  
# Créez le premier tableau d'entrées avec les titres

 #button Suivante 
  def suivant():
     page3.pack_forget()
     creer_page4(root,page3)
     retrieve_data(entries1)

     # Button to retrieve data 
  
  
  button_suivant = ctk.CTkButton(scrollable_frame, text="suivant", command=suivant , fg_color='#000000',corner_radius=0)
  button_suivant.grid(row=num_rows+1, column=1, columnspan=3, padx=2, pady=1)

  def retour():
         page3.pack_forget()
         page2.pack(fill="both", expand=1)

  
  button_retour = ctk.CTkButton(scrollable_frame, text="Précédent", command=retour , fg_color='#000000',corner_radius=0)
  button_retour.grid(row=num_rows+2, column=1, columnspan=3, padx=2, pady=1)

  

  return page3



############################################################################PAGE4############################################################################



def creer_page4(root,page3):


    page4 = ctk.CTkFrame(root, fg_color='#f0f0f0')
    page4.pack(fill="both", expand=True)

    left_barre(page4)

    label = customtkinter.CTkLabel(page4, text='\nB1–Production scientifique (24 points):\n', font=("Helvetica", 20, "bold"),text_color='black') 
    label.fg = "#f0f0f0"
    label.pack()



    canvas1 = Canvas(page4)
    scrollbar = Scrollbar(page4, orient=VERTICAL, command=canvas1.yview)
    scrollbar2 = Scrollbar(page4, orient=HORIZONTAL , command=canvas1.xview)
    scrollable_frame= Frame(canvas1)
    # Configure the canvas
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas1.configure(
            scrollregion=canvas1.bbox("all")
        )
    )
    canvas1.create_window((0, 0), window=scrollable_frame, anchor=NW)
    canvas1.configure(yscrollcommand=scrollbar.set)
    canvas1.configure(xscrollcommand=scrollbar2.set)

    scrollbar2.pack(side="bottom", fill="x")
    # Pack the canvas and scrollbar into the window
    canvas1.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")



# Function to retrieve data from all Entry widgets
    def retrieve_data(entries):
     data = []

     for row_entries in entries:
         row_data = []
         for entry in row_entries:
             if isinstance(entry, ctk.CTkEntry):
                row_data.append(entry.get())
         data.append(row_data)


         # Call the function to get the maximum of each column and the corresponding rows
         max_values, max_rows = functions['max_column_and_row'](data)
         # Print or use the max_values and max_rows as needed
         print("Maximum values of each column:", max_values)
         print("Rows containing the maximum values:", max_rows)
         calculer_somme_des_scores(max_values, data)


# Example usage:    
# Assuming 'entries' is a list of lists with Entry widgets, like this:
# entries = [[entry1, entry2], [entry3, entry4], ...]
# retrieve_data(entries)
    
    column_titles1 = ["Journaux non indexés", " 0 < l’impact facteur ≤1 ","l’impact facteur >1",'Ouvrage de recherche référencés',"Communications"]

    functions = comment_fuctions()
    entries1 = functions["create_entries"](scrollable_frame, num_rows, len(column_titles1)+1, column_titles1,enseignants) 





    def calculer_somme_des_lignes(entries1):
     sommes = []  # Liste pour stocker les sommes de chaque ligne
     # Define your fixed multipliers here
     multipliers = [1.5, 3, 4.5]  # Example multipliers for the 4 entries

     for row_entries in entries1:
         input_entries = [entry for entry in row_entries if isinstance(entry, ctk.CTkEntry)]
        # Calculer la somme des 4 premières colonnes après multiplication
         somme = sum(float(entry.get()) * multipliers[i] for i, entry in enumerate(input_entries[:3]) if entry.get().strip())
         sommes.append(somme)  # Ajouter la somme à la liste des sommes
     print(sommes)  # Afficher la liste des sommes dans la console pour vérification
     
     return sommes
    

  # Function to calculate normalized scores based on the maximum sum
    def Articles_scientifiques(sommes):
      if not sommes:
         return []  # Return an empty list if sommes is empty
      first_col_max = max(sommes)
      note_Enseignement = [(float(somme) * 15 / first_col_max) for somme in sommes]

      for score in note_Enseignement:
          print(score)
      return note_Enseignement  # Make sure to return the calculated scores
    

    def Ouvrage_recherche(max_values,data):
      fourth_col_max = max_values[3]
      scores = []
       
      for row in data:
        score = (float(row[3]) * 5) / fourth_col_max
        scores.append(score)
        print(score)
      return scores


    def Communications(max_values,data):
        fifth_col_max = max_values[4]
        scores = []
        for row in data:
            score = (float(row[4]) * 4) / fifth_col_max
            scores.append(score)
            print(score)
        return scores


    def calculer_somme_des_scores(max_values, data):
      sommes = calculer_somme_des_lignes(entries1)
      scores_Articles_scientifiques= Articles_scientifiques(sommes)
      scores_Ouvrage_recherche = Ouvrage_recherche(max_values, data)
      scores_Communications = Communications(max_values, data)
      global total_scores4
      total_scores4 = []

      for i in range(len(data)):
          total_score = (scores_Articles_scientifiques[i] + scores_Ouvrage_recherche[i] + scores_Communications[i])
          total_scores4.append(total_score)
          print(f'Total Score for row {i+1}: {total_score}')
      return total_scores4 

  

 #button Suivante 
    def suivant():
     retrieve_data(entries1)
     page4.pack_forget()
     creer_page5(root,page4)


     # Button to retrieve data 
    button = ctk.CTkButton(scrollable_frame, text="Suivant", command=suivant , fg_color='#000000',corner_radius=0)
    button.grid(row=num_rows+1, column=1,  padx=2, pady=1)

    def retour():
      page4.pack_forget()
      page3.pack(fill="both", expand=1)

  
    button_retour = ctk.CTkButton(scrollable_frame, text="Précédent", command=retour , fg_color='#000000',corner_radius=0)
    button_retour.grid(row=num_rows+2, column=1, columnspan=3, padx=2, pady=1)


    return page4



############################################################################PAGE5############################################################################



def creer_page5(root,page4):
    

    page5 =ctk.CTkFrame(root, fg_color='#f0f0f0')
    page5.pack(fill="both", expand=True)

    left_barre(page5)

    label = customtkinter.CTkLabel(page5, text='\nB2– Encadrement scientifique\n', font=("Helvetica", 20, "bold"),text_color='black')
    label.fg = "#f0f0f0"
    label.pack()
    canvas1 = Canvas(page5)
    scrollbar = Scrollbar(page5, orient=VERTICAL, command=canvas1.yview)
    scrollbar2 = Scrollbar(page5, orient=HORIZONTAL , command=canvas1.xview)
    scrollable_frame= Frame(canvas1)
    # Configure the canvas
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas1.configure(
            scrollregion=canvas1.bbox("all")
        )
    )

    canvas1.create_window((0, 0), window=scrollable_frame, anchor=NW)
    canvas1.configure(yscrollcommand=scrollbar.set)
    canvas1.configure(xscrollcommand=scrollbar2.set)
    scrollbar2.pack(side="bottom", fill="x")


    # Pack the canvas and scrollbar into the window
    canvas1.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")



# Function to retrieve data from all Entry widgets
    def retrieve_data(entries):
     data = []
     for row_entries in entries:
        row_data = []
        for entry in row_entries:
            if isinstance(entry, ctk.CTkEntry):
                row_data.append(entry.get())
        data.append(row_data)
 
        # Call the function to get the maximum of each column and the corresponding rows
        max_values, max_rows = functions['max_column_and_row'](data)
        # Print or use the max_values and max_rows as needed
        print("Maximum values of each column:", max_values)
        print("Rows containing the maximum values:", max_rows)
        calculer_somme_des_scores(max_values, data)
    


    column_titles1 = ["  Encadrement   ", "Co – Encadrement ","   Rapporteur   "," Membre de jury  "]
    functions = comment_fuctions()
    entries1 = functions["create_entries"](scrollable_frame, num_rows, len(column_titles1)+1, column_titles1,enseignants) 


    def Encadrement(max_values,data):
      scores = []
      
      for row in data:
        score = (float(row[0]) * 5)
        scores.append(score)
        print(score)
      return scores


    def Co_Encadrement(max_values,data):
      scores = []
      
      for row in data:
        score = (float(row[1]) * 2)
        scores.append(score)
        print(score)
      return scores
    

    def Rapporteur(max_values,data):  
       third_col_max = max_values[2]
       scores = []
       
       for row in data:
         score = (float(row[2]) * 2) / third_col_max
         scores.append(score)
         print(score)
       return scores


    def Membre_jury(max_values,data):  
       fourth_col_max = max_values[3]
       scores = []
       
       for row in data:
         score = (float(row[3]) * 1) / fourth_col_max
         scores.append(score)
         print(score)
       return scores
    
        
    def calculer_somme_des_scores(max_values, data):
      scores_Encadrement= Encadrement(max_values, data)
      scores_Co_Encadrement = Co_Encadrement(max_values, data)
      scores_Rapporteur = Rapporteur(max_values, data)
      scores_Membre_jury = Membre_jury(max_values, data)
      global total_scores5
      total_scores5 = []

      for i in range(len(data)):
          total_score = (scores_Encadrement[i] + scores_Co_Encadrement[i] + scores_Rapporteur[i]+scores_Membre_jury[i])
          total_scores5.append(total_score)
          print(f'Total Score for row {i+1}: {total_score}')
      return total_scores5
    

 #button Suivante 
    def suivant():
     retrieve_data(entries1)
     page5.pack_forget()
     creer_page6(root,page5)


    button = ctk.CTkButton(scrollable_frame, text="Suivant", command=suivant , fg_color='#000000',corner_radius=0)
    button.grid(row=num_rows+1, column=1, columnspan=3, padx=2, pady=1)

    def retour():
        page5.pack_forget()
        page4.pack(fill="both", expand=1)

  
    button_retour = ctk.CTkButton(scrollable_frame, text="Précédent", command=retour , fg_color='#000000',corner_radius=0)
    button_retour.grid(row=num_rows+2, column=1, columnspan=3, padx=2, pady=1)




    return page5



############################################################################PAGE6############################################################################



def creer_page6(root,page5):


  page6 = ctk.CTkFrame(root, fg_color='#f0f0f0')
  page6.pack(fill="both", expand=True)

  left_barre(page6)


  label = customtkinter.CTkLabel(page6, text='\nB 3 – Responsabilité scientifique (12points)\n', font=("Helvetica", 20, "bold"),text_color='black')
  label.fg = "#f0f0f0"
  label.pack()
  canvas1 = Canvas(page6)
  scrollbar = Scrollbar(page6, orient=VERTICAL, command=canvas1.yview)
  scrollbar2 = Scrollbar(page6, orient=HORIZONTAL , command=canvas1.xview)
  scrollable_frame= Frame(canvas1)
  # Configure the canvas
  scrollable_frame.bind(
      "<Configure>",
      lambda e: canvas1.configure(
          scrollregion=canvas1.bbox("all")
       )
   )
  canvas1.create_window((0, 0), window=scrollable_frame, anchor=NW)
  canvas1.configure(yscrollcommand=scrollbar.set)
  canvas1.configure(xscrollcommand=scrollbar2.set)


  scrollbar2.pack(side="bottom", fill="x")
   # Pack the canvas and scrollbar into the window
  canvas1.pack(side="left", fill="both", expand=True)
  scrollbar.pack(side="right", fill="y")




  
# Function to retrieve data from all Entry widgets
  def retrieve_data(entries):
    data = []
    for row_entries in entries:
        row_data = []
        for entry in row_entries:
            if isinstance(entry, ctk.CTkEntry):
                row_data.append(entry.get())
        data.append(row_data)

    # Call the function to get the maximum of each column and the corresponding rows
    max_values, max_rows = functions['max_column_and_row'](data)
    # Print or use the max_values and max_rows as needed
    print("Maximum values of each column:", max_values)
    print("Rows containing the maximum values:", max_rows)
    calculer_somme_des_scores(max_values, data)



# Example usage:
# Assuming 'entries' is a list of lists with Entry widgets, like this:
# entries = [[entry1, entry2], [entry3, entry4], ...]
# retrieve_data(entries)

  column_titles1 = ["Res_Labo","Res ou\ncoordination locale ", "En tant que\nmembre", 'projet:\nResponsabilité','Projet:\n membre','Rapporteur']

  functions = comment_fuctions()
  entries1 = functions["create_entries"](scrollable_frame, num_rows, len(column_titles1)+1, column_titles1,enseignants) 

  

  def Res_Labo(data):
      scores = []
      
      for row in data:
        score = (float(row[0]) * 4)
        scores.append(score)
        print(score)
      return scores
  


  def calculer_somme_des_lignes():
     sommes = []  # Liste pour stocker les sommes de chaque ligne
     
  
     for row_entries in entries1:
        somme = float(row_entries[1].get()) *2  + float(row_entries[2].get())*1.5
        sommes.append(somme)
           
     return sommes
    
  

  def Structure_recherche(sommes):
     if not sommes:
         return []  # Return an empty list if sommes is empty
     first_col_max = max(sommes)
     note_Structure_recherche = [(float(somme) * 4 / first_col_max) for somme in sommes]
     for score in note_Structure_recherche:
         print(score)
     return note_Structure_recherche  # Make sure to return the calculated scores
    

        
  def Responsabilité_membre():
     
     sommes1 = []  
  
     for row_entries in entries1:
        somme = float(row_entries[3].get()) *2  + float(row_entries[4].get())
        sommes1.append(somme)
           
     return sommes1

  


  def Projets_contrats_recherche(sommes1):
     if not sommes1:
      return []  # Return an empty list if sommes is empty
     first_col_max = max(sommes1)
     note_Structure_recherche = [(float(somme) * 2 / first_col_max) for somme in sommes1]
     for score in note_Structure_recherche:
         print(score)
     return note_Structure_recherche  # Make sure to return the calculated scores
    


  def Activités_expertises(max_values,data):  
       fifth_col_max = max_values[5]
       scores = []
       
       for row in data:
         score = (float(row[5]) * 2) / fifth_col_max
         scores.append(score)
         print(score)
       return scores



  def calculer_somme_des_scores(max_values, data):
      sommes = calculer_somme_des_lignes()
      sommes1=Responsabilité_membre()
    
      score_Res_Labo= Res_Labo(data)
      score_Structure_recherche = Structure_recherche(sommes)
      score_Projets_contrats_recherche= Projets_contrats_recherche(sommes1)
      score_Activités_expertises= Activités_expertises(max_values,data)
      global total_scores6
      total_scores6 = []

      for i in range(len(data)):
          total_score = (score_Res_Labo[i] + score_Structure_recherche [i] +score_Projets_contrats_recherche[i]+score_Activités_expertises[i])
          total_scores6.append(total_score)
          print(f'Total Score for row {i+1}: {total_score}')
      return total_scores6




# Créez le premier tableau d'entrées avec les titres

  def suivant():
   retrieve_data(entries1)
   page6.pack_forget()
   creer_page7(root,page6)


## Button to retrieve data 
  button = ctk.CTkButton(scrollable_frame, text="Suivant", command=suivant , fg_color='#000000',corner_radius=0)
  button.grid(row=num_rows+1, column=1, columnspan=3, padx=2, pady=1)

  def retour():
      page6.pack_forget()
      page5.pack(fill="both", expand=1)

  
  button_retour = ctk.CTkButton(scrollable_frame, text="Précédent", command=retour , fg_color='#000000',corner_radius=0)
  button_retour.grid(row=num_rows+2, column=1, columnspan=3, padx=2, pady=1)
 
  return page6



############################################################################PAGE7############################################################################



def creer_page7(root,page6):

  page7 = tk.Frame(root)
  page7.pack(fill="both", expand=True)

  left_barre(page7)

  label = customtkinter.CTkLabel(page7, text='\nB4 – Innovation et Valorisation (6 points)\n', font=("Helvetica", 20, "bold"),text_color='black')
  label.fg = "#e8e4e4"
  label.pack()


  canvas1 = Canvas(page7)
  scrollbar = Scrollbar(page7, orient=VERTICAL, command=canvas1.yview)
  scrollbar2 = Scrollbar(page7, orient=HORIZONTAL , command=canvas1.xview)
  scrollable_frame= Frame(canvas1)
  # Configure the canvas
  scrollable_frame.bind(
      "<Configure>",
      lambda e: canvas1.configure(
          scrollregion=canvas1.bbox("all")
      )
  )
  canvas1.create_window((0, 0), window=scrollable_frame, anchor=NW)
  canvas1.configure(yscrollcommand=scrollbar.set)
  canvas1.configure(xscrollcommand=scrollbar2.set)

  scrollbar2.pack(side="bottom", fill="x")
  # Pack the canvas and scrollbar into the window
  canvas1.pack(side="left", fill="both", expand=True)
  scrollbar.pack(side="right", fill="y")



# Function to retrieve data from all Entry widgets
  def retrieve_data(entries):
    data = []
    for row_entries in entries:
        row_data = []
        for entry in row_entries:
            if isinstance(entry, ctk.CTkEntry):
                row_data.append(entry.get())
        data.append(row_data)
   
       # Call the function to get the maximum of each column and the corresponding rows
        max_values, max_rows = functions['max_column_and_row'](data)
        # Print or use the max_values and max_rows as needed
        print("Maximum values of each column:", max_values)
        print("Rows containing the maximum values:", max_rows)
        calculer_somme_des_scores(max_values, data)
   
  



# Example usage:
# Assuming 'entries' is a list of lists with Entry widgets, like this:
# entries = [[entry1, entry2], [entry3, entry4], ...]
# retrieve_data(entries)

  column_titles1 = ["coordination","le comité d’organisation","comité scientifique", 'Expertise\net valorisation','Dépôt de brevets']
  functions = comment_fuctions()
  entries1 = functions["create_entries"](scrollable_frame, num_rows, len(column_titles1)+1, column_titles1,enseignants) 
    



  def Organisation_manifestations(entries1):
     
     sommes = []  
  
     for row_entries in entries1:
        input_entries = [entry for entry in row_entries if isinstance(entry, ctk.CTkEntry)]
        somme = float(input_entries[0].get()) *2  + float(input_entries[1].get())+float(input_entries[2].get())
        sommes.append(somme)
           
     return sommes



  def manifestations(sommes):
      if not sommes:
       return []  # Return an empty list if sommes is empty
      first_col_max = max(sommes)
      note_manifestations = [(float(somme) * 4 / first_col_max) for somme in sommes]
      for score in note_manifestations:
         print(score)
      return note_manifestations  # Make sure to return the calculated scores
  

   
  def Expertise_valorisation(max_values,data):
     fifth_col_max = max_values[3]
     scores = []
     
     for row in data:
       score = (float(row[3]) * 1) / fifth_col_max
       scores.append(score)
       print(score)
     return scores
  

  
  def Dépôt_de_revets(data):
     scores = []
      
     for row in data:
        score = (float(row[4]) * 1)
        scores.append(score)
        print(score)
     return scores



  def calculer_somme_des_scores(max_values, data):
      sommes = Organisation_manifestations(entries1)
      
      score_manifestations =manifestations(sommes)
      score_Expertise_valorisation= Expertise_valorisation(max_values,data)
      score_Dépôt_de_brevet = Dépôt_de_revets(data)
      
      global total_scores7
      total_scores7 = []

     
      for i in range(len(data)):
          total_score = (score_Expertise_valorisation[i] +score_Dépôt_de_brevet [i] +score_manifestations[i])
          total_scores7.append(total_score)
          print(f'Total Score for row {i+1}: {total_score}')
      return total_scores7 



  def suivant():
    retrieve_data(entries1)
    page7.pack_forget()
    final_page(root,enseignants)
    

# Button to retrieve data 
  # Button to retrieve data
  button_suivant = ctk.CTkButton(scrollable_frame, text="Suivant", command=suivant , fg_color='#000000',corner_radius=0)
  button_suivant.grid(row=num_rows+1, column=1, columnspan=3, padx=2, pady=1)


  def retour():
     page7.pack_forget()
     page6.pack(fill="both", expand=1)

  button_retour = ctk.CTkButton(scrollable_frame, text="Précédent", command=retour , fg_color='#000000',corner_radius=0)
  button_retour.grid(row=num_rows+2, column=1, columnspan=3, padx=2, pady=1)



  return page7


############################################################################PAGE FINal############################################################################





def Results(enseignants, date_effet):
    total_scores8 = []

    for i in range(len(enseignants)):
        total_score = (total_scores1[i] + total_scores2[i] + total_scores3[i] +
                       total_scores4[i] + total_scores5[i] + total_scores6[i] + total_scores7[i])
        enseignant_id = enseignants[i][0]
        enseignant_nom = enseignants[i][1]
        enseignant_prenom = enseignants[i][2]

        date_effet_value = date_effet[i][0]  # Ensure correct access to date_effet

        # Append (ID, NOM, PRENOM, total_score, date_effet) tuple
        total_scores8.append((enseignant_id, enseignant_nom, enseignant_prenom, total_score, date_effet_value))
        print(f'Total {i+1}: {total_score}')

    # Sort first by total_score in descending order, then by date_effet in descending order
    total_scores8.sort(key=lambda x: (x[3], x[4]), reverse=True)

    # Extract (ID, NOM, PRENOM, total_score) tuples for the final result
    final_results = [(entry[0], entry[1], entry[2], entry[3]) for entry in total_scores8]

    return final_results


# Fonction pour générer le PDF avec une table
def generate_pdf(results, file_path):
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Classement des candidats', 0, 1, 'C')

        def chapter_title(self, title):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, title, 0, 1, 'L')
            self.ln(10)

        def chapter_body(self, body):
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 10, body)
            self.ln()

        def table(self, data):
            # Définir la largeur des colonnes
            col_widths = [20, 50, 50, 50]  # Ajustez en fonction du nombre de colonnes
            self.set_font('Arial', 'B', 12)
            for row in data:
                for idx, item in enumerate(row):
                    self.cell(col_widths[idx], 10, str(item), border=1)
                self.ln()

    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title(' ')

    # Ajouter les en-têtes de colonnes
    headers = ['ID', 'Nom', 'Prenom', ' note ']  # Ajustez en fonction de vos colonnes
    pdf.table([headers] + results)

    pdf.output(file_path)

def final_page(root, enseignants):
    page8 = customtkinter.CTkFrame(root)
    page8.pack(fill="both", expand=True)
    
    # Use relative path to the image
    script_dir = os.path.dirname(__file__)  # Get the directory of the script
    image_path = os.path.join(script_dir, "03.png")  # Construct the full path to the image

    if os.path.exists(image_path):
        bg_image = PhotoImage(file=image_path)
        image_label = tk.Label(page8, image=bg_image)
        image_label.pack(side='top', fill='y')
        page8.image = bg_image  # Keep a reference to prevent garbage collection
    else:
        print(f"Error: The image {image_path} does not exist.")

 # Create a canvas widget
    canvas = tk.Canvas(page8, bg='grey')
    canvas.pack(side='left', fill='both', expand=True)

    # Add a vertical scrollbar to the canvas
    scrollbar = ttk.Scrollbar(page8, orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a frame inside the canvas
    page8 = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=page8, anchor='nw')


    # Calculer les résultats 
    total_scores8 = Results(enseignants, date_effet)

    # Créez un style pour le Treeview
    style = ttk.Style()
    style.theme_use("clam")

    # Couleur de fond des lignes
    style.configure("Treeview", background="#D3D3D3", fieldbackground="#D3D3D3", font=('Helvetica', 15), rowheight=25)

    # Couleur de fond des en-têtes
    style.configure("Treeview.Heading", background="#2794b4", foreground="white", font=('Helvetica', 18, 'bold'))

    # Hauteur des lignes (augmente la taille de chaque ligne)
    style.configure("Treeview", rowheight=70)

    # Créez un tableau pour afficher les résultats
    results_frame = customtkinter.CTkFrame(page8)
    results_frame.pack(side='top', pady=20)

    # Utilisez un Treeview pour un affichage de type tableau
    tree = ttk.Treeview(results_frame, columns=('ID', 'NOM', 'PRENOM', 'Score total'), show='headings', height=len(total_scores8))

    # Définissez les en-têtes
    tree.heading('ID', text='ID')
    tree.heading('NOM', text='NOM')
    tree.heading('PRENOM', text='PRENOM')
    tree.heading('Score total', text='Score total')

    tree.column('ID', width=300)
    tree.column('NOM', width=300)
    tree.column('PRENOM', width=300)
    tree.column('Score total', width=300)

    # Créer un bouton pour enregistrer le PDF
    def save_pdf():
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            try:
                generate_pdf(total_scores8, file_path)
                messagebox.showinfo("Succès", f"PDF enregistré à l'emplacement : {file_path}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement du PDF : {e}")

    button_save = customtkinter.CTkButton(page8, text="Enregistrer PDF", command=save_pdf)
    button_save.pack(pady=20)


    # Créer un bouton pour imprimer le PDF directement
    def print_pdf():
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
                generate_pdf(total_scores8, tmp_pdf.name)
                tmp_pdf.close()
                printer_name = win32print.GetDefaultPrinter()
                hPrinter = win32print.OpenPrinter(printer_name)
                try:
                    with open(tmp_pdf.name, 'rb') as f:
                        pdf_data = f.read()
                    # Configuration du document à imprimer
                    doc_info = ("PDF Document", None, "RAW")
                    job_id = win32print.StartDocPrinter(hPrinter, 1, doc_info)
                    try:
                        win32print.StartPagePrinter(hPrinter)
                        win32print.WritePrinter(hPrinter, pdf_data)
                        win32print.EndPagePrinter(hPrinter)
                    finally:
                        win32print.EndDocPrinter(hPrinter)
                finally:
                    win32print.ClosePrinter(hPrinter)
                messagebox.showinfo("Succès", "PDF envoyé à l'imprimante par défaut")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'impression du PDF : {e}")

    button_print = customtkinter.CTkButton(page8, text="Imprimer PDF", command=print_pdf)
    button_print.pack(pady=20)

    # Insérez les données dans le tableau
    for id_, nom_, prenom_, score in total_scores8:
        tree.insert('', 'end', values=(id_, nom_, prenom_, score))

    tree.pack()

    return page8




creer_page(root)
root.mainloop()