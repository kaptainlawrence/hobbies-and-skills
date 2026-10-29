import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title='PathFinder | Hobby & Career Explorer', page_icon='🧭', layout='wide')
st.markdown('''<style>.block-container{max-width:1150px;padding-top:1.5rem}.hero{padding:1.5rem;border-radius:18px;background:linear-gradient(120deg,#123B5D,#2563EB,#7C3AED);color:white;margin-bottom:1rem}.hero h1{color:white}.hero p{color:#edf4ff}.card{border:1px solid #e2e8f0;padding:1rem;border-radius:14px}</style><div class="hero"><h1>🧭 PathFinder</h1><p>Explore hobbies, build useful skills, and discover career paths that interest you.</p></div>''', unsafe_allow_html=True)

HOBBIES = {
 'Technology & problem-solving': [
  ('Coding small projects',['Logical thinking','Problem-solving','Programming'],['Software Developer','Data Analyst','Cybersecurity Analyst'],'Build a calculator, quiz, or simple webpage.','2–4 hours/week'),
  ('Robotics & electronics',['Engineering thinking','Troubleshooting','Design'],['Robotics Engineer','Electrical Engineer'],'Try a beginner circuit simulator or safe electronics activity.','2–3 hours/week'),
  ('Puzzles & chess',['Planning','Pattern recognition','Decision-making'],['Data Analyst','Operations Research Analyst'],'Solve a puzzle daily and reflect on your strategy.','1–3 hours/week')],
 'Creative arts & communication': [
  ('Drawing & digital design',['Visual communication','Creativity','Attention to detail'],['Graphic Designer','UI/UX Designer','Animator'],'Create a poster for a school club or redesign an app screen.','2–4 hours/week'),
  ('Writing stories or a blog',['Writing','Research','Storytelling'],['Writer','Journalist','Content Strategist'],'Write a short article about a topic you care about.','1–3 hours/week'),
  ('Photography & video editing',['Visual storytelling','Planning','Editing'],['Photographer','Video Editor','Digital Marketer'],'Make a one-minute video or photo story.','2–4 hours/week'),
  ('Music or an instrument',['Practice discipline','Listening','Performance'],['Musician','Music Producer','Music Teacher'],'Practice a short piece three times this week.','2–4 hours/week')],
 'People & community': [
  ('Volunteering',['Empathy','Teamwork','Organization'],['Teacher','Social Worker','Community Development Officer'],'Help with a supervised school or community activity.','1–3 hours/week'),
  ('Debate & public speaking',['Communication','Research','Confidence'],['Lawyer','Teacher','Public Relations Specialist'],'Prepare a two-minute talk and practice it.','1–2 hours/week'),
  ('Tutoring classmates',['Explaining ideas','Patience','Leadership'],['Teacher','Lecturer','Training Specialist'],'Help a classmate understand a topic you know well.','1–2 hours/week')],
 'Business & leadership': [
  ('Planning a school club or event',['Leadership','Planning','Teamwork'],['Entrepreneur','Project Manager','Business Manager'],'Plan a small activity with a budget and task list.','2–3 hours/week'),
  ('Budgeting & personal finance',['Numeracy','Planning','Decision-making'],['Accountant','Financial Analyst','Economist'],'Create a sample monthly budget and compare choices.','1 hour/week'),
  ('Selling crafts or products',['Customer service','Creativity','Marketing'],['Entrepreneur','Marketing Specialist','Product Manager'],'Develop a product idea and ask people for feedback.','2–4 hours/week')],
 'Science, nature & health': [
  ('Gardening & nature journaling',['Observation','Patience','Record keeping'],['Environmental Scientist','Agricultural Scientist','Botanist'],'Grow a plant or record local nature over two weeks.','1–3 hours/week'),
  ('Safe science experiments',['Curiosity','Testing ideas','Data recording'],['Scientist','Laboratory Technologist','Engineer'],'Try a safe school-level experiment and record results.','1–2 hours/week'),
  ('Sports & fitness',['Discipline','Teamwork','Goal setting'],['Sports Coach','Physiotherapist','Sports Scientist'],'Choose a safe activity and track your progress.','2–4 hours/week')],
 'Practical & hands-on': [
  ('Cooking & baking',['Planning','Creativity','Measurement'],['Chef','Food Scientist','Hospitality Manager'],'Learn a recipe and note what you would improve.','1–3 hours/week'),
  ('DIY & making things',['Troubleshooting','Spatial reasoning','Practical problem-solving'],['Product Designer','Technician','Industrial Designer'],'Make a useful item from safe recycled materials.','1–3 hours/week')]
}
CAREERS = {
 'Technology':(['Software Developer','Data Analyst','Cybersecurity Analyst','UI/UX Designer'],['Problem-solving','Digital literacy','Communication','Project building'],'Build a small website, analyze a simple dataset, or design an app screen.'),
 'Creative arts & media':(['Graphic Designer','Writer','Video Editor','Animator','Digital Marketer'],['Creativity','Communication','Portfolio building','Time management'],'Create three sample pieces and ask for constructive feedback.'),
 'Health & life sciences':(['Doctor','Nurse','Physiotherapist','Laboratory Scientist','Public Health Worker'],['Biology foundations','Empathy','Attention to detail','Teamwork'],'Explore biology or create a health-awareness project using trusted sources.'),
 'Engineering & environment':(['Civil Engineer','Electrical Engineer','Environmental Scientist','Agricultural Scientist'],['Mathematics','Scientific thinking','Design','Practical problem-solving'],'Build a simple model or track a local environmental issue.'),
 'Business, law & leadership':(['Accountant','Entrepreneur','Lawyer','Project Manager','Economist'],['Communication','Numeracy','Research','Leadership'],'Plan a small event, make a mock budget, or research a community issue.'),
 'Education & social impact':(['Teacher','Social Worker','Policy Analyst','Community Development Officer'],['Empathy','Explaining ideas','Research','Organization'],'Tutor a peer or create a learning resource.'),
 'Hospitality, food & sport':(['Chef','Hospitality Manager','Sports Coach','Fitness Trainer','Food Scientist'],['Customer service','Planning','Discipline','Teamwork'],'Plan a menu, organize a friendly sports activity, or learn food-safety basics.')
}

if 'profile' not in st.session_state: st.session_state.profile = {'name':'','stage':'Senior secondary','categories':[],'interests':[],'skills':[],'goals':''}
if 'plan' not in st.session_state: st.session_state.plan = []
if 'recs' not in st.session_state: st.session_state.recs = None
profile = st.session_state.profile
page = st.sidebar.radio('Navigate',['Explore hobbies','Career explorer','My growth plan','About'])
st.sidebar.caption('Explore possibilities; you do not have to decide your whole future today.')

if page == 'Explore hobbies':
 st.subheader('Find hobbies that fit your curiosity')
 st.write('Choose areas you enjoy and skills you want to develop. You can change your answers at any time.')
 all_hobbies = [x[0] for entries in HOBBIES.values() for x in entries]
 all_skills = sorted({skill for entries in HOBBIES.values() for item in entries for skill in item[1]})
 with st.form('interest_form'):
  a,b = st.columns(2)
  name = a.text_input('What should we call you? (optional)',profile['name'])
  stage = a.selectbox('Your school stage',['Junior secondary','Senior secondary','College / university','Recent graduate','Other'],index=['Junior secondary','Senior secondary','College / university','Recent graduate','Other'].index(profile['stage']))
  categories = a.multiselect('Areas that interest you',list(HOBBIES),default=profile['categories'])
  interests = b.multiselect('Specific hobbies you are curious about',all_hobbies,default=profile['interests'])
  skills = b.multiselect('Skills you want to build',all_skills,default=profile['skills'])
  goals = st.text_area('What would you like to achieve? (optional)',profile['goals'],placeholder='e.g. build confidence, create a portfolio, explore careers')
  submitted = st.form_submit_button('✨ Find my hobby ideas',use_container_width=True)
 if submitted:
  profile.update({'name':name,'stage':stage,'categories':categories,'interests':interests,'skills':skills,'goals':goals})
  found=[]
  for cat, entries in HOBBIES.items():
   if categories and cat not in categories: continue
   for n, ss, cc, starter, time in entries:
    if (not interests and not skills) or n in interests or any(s in ss for s in skills): found.append({'name':n,'category':cat,'skills':ss,'careers':cc,'starter':starter,'time':time})
  st.session_state.recs=found
 if st.session_state.recs is not None:
  recs=st.session_state.recs
  if not recs: st.info('No close matches yet. Try choosing a broader area or more skills.')
  else:
   st.subheader(f'{len(recs)} hobby ideas to explore')
   cols=st.columns(2)
   for i,item in enumerate(recs):
    with cols[i%2]:
     with st.container(border=True):
      st.markdown('### '+item['name']); st.caption(item['category'])
      st.markdown('**Skills to practice**'); st.write(' · '.join(item['skills']))
      st.markdown('**Try this first**'); st.write(item['starter']); st.caption('Suggested time: '+item['time'])
      st.write('**Related careers:** '+', '.join(item['careers']))
      if st.button('＋ Add to my growth plan',key='add_'+item['name']):
       if not any(p['name']==item['name'] for p in st.session_state.plan): st.session_state.plan.append({'name':item['name'],'category':item['category'],'starter':item['starter'],'status':'Not started','notes':''}); st.success('Added to your plan.')
       else: st.info('Already in your plan.')
 else: st.info('Choose your interests above and click Find my hobby ideas.')

elif page == 'Career explorer':
 st.subheader('Explore career directions')
 st.write('Careers combine subjects, skills, values, and opportunities. These examples are starting points, not predictions.')
 path=st.selectbox('Which area would you like to explore?',list(CAREERS))
 careers,skills,project=CAREERS[path]
 a,b=st.columns(2)
 with a:
  st.markdown('### Example careers')
  for x in careers: st.write('• '+x)
 with b:
  st.markdown('### Useful skills')
  for x in skills: st.write('• '+x)
 st.markdown('### A small project to try'); st.info(project)
 st.markdown('### Reflect on these questions')
 st.write('- Do I enjoy the activities involved in this field?')
 st.write('- Which school subjects or hobbies connect to it?')
 st.write('- What qualifications or training are needed where I live?')
 st.write('- Can I speak with a teacher, career adviser, or professional?')
 if st.button('＋ Add career exploration to my plan'):
  goal={'name':'Explore: '+path,'category':'Career exploration','starter':project,'status':'Not started','notes':''}
  if not any(x['name']==goal['name'] for x in st.session_state.plan): st.session_state.plan.append(goal); st.success('Added to your plan.')
  else: st.info('Already in your plan.')

elif page == 'My growth plan':
 st.subheader('My hobby and skills growth plan')
 st.write('Keep the plan small and flexible. Progress matters more than perfection.')
 if not st.session_state.plan: st.info('Your plan is empty. Add an activity from Explore hobbies or Career explorer.')
 else:
  done=sum(x['status']=='Completed' for x in st.session_state.plan)
  st.metric('Activities completed',f'{done} / {len(st.session_state.plan)}'); st.progress(done/len(st.session_state.plan))
  for i,item in enumerate(st.session_state.plan):
   with st.container(border=True):
    st.markdown('### '+item['name']); st.caption(item['category']); st.write(item['starter'])
    status=st.selectbox('Progress',['Not started','In progress','Completed'],index=['Not started','In progress','Completed'].index(item['status']),key=f'status{i}')
    notes=st.text_area('Notes / what I learned',item.get('notes',''),key=f'notes{i}',height=70)
    a,b=st.columns(2)
    if a.button('Save progress',key=f'save{i}'):
     st.session_state.plan[i]['status']=status; st.session_state.plan[i]['notes']=notes; st.success('Progress saved.'); st.rerun()
    if b.button('Remove',key=f'remove{i}'):
     st.session_state.plan.pop(i); st.rerun()
  export={'profile':profile,'growth_plan':st.session_state.plan,'exported_at':datetime.now().isoformat(timespec='seconds')}
  st.download_button('Download my growth plan (JSON)',json.dumps(export,indent=2),file_name='pathfinder_growth_plan.json',mime='application/json')
  st.caption('This starter app keeps plans in the current session. Download your plan to keep a copy.')
else:
 st.subheader('About PathFinder')
 st.write('PathFinder helps students discover hobbies, practice transferable skills, explore related careers, and record small growth goals.')
 st.info('Hobbies can be worthwhile even when they do not become careers. Explore, reflect, ask questions, and change direction as you learn.')
 st.markdown('### Possible future features')
 st.write('- Student accounts and cloud-saved plans\n- Interest quiz with explainable matching\n- Mentor or teacher dashboard\n- Optional AI-assisted reflection prompts\n- Courses, clubs, scholarships, and career resources')
 st.caption('Career suggestions are exploratory and are not a guarantee of fit or success. Consider your interests, values, learning opportunities, and local qualification requirements.')
