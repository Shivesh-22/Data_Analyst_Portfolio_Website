from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon="🌒",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("/Users/shiveshsingh/Documents/style/style.css")

# ---- LOAD ASSETS ----

lottie_coding = load_lottieurl("https://lottie.host/2e4d229f-ef34-4293-904f-36e8812cdac7/KYyQJmstHa.json")
img_EDA = Image.open("/Users/shiveshsingh/Documents/Images/data6.png")
img_web = Image.open("/Users/shiveshsingh/Documents/Images/data7.png")

# ----HEADER SECTION ----

with st.container():
    st.subheader("Hi, I am Shivesh 👋🏻")
    st.title("A Data Analyst From India")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings.")

# ---- WHAT I DO ----

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do:")
        st.write("##")
        st.write("""
                 - My job as a data analyst is to find patterns and insights that are
                 hidden in large datasets. I collect,purify,and arrange data to guarantee
                 its correctness and applicability.
                 - I then use statistical techniques and machine learning algorithms to draw relevant conclusions. My job goes beyond
                 analysis; I also convert intricate results into understandable, practical insights
                 that inform business expansion and strategic choices.
                 - Whether it's determining consumer behaviour, seeing market trends, or streamlining internal operations,
                 I use data to make insightful recommendations that improve effectiveness and
                 performance.
                 - In addition, I work cross-functionally with others to create and
                 manage data systems that gaurantee data integrity and facilitate well-informed
                 decision-making throughout the company.
                 - My area of interest is using data to drive change and add value for the company.
                """)

with right_column:
    st_lottie(lottie_coding, height = 400, key="Data Analytics")


# ---- PROJECTS ----

with st.container():
    st.write("---")
    st.header("My Projects:")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_EDA)

        
    with text_column:
        st.subheader("Exploratory Data Analysis(EDA)")
        st.write(
            """
            As part of my data analysis portfolio, I completed an exploratory data analysis project
            centered on E-commerce sales. By employing statistical methods and visualization tools like
            histograms and scatter plots, I unearthed significant patterns and relationships within the data,
            aiding in understanding customer behaviour and market trends. Through meticulous data cleaning
            and insightful analysis, I showcased my ability to derive actionable insights and present them
            visually. This project underscores my expertise in data exploration and analysis, highlighting my
            capacity to extract valuable information from raw datasets.
            """)

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_web)
    with text_column:
        st.subheader("Web Scraping")
        st.write(
            """
            In my web scraping project, I developed a Python-based tool using BeautifulSoup and Scrapy
            to extract data from Amazon.in. This automated process enabled efficient collection of data
            for purposes such as market research and price monitoring. I navigated through web structures,
            handled dynamic content, and implemented error-handling mechanisms to ensure robust data extraction.
            Through data cleaning and preprocessing, I prepared the extracted data for analysis. This project
            showcased my ability to leverage technology for efficient data acquisition, streamlining workflows,
            and facilitating data-driven decision-making processes.
            """)

# ---- CONTACT ----

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
        <form action="https://formsubmit.co/shiveshs464@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">   
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
            
