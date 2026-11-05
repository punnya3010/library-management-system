import streamlit as st
import pandas as pd

from database import (
    load_data,
    add_book,
    add_member
)

st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Library Management System")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Add Books",
        "View Books",
        "Register Members",
        "View Members"
    ]
)

data = load_data()

if menu == "Dashboard":

    st.header("Library Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Books", sum(
        b["quantity"] for b in data["books"]
    ))

    col2.metric("Total Members", len(data["members"]))

    col3.metric(
        "Books Issued",
        sum(
            1 for t in data["transactions"]
            if t["status"] == "Issued"
        )
    )

elif menu == "Add Books":

    st.header("Add New Book")

    with st.form("book_form"):

        title = st.text_input("Book Title")
        author = st.text_input("Author")
        category = st.text_input("Category")
        quantity = st.number_input(
            "Quantity", min_value=1, step=1
        )

        submit = st.form_submit_button("Add Book")

        if submit:
            if title.strip() and author.strip():
                add_book(
                    title,
                    author,
                    category,
                    int(quantity)
                )

                st.success("Book added successfully!")
            else:
                st.error("Enter book title and author.")

elif menu == "View Books":

    st.header("Available Books")

    if data["books"]:
        st.dataframe(
            pd.DataFrame(data["books"]),
            use_container_width=True
        )
    else:
        st.info("No books available.")

elif menu == "Register Members":

    st.header("Register New Member")

    with st.form("member_form"):

        name = st.text_input("Member Name")
        email = st.text_input("Email")

        submit = st.form_submit_button("Register")

        if submit:
            if name.strip():
                add_member(name, email)
                st.success("Member registered successfully!")
            else:
                st.error("Enter member name.")

elif menu == "View Members":

    st.header("Registered Members")

    if data["members"]:
        st.dataframe(
            pd.DataFrame(data["members"]),
            use_container_width=True
        )
    else:
        st.info("No members registered.")