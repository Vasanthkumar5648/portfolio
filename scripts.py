import streamlit as st
from PIL import Image
import base64

# Set page configuration
st.set_page_config(
    page_title="Your Name | Professional Portfolio",
    page_icon="👨‍💼",
    layout="wide"
)

# Embedded CSS styling
def set_custom_style():
    st.markdown("""
    <style>
    /* Main content styling */
    .stApp {
        background-color: #f8f9fa;
    }
    .stMarkdown h1 {
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
    }
    .stMarkdown h2 {
        color: #2980b9;
    }
    .stMarkdown h3 {
        color: #16a085;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #2c3e50 !important;
    }
    [data-testid="stSidebar"] .stMarkdown h1 {
        color: white !important;
        border-bottom: 2px solid #3498db;
    }
    [data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }
    
    /* Button styling */
    .stDownloadButton button {
        background-color: #3498db !important;
        color: white !important;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
    }
    
    /* Expander styling */
    .stExpander {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        padding: 15px;
        margin-bottom: 20px;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 20px;
        color: #7f8c8d;
    }
    </style>
    """, unsafe_allow_html=True)

set_custom_style()

# Sidebar
with st.sidebar:
    st.title("Navigation")
    menu = ["Home", "About Me", "Projects", "Skills", "Experience", "Education", "Contact"]
    choice = st.radio("Go to", menu)
    
    # Contact information in sidebar
    st.markdown("---")
    st.subheader("Contact Info")
    st.write("📧 email@example.com")
    st.write("📞 +1 (123) 456-7890")
    st.write("📍 Your City, Country")
    
    # Social media links
    st.markdown("---")
    st.subheader("Connect With Me")
    st.markdown("[LinkedIn](#)", unsafe_allow_html=True)
    st.markdown("[GitHub](#)", unsafe_allow_html=True)
    st.markdown("[Twitter](#)", unsafe_allow_html=True)

# Home Page
if choice == "Home":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Placeholder for profile image (replace with actual image loading if available)
        st.image(Image.new('RGB', (250, 250), color='#3498db'), width=250, 
                caption="Profile Image (replace with your image)")
    
    with col2:
        st.title("Your Name")
        st.subheader("Your Profession/Tagline")
        st.write("""
        Welcome to my professional portfolio! I'm passionate about [your field] 
        with expertise in [key skills]. This portfolio showcases my work, skills, 
        and professional journey.
        """)
        
        # Download resume button (placeholder)
        st.download_button(
            label="Download Resume",
            data="This would be your resume content".encode(),
            file_name="YourName_Resume.pdf",
            mime="application/octet-stream",
        )

# About Me Page
elif choice == "About Me":
    st.title("About Me")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(Image.new('RGB', (300, 300), color='#16a085'), 
                width=300, caption="About Me Image")
    
    with col2:
        st.write("""
        ## Who Am I?
        A detailed introduction about yourself, your professional journey, 
        and what drives you. Highlight your values, approach to work, and 
        what makes you unique.
        
        ### Professional Philosophy
        - Value 1: Explanation
        - Value 2: Explanation
        - Value 3: Explanation
        
        ### Personal Interests
        Outside of work, I enjoy [hobby 1], [hobby 2], and [hobby 3]. 
        These activities help me [benefit they provide].
        """)

# Projects Page
elif choice == "Projects":
    st.title("My Projects")
    st.markdown("---")
    
    # Project 1
    with st.expander("**Project 1: Project Name**", expanded=True):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(Image.new('RGB', (250, 150), color='#e74c3c'), 
                    width=250, caption="Project Screenshot")
        
        with col2:
            st.write("""
            ### Overview
            Brief description of the project, its purpose, and your role.
            
            ### Technologies Used
            - Technology 1
            - Technology 2
            - Technology 3
            
            ### Key Achievements
            - Achievement 1
            - Achievement 2
            
            [View Project](#) | [GitHub Repository](#)
            """)
    
    # Project 2
    with st.expander("**Project 2: Project Name**", expanded=False):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(Image.new('RGB', (250, 150), color='#9b59b6'), 
                    width=250, caption="Project Screenshot")
        
        with col2:
            st.write("""
            ### Overview
            Brief description of the project, its purpose, and your role.
            
            ### Technologies Used
            - Technology 1
            - Technology 2
            - Technology 3
            
            ### Key Achievements
            - Achievement 1
            - Achievement 2
            
            [View Project](#) | [GitHub Repository](#)
            """)

# Skills Page
elif choice == "Skills":
    st.title("My Skills")
    st.markdown("---")
    
    # Technical Skills
    st.subheader("Technical Skills")
    tech_skills = {
        "Programming Languages": ["Python", "JavaScript", "SQL"],
        "Frameworks": ["Streamlit", "React", "Django"],
        "Tools": ["Git", "Docker", "AWS"],
    }
    
    for category, skills in tech_skills.items():
        with st.expander(f"**{category}**"):
            for skill in skills:
                st.write(f"- {skill}")
    
    # Professional Skills
    st.subheader("Professional Skills")
    prof_skills = ["Communication", "Team Leadership", "Project Management", "Problem Solving"]
    for skill in prof_skills:
        st.write(f"- {skill}")

# Experience Page
elif choice == "Experience":
    st.title("Professional Experience")
    st.markdown("---")
    
    # Job 1
    with st.expander("**Company 1 | Job Title** (2020 - Present)", expanded=True):
        st.write("""
        ### Responsibilities
        - Developed and maintained web applications
        - Collaborated with cross-functional teams
        - Implemented new features and improvements
        
        ### Achievements
        - Increased system performance by 30%
        - Led a team of 5 developers
        """)
    
    # Job 2
    with st.expander("**Company 2 | Junior Developer** (2018 - 2020)", expanded=False):
        st.write("""
        ### Responsibilities
        - Assisted in development tasks
        - Fixed bugs and issues
        - Participated in code reviews
        
        ### Achievements
        - Implemented key feature that improved user retention
        - Received employee of the month award
        """)

# Education Page
elif choice == "Education":
    st.title("Education & Certifications")
    st.markdown("---")
    
    # Education 1
    with st.expander("**Bachelor of Science in Computer Science** - University Name (2014 - 2018)", expanded=True):
        st.write("""
        - Major: Computer Science
        - GPA: 3.8/4.00
        - Relevant Coursework: Data Structures, Algorithms, Web Development
        """)
    
    # Certifications
    st.subheader("Certifications")
    certs = {
        "AWS Certified Developer": "Amazon Web Services (2021)",
        "Python Professional Certification": "Python Institute (2020)",
    }
    for cert, details in certs.items():
        st.write(f"- **{cert}**: {details}")

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
            st.success("Thank you for your message! I'll get back to you soon.")

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>© 2023 Your Name. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
