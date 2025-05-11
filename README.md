# Dawai Finder
Welcome to the Dawai Finder Dashboard! This is a web app designed for managing and searching medicinal products in a local medical store. With an intuitive interface, you can easily add, update, delete, and search for medicines in your store's database.

# Features
Search for Medicine: Quickly search for any medicine by name.

Urgent Medicines: Display urgent medicine requirements such as Paracetamol and Cetirizine.

Add New Medicine: Add new medicines to the store’s inventory with relevant details (name, price, uses, stock, and availability).

Update Medicine: Update the price, uses, or availability of existing medicines.

Delete Medicine: Remove unwanted medicines from the inventory.

Stock Visualization: View a bar chart of the current stock levels for medicines.

Show All Medicines: Display all available medicines in the store’s database.

# Prerequisites
Python 3.13 or later

Streamlit

JSON handling libraries

Installation
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/dawai-finder.git
cd dawai-finder
# Create a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run ui.py
Open your browser and go to the address shown (usually http://localhost:8501).

# Usage
Upon running the app, you'll be presented with a sidebar for navigation.

You can choose between the following actions:

Search Medicine: Search for any medicine by name.

Urgent Medicines: Check the availability of urgent medicines.

Add Medicine: Add a new medicine to the inventory.

Update Medicine: Modify the details of an existing medicine.

Delete Medicine: Remove a medicine from the inventory.

Show All Medicines: View all medicines currently stored in the database.

# File Structure
ui.py: Main Streamlit app file for UI and app flow.

dawai.py: Contains the Dawai class for medicine data, methods for adding and displaying information.

information.py: Manages the database (loading, saving, updating, and deleting medicine records).

json_handler.py: Handles loading and saving of medicine data in the JSON file format.

# Technology Stack
Python (3.13+)

Streamlit: For the user interface.

JSON: For storing and retrieving data.

Object-Oriented Programming (OOP): Used for defining the Dawai class and organizing methods.

# Future Enhancements
Add features like medicine expiration date tracking.

Implement more advanced stock management features.

Add a user authentication system for accessing the dashboard.
