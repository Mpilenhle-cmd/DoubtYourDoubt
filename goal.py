import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_player import st_player
import datetime
#import cv2

from db_function import  *

def main():


    # Creating sidebar with selection box -
    # you can create multiple pages this way
    options = ["Personal Development", "Career", 'Business', "Family", "Health", 'Relationship', 'Spirituality']
    selection = st.sidebar.selectbox("Choose Option", options)

    create_table_personal_development()
    create_table_career()
    create_table_business()
    create_table_family()
    create_table_health()
    create_table_relationship()
    create_table_spiritual()

    # Building out the "Information" page
    if selection == "Personal Development":
        st.title('The Rich And The Poor Have 24 Hours A Day')
        # Embed a youtube video
        #@st.cache
        st_player("https://www.youtube.com/watch?v=mmU56vZs72A")

        # Embed a music from SoundCloud
        #st_player("https://soundcloud.com/imaginedragons/demons")
        
        # Task options
        person_task_ops = ["Create", "Read", 'Update', "Delete", "About"]
        selection1 = st.sidebar.selectbox("Choose Option", person_task_ops)
        
        if selection1 == 'Create':

            st.subheader("Personal development")
            st.info("Insights on the topic")
            # You can read a markdown file from supporting resources folder
            st.markdown("No one knows how much they can take, how much they can work, just how much "
                        "we could actually have, but most importantly, "
                        "what we could become. Jim Rohn favourite quote on Business is `"
                        "Happiness is not contained in what you get, happiness is contained in what "
                        "you become`")

            col1, col2 = st.columns(2)

            with col1:
                task = st.text_area("Task To Do", 'Practice speaking everyday for 3 months')
                reason = st.text_area("Why do you thing this task is important, what are you going to benefit?", "I want to be the best positive speaker of our time")
                impact = st.text_area("What will you loose not making this task a priority?", 'I could live my life with no one knowing of my impact')
                
                #st.success('Alarm is set for', t)

            with col2:
                task_status = st.selectbox("Status", ['To Do', 'Doing', 'Done'])
                task_start_date = st.date_input('Start Date')
                task_due_date = st.date_input('Due Date')
                time = str(st.time_input('Set an alarm for', datetime.time(8, 45)))
            
            if st.button("Add Task"):
                add_task_personal_development(task,reason, impact, task_status, task_start_date, task_due_date, time)
                st.success("Successfully added task: {}".format(task))
                
        elif selection1 == 'Read':
            st.write('Personal Development tasks')
            personal_results = view_all_data_personal()
            with st.expander('View All Tasks'):
                personal_df = pd.DataFrame(personal_results, columns= ['Task', 'Reason', 'Impact', 'Status', 'Start Date', 'Due Date', 'Time'])
                st.write(personal_df)
            
        elif selection1 == 'Update':
            
            st.write('Updating')
            
        elif selection1 == 'Delete':
            st.write("Deleting")
            
        else:
            st.write('About')

    elif selection == "Career":
        career_task_ops = ["Create", "Read", 'Update', "Delete", "About"]
        selection2 = st.sidebar.selectbox("Choose Option", career_task_ops)
        
        if selection2 == "Create":
            st_player("https://www.youtube.com/watch?v=q1OUyeM4oU4")
            

            st.subheader("Career")
            st.info("Insights on the topic")
            # You can read a markdown file from supporting resources folder
            st.markdown("Work is your life, whatever you do make sure you do it with all your might,"
                        " make sure you do it with all your strength. but make sure "
                        "what you do is what you love, it is connected to the dreams you have, `work is part "
                        "of your life, when you play, play. when you work, work. just Do not play at work.`")

            col1, col2 = st.columns(2)

            with col1:
                task = st.text_area("Task To Do")
                task_start_date = st.date_input('Start Date')

            with col2:
                task_status = st.selectbox("Status", ['To Do', 'Doing', 'Done'])
                task_due_date = st.date_input('Due Date')
                
            if st.button("Add Task"):
                add_task_career(task,task_status, task_start_date, task_due_date)
                st.success("Successfully added task: {}".format(task))
                
        elif selection2 == 'Read':
            
            st.write('Personal Career tasks')
            career_results = view_all_data_health()
            with st.expander('View All Tasks'):
                career_df = pd.DataFrame(career_results, columns= ['Task', 'Status', 'Start Date', 'Due Date'])
                st.write(career_df)
            
        elif selection2 == 'Update':
            
            st.write('Updating')
            
        elif selection2 == 'Delete':
            st.write("Deleting")
            
        else:
            st.write('About')

    elif selection == "Health":
        health_task_ops = ["Create", "Read", 'Update', "Delete", "About"]
        selection3 = st.sidebar.selectbox("Choose Option", health_task_ops)
        
        if selection3 == 'Create':
            st_player("https://www.youtube.com/watch?v=fEL83JZ4hnE")
            

            st.subheader("Health")
            st.info("Insights on the topic")
            # You can read a markdown file from supporting resources folder
            st.markdown("All of this work and focus needs a healthy mind and a healthy body, "
                        "make sure you take care of your self. Sometimes the spirit is willing but the body is not. "
                        " most powerful quotes in a scripture is "
                        "`Treat your body like a temple`")

            col1, col2 = st.columns(2)

            with col1:
                task = st.text_area("Task To Do")
                task_start_date = st.date_input('Start Date')

            with col2:
                task_status = st.selectbox("Status", ['To Do', 'Doing', 'Done'])
                task_due_date = st.date_input('Due Date')
                
            if st.button("Add Task"):
                add_task_health(task,task_status, task_start_date, task_due_date)
                st.success("Successfully added task: {}".format(task))
                
        elif selection3 == 'Read':
            
            st.write('Personal Health tasks')
            health_results = view_all_data_health()
            with st.expander('View All Tasks'):
                health_df = pd.DataFrame(health_results, columns= ['Task', 'Status', 'Start Date', 'Due Date'])
                st.write(health_df)
            
        elif selection3 == 'Update':
            
            st.write('Updating')
            
        elif selection3 == 'Delete':
            st.write("Deleting")
            
        else:
            st.write('About')


    elif selection == "Business":
        buss_task_ops = ["Create", "Read", 'Update', "Delete", "About"]
        selection4 = st.sidebar.selectbox("Choose Option", buss_task_ops)
        
        if selection4 == 'Create':
            st_player("https://www.youtube.com/watch?v=2nTIdTLAc1A")

            st.subheader("Business")
            st.info("Insights on the topic")
            # You can read a markdown file from supporting resources folder
            st.markdown("To have a fulfillment about your life is when you are able to do what you love"
                        " doing, such that it does not feel like work anymore, Jim Rohn favourite quote on Business is `"
                        "Work part time on you business when working full time on your career`")

            col1, col2 = st.columns(2)

            with col1:
                task = st.text_area("Task To Do")
                task_start_date = st.date_input('Start Date')

            with col2:
                task_status = st.selectbox("Status", ['To Do', 'Doing', 'Done'])
                task_due_date = st.date_input('Due Date')
                
            if st.button("Add Task"):
                add_task_business(task,task_status, task_start_date, task_due_date)
                st.success("Successfully added task: {}".format(task))
                
        elif selection4 == 'Read':
            
            st.write('Personal Business tasks')
            business_results = view_all_data_business()
            with st.expander('View All Tasks'):
                business_df = pd.DataFrame(business_results, columns= ['Task', 'Status', 'Start Date', 'Due Date'])
                st.write(business_df)
            
        elif selection4 == 'Update':
            
            st.write('Updating')
            
        elif selection4 == 'Delete':
            st.write("Deleting")
            
        else:
            st.write('About')

    elif selection == "Family":
        fam_task_ops = ["Create", "Read", 'Update', "Delete", "About"]
        selection5 = st.sidebar.selectbox("Choose Option", fam_task_ops)
        
        if selection5 == 'Create':
            st_player("https://www.youtube.com/watch?v=zcU1NHbrLRk&t=7s")
            

            st.subheader("Family")
            st.info("Insights on the topic")
            # You can read a markdown file from supporting resources folder
            st.markdown("Family is one of the most important things in our life, it is one of the biggest reason of "
                        "beings. it is also a reason behind the way we choose to make our live, to the things we choose"
                        " to have and believe. and one of Claus Michaelson's quote is `Family"
                " is much more than blood`")

            col1, col2 = st.columns(2)

            with col1:
                task = st.text_area("Task To Do")
                task_start_date = st.date_input('Start Date')

            with col2:
                task_status = st.selectbox("Status", ['To Do', 'Doing', 'Done'])
                task_due_date = st.date_input('Due Date')
            
            if st.button("Add Task"):
                add_task_family(task,task_status, task_start_date, task_due_date)
                st.success("Successfully added task: {}".format(task))
        
                
        elif selection5 == 'Read':
            
            st.write('Personal Family tasks')
            family_results = view_all_data_family()
            with st.expander('View All Tasks'):
                family_df = pd.DataFrame(family_results, columns= ['Task', 'Status', 'Start Date', 'Due Date'])
                st.write(family_df)
                
                
            with st.expander('Task Status'):
                fam_df = family_df['status'].value_counts()
                fam_df = fam_df.reset_index()
                st.write(fam_df)
                
                p1 = px.pie
            
        elif selection5 == 'Update':
            
            st.write('Updating')
            
        elif selection5 == 'Delete':
            st.write("Deleting")
            
        else:
            st.write('About')
            
            
    
    elif selection == 'Spirituality':
        spirit_task_ops = ["Create", "Read", 'Update', "Delete", "About"]
        selection6 = st.sidebar.selectbox("Choose Option", spirit_task_ops)
        
        if selection6 == 'Create':
            st_player("https://www.youtube.com/watch?v=zVdDR0N8UGU")

            st.subheader('Spirituality')
            st.info("Insights on the topic")
            # You can read a markdown file from supporting resources folder
            st.markdown("Family is one of the most important things in our life, it is one of the biggest reason of "
                        "beings. it is also a reason behind the way we choose to make our live, to the things we choose"
                        " to have and believe. and one of Claus Michaelson's quote is `Family"
                " is much more than blood`")

            col1, col2 = st.columns(2)

            with col1:
                task = st.text_area("Task To Do")
                task_start_date = st.date_input('Start Date')

            with col2:
                task_status = st.selectbox("Status", ['To Do', 'Doing', 'Done'])
                task_due_date = st.date_input('Due Date')
            
            if st.button("Add Task"):
                add_task_spiritual(task,task_status, task_start_date, task_due_date)
                st.success("Successfully added task: {}".format(task))
                
        elif selection6 == 'Read':
            
            st.write('Personal Spiritual tasks')
            spiritual_results = view_all_data_spiritual()
            with st.expander('View All Tasks'):
                spiritual_df = pd.DataFrame(spiritual_results, columns= ['Task', 'Status', 'Start Date', 'Due Date'])
                st.write(spiritual_df)
            
        elif selection6 == 'Update':
            
            st.write('Updating')
            
        elif selection6 == 'Delete':
            st.write("Deleting")
            
        else:
            st.write('About')

    else:
        realations_task_ops = ["Create", "Read", 'Update', "Delete", "About"]
        selection7 = st.sidebar.selectbox("Choose Option", realations_task_ops)
        
        if selection7 == 'Create':
            st_player("https://www.youtube.com/watch?v=AAwKrLf9ljQ")
            

            st.subheader("Relationships")
            st.info("Insights on the topic")
            # You can read a markdown file from supporting resources folder
            st.markdown("The people we have around us pour so much influence in our minds, from what we think about,"
                        "what we talk about, and the philosophies we develop about life, influences us all. In life"
                        " it is as simple as walking with someone it is either you adjust to their pace or they"
                        "adjust to your pace, ask your self whose pace have I adjusted to ?`"
                        " show me your friends and I will tell you your future.`")

            col1, col2 = st.columns(2)

            with col1:
                task = st.text_area("Task To Do")
                task_start_date = st.date_input('Start Date')


            with col2:
                task_status = st.selectbox("Status", ['To Do', 'Doing', 'Done'])
                task_due_date = st.date_input('Due Date')

            
            if st.button("Add Task"):
                add_task_relationship(task,task_status, task_start_date, task_due_date)
                st.success("Successfully added task: {}".format(task))
                
        elif selection7 == 'Read':
            
            st.write('Personal Relationship tasks')
            relationship_results = view_all_data_relationship()
            with st.expander('View All Tasks'):
                relationship_df = pd.DataFrame(relationship_results, columns= ['Task', 'Status', 'Start Date', 'Due Date'])
                st.write(relationship_df)
            
        elif selection7 == 'Update':
            
            st.write('Updating')
            
        elif selection7 == 'Delete':
            st.write("Deleting")
            
        else:
            st.write('About')


if __name__ == '__main__':
    main()