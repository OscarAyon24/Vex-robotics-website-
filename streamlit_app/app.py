import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="VEX Robotics Club",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for orange, green, white theme and gears
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ff9800 0%, #4caf50 100%);
    }
    .main {
        background-color: #fff;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 24px rgba(0,0,0,0.08);
    }
    h1, h2, h3 {
        color: #ff9800;
        font-family: 'Roboto', sans-serif;
    }
    .stButton>button {
        background-color: #4caf50;
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #388e3c;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Gear SVG for decoration
def gear_svg(size=40, color="#ff9800"):
    return f'''
    <svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <g>
    <circle cx="12" cy="12" r="5" stroke="{color}" stroke-width="2" fill="white"/>
    <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41" stroke="{color}" stroke-width="2"/>
    </g>
    </svg>
    '''

# Sidebar navigation
st.sidebar.markdown(gear_svg(60, "#4caf50"), unsafe_allow_html=True)
page = st.sidebar.radio("Navigate", ["About", "Teams", "Schedule"])
st.sidebar.markdown(gear_svg(60, "#ff9800"), unsafe_allow_html=True)

st.markdown(f"<div style='text-align:center'>{gear_svg(60)}<h1>VEX Robotics Club</h1>{gear_svg(60, '#4caf50')}</div>", unsafe_allow_html=True)

if page == "About":
    st.header("About Us")
    st.write("""
    Welcome to the VEX Robotics Club! Our club is dedicated to fostering a love for robotics and technology among students. 
    We provide hands-on learning where members build, program, and compete with robots.

    **How it works:**
    - Regular meetings and workshops
    - Team collaboration on projects
    - Preparation for competitions
    - Emphasis on teamwork, creativity, and innovation
    """)
    st.markdown(gear_svg(40, "#4caf50"), unsafe_allow_html=True)

elif page == "Teams":
    st.header("Our Teams")
    teams = [
        {"name": "Design Team", "desc": "Creates robot design and aesthetics."},
        {"name": "Programming Team", "desc": "Codes and develops software for the robot."},
        {"name": "Build Team", "desc": "Assembles and constructs the robot."},
        {"name": "Marketing Team", "desc": "Promotes the club and manages outreach."},
    ]
    for t in teams:
        st.subheader(t["name"])
        st.write(t["desc"])
        st.markdown(gear_svg(30, "#ff9800"), unsafe_allow_html=True)

elif page == "Schedule":
    st.header("Competition Schedule")
    schedule = [
        {"date": "2023-10-15", "time": "10:00 AM", "location": "School Gymnasium"},
        {"date": "2023-11-05", "time": "1:00 PM", "location": "Community Center"},
        {"date": "2023-12-01", "time": "9:00 AM", "location": "City Stadium"},
    ]
    st.table(schedule)
    st.markdown(gear_svg(40, "#4caf50"), unsafe_allow_html=True)
