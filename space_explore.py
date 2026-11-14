import streamlit as st
import pandas as pd
from datetime import date

st.title("To-Do List & Habit Tracker ✅")

page = st.sidebar.selectbox("Select Page", ["To-Do List", "Habit Tracker"])

# Initialize session state for tasks and habits
if "tasks" not in st.session_state:
    st.session_state.tasks = pd.DataFrame(columns=["Task", "Deadline", "Completed"])

if "habits" not in st.session_state:
    st.session_state.habits = pd.DataFrame(columns=["Habit", "Completed"])

if page == "To-Do List":
    st.header("To-Do List")

    # User inputs
    new_task = st.text_input("Add a new task:", key="task_input")
    deadline = st.date_input("Deadline:", min_value=date.today())

    if st.button("Add Task"):
        if new_task:
            new_row = pd.DataFrame({"Task": [new_task], "Deadline": [deadline], "Completed": ["Undone"]})
            st.session_state.tasks = pd.concat([st.session_state.tasks, new_row], ignore_index=True)
            st.session_state.pop("task_input")  # Clears the input field
            st.rerun()  # Refresh the UI

    # Display and update task list
    if not st.session_state.tasks.empty:
        updated_tasks = st.session_state.tasks.copy()
        for index, row in updated_tasks.iterrows():
            completed = st.checkbox(row["Task"], value=(row["Completed"] == "Done"), key=f"task_{index}")
            updated_tasks.loc[index, "Completed"] = "Done" if completed else "Undone"

        st.session_state.tasks = updated_tasks

        # Display the task list with numbering
        st.write("### Task List:")
        task_list = st.session_state.tasks.copy()
        task_list.index = task_list.index + 1  # Start numbering from 1
        st.table(task_list)

elif page == "Habit Tracker":
    st.header("Habit Tracker")

    new_habit = st.text_input("Add a new habit:", key="habit_input")

    if st.button("Add Habit"):
        if new_habit:
            new_row = pd.DataFrame({"Habit": [new_habit], "Completed": ["Undone"]})
            st.session_state.habits = pd.concat([st.session_state.habits, new_row], ignore_index=True)
            st.session_state.pop("habit_input")  # Clears the input field
            st.rerun()  # Refresh UI

    # Display and update habit list
    if not st.session_state.habits.empty:
        updated_habits = st.session_state.habits.copy()
        for index, row in updated_habits.iterrows():
            completed = st.checkbox(row["Habit"], value=(row["Completed"] == "Done"), key=f"habit_{index}")
            updated_habits.loc[index, "Completed"] = "Done" if completed else "Undone"

        st.session_state.habits = updated_habits

        # Display the habit list with numbering
        st.write("### Habit List:")
        habit_list = st.session_state.habits.copy()
        habit_list.index = habit_list.index + 1  # Start numbering from 1
        st.table(habit_list)
