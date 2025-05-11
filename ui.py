import streamlit as st
from information import DawaiInformation
from dawai import Dawai
from json_handler import load_medicines_from_json, save_medicines_to_json

# Initialize the database
db = DawaiInformation()

# Load initial medicines from the JSON file
db.dawayan = load_medicines_from_json()

#Function for stock visualization using Streamlit's built-in chart
def plot_stock_data():
    medicines = load_medicines_from_json()
    if medicines:
        stock_data = {med.name: med.stock for med in medicines}
        st.bar_chart(stock_data)
    else:
        st.info("No medicine data available for graph.")

# Title of the app
st.title("🩺 Dawai Finder Dashboard")

# Sidebar for navigation
st.sidebar.title("Dashboard For Local (Medical Store)")
menu = st.sidebar.radio("Choose an action", 
                       ("Search Medicine", 
                        "Urgent Medicines", 
                        "Add Medicine", 
                        "Update Medicine", 
                        "Delete Medicine", 
                        "Show All Medicines"))

# Search Medicine
if menu == "Search Medicine":
    st.header("Search for Medicine")
    medicine_name = st.text_input("Enter the medicine name to search")
    
    if st.button("Search"):
        med = db.find_dawayan(medicine_name)
        if med:
            st.success("✅ Medicine Found")
            st.markdown(med.display_info()) 
        else:
            st.error("❌ Medicine not found. Please add it to your dashboard.")

# Urgent Medicines
elif menu == "Urgent Medicines":
    st.header("Urgent Medicines")
    urgent_meds = ["Paracetamol", "Cetirizine"]
    for med_name in urgent_meds:
        med = db.find_dawayan(med_name)
        if med:
            st.markdown(f"🔴 **{med.name.title()}** - {med.uses} - PKR= {med.price}")
        else:
            st.error(f"❌ {med_name} not available")

# Add Medicine
elif menu == "Add Medicine":
    st.header("Add Medicine")
    name = st.text_input("Enter Medicine Name")
    price = st.number_input("Price", min_value=1, value=1)
    uses = st.text_area("Uses")
    stock = st.number_input("Stock Quantity", min_value=1, value=10)
    available = st.selectbox("Available", ["Yes", "No"])
    
    if st.button("Add Medicine"):
        available_bool = available == "Yes"
        new_med = Dawai(name, uses, price, available_bool, stock)
        if db.add_dwai(new_med):
            save_medicines_to_json(db.dawayan)
            st.success("✅ Medicine Added Successfully and Saved!")
        else:
            st.error("⚠️ Medicine already exists!")

# Update Medicine
elif menu == "Update Medicine":
    st.header("Update Medicine")
    name = st.text_input("Enter Medicine Name to Update")
    price = st.number_input("New Price", min_value=1, value=1)
    uses = st.text_area("New Uses", value="")
    available = st.selectbox("Available", ["Yes", "No", "Leave as is"])
    
    if st.button("Update Medicine"):
        available_bool = None if available == "Leave as is" else (available == "Yes")
        success = db.updated_dawayan(
            name,
            new_price=price if price > 0 else None,
            new_uses=uses if uses else None,
            new_availableity=available_bool
        )
        if success:
            st.success("✅ Medicine Updated Successfully!")
        else:
            st.error("❌ Medicine not found.")

# Delete Medicine
elif menu == "Delete Medicine":
    st.header("Delete Medicine")
    name = st.text_input("Enter Medicine Name to Delete")
    
    if st.button("Delete Medicine"):
        if db.delete_dawayan(name):
            save_medicines_to_json(db.all_dawyan())
            st.success("🗑️ Medicine Deleted!")
        else:
            st.error("❌ Medicine not found.")

# Show All Medicines
elif menu == "Show All Medicines":
    st.header("All Medicines in Database")
    all_meds = load_medicines_from_json()  # Load medicines from JSON
    if all_meds:
        for med in all_meds:
            st.write(med.display_info())  # Display each medicine's information
    else:
        st.warning("📭 No medicines found in the database.")

# Stock Visualization
st.subheader("Stock Visualization")
plot_stock_data()
