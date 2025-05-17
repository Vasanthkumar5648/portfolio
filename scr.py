import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import base64

# Set page configuration
st.set_page_config(
    page_title="Vasantha Kumar | Professional Portfolio",
    page_icon="👨‍💼",
    layout="wide"
)

# Function to load image from URL
def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# GitHub image URLs (replace with your actual image URLs)
PROFILE_IMAGE_URL ="https://raw.github.com/Vasanthkumar5648/portfolio/main/image.jpg%20(2)%20(1).jpg"
ABOUT_IMAGE_URL ="https://raw.http://github.com/Vasanthkumar5648/portfolio/main/image.jpg%20(2)%20(1).jpg"

# Custom CSS for black sidebar with white text
st.markdown("""
<style>
    /* Black sidebar background */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
    }
    
    /* White text for all sidebar content */
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* White radio button labels */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
        color: white !important;
    }
    
    /* White radio button circles */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] div[data-baseweb="radio"] div:first-child {
        background-color: white !important;
    }
    
    /* White links */
    [data-testid="stSidebar"] a {
        color: white !important;
    }
    
    /* Hover effect for links */
    [data-testid="stSidebar"] a:hover {
        color: #3498db !important;
    }
    
    /* Image styling */
    .profile-img {
        border-radius: 50%;
        border: 3px solid white;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with black background
with st.sidebar:
    st.title("Navigation")
    menu = ["Home", "About Me", "Projects", "Skills", "Experience", "Education", "Contact"]
    choice = st.radio("Go to", menu)
    
    # Contact information
    st.markdown("---")
    st.subheader("Contact Info")
    st.markdown("📧 vasanthkumar5648@gmail.com")
    st.markdown("📞 +91 9791585648")
    st.markdown("📍 Chennai, India")
    
    # Social media links
    st.markdown("---")
    st.subheader("Connect With Me")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/vasantha-kumar-p-99119a2b3)")
    st.markdown("[Tableau Portfolio](https://public.tableau.com/app/profile/vasantha.kumar2203/vizzes)")
    st.markdown("[GitHub](https://github.com/Vasanthkumar5648)")
    st.markdown("[Data Science Portfolio](https://www.datascienceportfol.io/vasanthkumar5648)")

# Home Page
if choice == "Home":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            profile_img = load_image_from_url(PROFILE_IMAGE_URL)
            st.image(profile_img, width=250, caption="", output_format="JPEG", use_column_width=False, clamp=True, channels="RGB", 
                    format="JPEG", class_="profile-img")
        except:
            st.image(Image.new('RGB', (250, 250), color='#3498db'), width=250, 
                    caption="Profile Image")
    
    with col2:
        st.title("Vasantha Kumar")
        st.subheader("Data Science Analyst | MBA in Aviation Management")
        st.write("""
        Aspiring Data Science Analyst with a strong foundation in statistics, machine learning, 
        and data visualization. Skilled in Python, SQL, and data analytics tools with hands-on 
        experience in data modeling and hypothesis testing.
        """)
        
        # Download resume button (placeholder)
        st.download_button(
            label="Download Resume",
            data="This would be your resume content".encode(),
            file_name="VasanthaKumar_Resume.pdf",
            mime="application/octet-stream",
        )

# About Me Page
elif choice == "About Me":
    st.title("About Me")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            about_img = load_image_from_url(ABOUT_IMAGE_URL)
            st.image(about_img, width=300, caption="", output_format="JPEG")
        except:
            st.image(Image.new('RGB', (300, 300), color='#16a085'), 
                    width=300, caption="About Me Image")
    
    with col2:
        st.write("""
        ## Professional Profile
        I am an aspiring Data Science Analyst with a unique combination of technical skills 
        in data science and business acumen from my MBA in Aviation Management. My passion 
        lies in transforming raw data into meaningful insights that drive strategic decisions.
        
        ### Career Objective
        Seeking to leverage my analytical skills, Python and SQL expertise, and hands-on 
        experience in data modeling to support strategic decision-making and drive impactful 
        business insights at organizations like American Express.
        
        ### Personal Interests
        Outside of work, I enjoy exploring new data visualization techniques, contributing to 
        open-source projects, and staying updated with the latest advancements in AI and ML.
        """)

# [Rest of your pages (Projects, Skills, Experience, Education, Contact) would go here]
# Keep the same content as before, just ensure proper indentation# Projects Page
elif choice == "Projects":
    st.title("My Projects")
    st.markdown("---")
    
    # Project 1
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("Titanic ML Predictive Model using Logistic Regression")
        st.write("**Technologies:** Python, Machine Learning, Statistics, Hypothesis Testing")
        st.write("""
        Developed a binary classification model to predict Titanic passenger survival with 
        comprehensive feature engineering and model evaluation.
        """)
        st.markdown('[View on GitHub](https://github.com/Vasanthkumar5648/Machine-Learing/tree/main/Titanic%20ML%20predictive%20model)', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 2
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("Iris Dataset - Multiclass Classification")
        st.write("**Technologies:** Python, Data Visualization, Machine Learning")
        st.write("""
        Built a multiclass classifier using Logistic Regression for flower classification 
        with detailed exploratory data analysis.
        """)
        st.markdown('[View on GitHub](https://github.com/Vasanthkumar5648/Machine-Learing/tree/main/Iris%20Dataset%20by%20using%20LogisticRegression%20Multiclass%20Classification)', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 3
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("Netflix Dashboard (Tableau)")
        st.write("**Technologies:** Tableau, Data Visualization")
        st.write("""
        Built an interactive dashboard to analyze Netflix content distribution by year, 
        genre, and country with insightful visualizations.
        """)
        st.markdown('[View on Tableau Public](https://public.tableau.com/app/profile/vasantha.kumar2203/viz/NetFlixDashboard_17369621170060/NetflixDashboard)', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Skills Page
elif choice == "Skills":
    st.title("My Skills")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Technical Skills")
        st.markdown("""
        <div>
            <span class="skill-chip">Python</span>
            <span class="skill-chip">SQL</span>
            <span class="skill-chip">Power BI</span>
            <span class="skill-chip">Tableau</span>
            <span class="skill-chip">Machine Learning</span>
            <span class="skill-chip">Deep Learning</span>
            <span class="skill-chip">NLP</span>
            <span class="skill-chip">AI</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Analytics Tools")
        st.markdown("""
        <div>
            <span class="skill-chip">Pandas</span>
            <span class="skill-chip">NumPy</span>
            <span class="skill-chip">Scikit-learn</span>
            <span class="skill-chip">Matplotlib</span>
            <span class="skill-chip">Seaborn</span>
            <span class="skill-chip">MS Excel</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("Business Skills")
        st.markdown("""
        <div>
            <span class="skill-chip">Data Analytics</span>
            <span class="skill-chip">SEO</span>
            <span class="skill-chip">Business Strategy</span>
            <span class="skill-chip">Market Research</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Soft Skills")
        st.markdown("""
        <div>
            <span class="skill-chip">Communication</span>
            <span class="skill-chip">Team Collaboration</span>
            <span class="skill-chip">Leadership</span>
            <span class="skill-chip">Problem Solving</span>
        </div>
        """, unsafe_allow_html=True)

# Experience Page
elif choice == "Experience":
    st.title("Professional Experience")
    st.markdown("---")
    
    with st.expander("**Operations Intern**, Airport Authority of India, Chennai (Mar 2024 - Apr 2024)", expanded=True):
        st.write("""
        - Managed operational processes, ensuring regulatory compliance and safety standards
        - Gained hands-on experience in airport operations and customer service
        - Assisted in data collection and analysis for operational improvements
        """)
    
    with st.expander("**Data Analytics Intern**, Tata Forage Virtual, Chennai (Feb 2024 - Apr 2024)", expanded=False):
        st.write("""
        - Designed Power BI reports to deliver key supermarket insights to executive stakeholders
        - Analyzed business problems and proposed data-driven solutions
        - Created dashboards to track KPIs and business performance metrics
        """)
    
    with st.expander("**SEO Intern**, PickYourTrail, Chennai (Jul 2023 - Sep 2023)", expanded=False):
        st.write("""
        - Optimized website architecture and content to improve search engine rankings
        - Conducted keyword research and analyzed user engagement metrics
        - Implemented SEO strategies that increased organic traffic by 25%
        """)

# Education Page
elif choice == "Education":
    st.title("Education & Certifications")
    st.markdown("---")
    
    with st.expander("**MBA, Aviation Management**, Hindustan Institute Of Technology And Science (2022 - 2024)", expanded=True):
        st.write("""
        - CGPA: 8.50 / 10
        - Specialization in Business Analytics and Aviation Operations
        - Relevant coursework: Data Analysis for Decision Making, Business Statistics
        """)
    
    with st.expander("**B.E, Aeronautical Engineering**, Rajalakshmi Engineering College (2017 - 2021)", expanded=False):
        st.write("""
        - CGPA: 7.32 / 10
        - Thesis: "Morphing of Rocket Nose Cone" (Jan 2021 - Apr 2021)
        - Relevant coursework: Computational Fluid Dynamics, Aerodynamics
        """)
    
    st.subheader("Certifications")
    with st.expander("**Data Science & AI**, Boston Institute Of Analytics, Chennai (Oct 2024 - Present)"):
        st.write("Comprehensive training in machine learning, deep learning, and AI applications")
    
    with st.expander("**Business Analytics**, Internshala Trainings (Jan 2024 - Feb 2024)"):
        st.write("Hands-on training in data analysis, visualization, and business intelligence tools")

# Contact Page
elif choice == "Contact":
    st.title("Get In Touch")
    st.markdown("---")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thank you for your message, Vasantha will get back to you soon!")

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>© 2023 Vasantha Kumar. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
