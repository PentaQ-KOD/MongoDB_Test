import streamlit as st
from pymongo import MongoClient

mongo_uri = "mongodb+srv://inpantawat22:!087616436464Mongodb@cluster0.8uisl.mongodb.net/"
client = MongoClient(mongo_uri)

db = client['organization_database']
collection = db['jobs']

st.title("MongoDB CRUD Operations with Streamlit")

st.header("Create Job")
create_title = st.text_input("Job Title", key="create_title")
create_company = st.text_input("Company", key="create_company")
create_location = st.text_input("Location", key="create_location")
create_salary = st.number_input("Salary", min_value=0.0, key="create_salary", format="%.2f")

if st.button("Create Job"):
    job = {
        "title": create_title,
        "company": create_company,
        "location": create_location,
        "salary": create_salary,
    }
    result = collection.insert_one(job)
    st.success(f"Job created with id: {result.inserted_id}")

# READ
st.header("Read Jobs")
if st.button("Read Jobs"):
    jobs = collection.find()
    for job in jobs:
        st.write(job)

#update
st.header("Update Job")
update_title = st.text_input("Title of the job to update", key="update_title")
new_company = st.text_input("New Company", key="new_company")
new_location = st.text_input("New Location", key="new_location")
new_salary = st.number_input("New Salary", min_value=0.0, key="new_salary", format="%.2f")

# Delete
st.header("Delete Job")
delete_title = st.text_input("Title of the job to delete", key="delete_title")
if st.button("Delete Job"):
    query= {"title": delete_title}
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        st.success(f"Deleted {result.deleted_count} document(s)")
    else:
        st.warning("No matching document found")

#Close the connection when done
client.close()
