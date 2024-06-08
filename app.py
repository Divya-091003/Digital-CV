import streamlit as st
from pathlib import Path
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic_path = current_dir / "assets" / "divya.jpg"

PAGE_TITLE = "Digital CV | Divya M"
PAGE_ICON = ":wave:"
NAME = "Divya"
DESCRIPTION = """
My skills include Python, HTML, and Java. I am a goal-oriented person with good communication skills.
"""
EMAIL = "divya091003divya@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/divya-m",
    "GitHub": "https://github.com/Divya-091003/Project"
}

PROJECTS = {
    "Inventory Management System": "A project that includes details of employee products and sales in a company.",
    "Heart Disease Predictor": "A project that predicts heart disease.",
    "Automatic Sensing Taps": "A project that senses any object automatically."
}
LEADERSHIP_SKILLS = [
    "Communication skills",
    "Project Management",
    "Time Management",
    "Leadership",
    "Teamwork"
]

Course_workshop = [
    "Python course given by IBM including certificate",
    "RDBMS course given by IBM including certificate",
    "Attended workshop based on soft skills and entrepreneurship given by Microsoft"
]

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load CSS and PDF and profile picture
if css_file.exists():
    st.markdown(f'<style>{css_file.read_text()}</style>', unsafe_allow_html=True)
else:
    st.warning("Welcome to my digital CV!")

if resume_file.exists():
    with open(resume_file, "rb") as pdf_file:
        pdf_byte = pdf_file.read()
else:
    st.warning("Resume file not found!")

if profile_pic_path.exists():
    profile_pic = Image.open(profile_pic_path)
    profile_pic = profile_pic.resize((150, 150))  # Resize the profile picture
else:
    st.warning("Profile picture not found!")

col1, col2 = st.columns([1, 3])  # Adjust the column widths as needed
with col1:
    st.image(profile_pic)
with col2:
    st.title(NAME)
    st.markdown(DESCRIPTION)

    st.subheader("Projects")
    for project_name, project_description in PROJECTS.items():
        st.write(f"**{project_name}:** {project_description}")

    st.subheader("Leadership Skills")
    st.write("\n".join([f"- {skill}" for skill in LEADERSHIP_SKILLS]))


    st.subheader("Contact")
    st.write(f"Email: {EMAIL}")
    for platform, link in SOCIAL_MEDIA.items():
        st.write(f"{platform}: [{link}]({link})")

    st.download_button(
        label="Download Resume",
        data=pdf_byte,
        file_name=resume_file.name,
        mime="application/pdf",
    )
