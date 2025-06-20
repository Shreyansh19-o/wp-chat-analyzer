WhatsApp Chat Analyzer 📊💬
Analyze your WhatsApp chat data with insightful visualizations and statistics! This Streamlit-powered web application allows you to upload your exported WhatsApp chat .txt file and get instant analytics on message counts, word usage, media shared, links shared, most active users, common words, emoji usage, and timelines.

✨ Features
Overall Chat Statistics: Get a quick overview of total messages, words, media files, and links shared in the entire chat.

Individual User Analysis: Dive deep into the chat patterns of a specific user.

Most Active Users (Group Chats): Identify the top contributors in your group chats with a message count breakdown and a visual bar chart.

Word Cloud Generation: Visualize the most frequently used words in the chat for both overall and individual users.

Most Common Words: See a detailed list and bar chart of the most frequently used words (excluding stopwords).

Emoji Analysis: Discover the most used emojis and their distribution in the chat.

Monthly & Daily Timelines: Track message activity over time to identify peak communication periods.

Activity Maps: Analyze daily and monthly activity patterns to understand when the chat is most busy.

🚀 How to Use
1. Prerequisites
Before you begin, ensure you have Python installed on your system.

2. Export Your WhatsApp Chat
To use this analyzer, you first need to export your WhatsApp chat.

Open the WhatsApp chat you want to analyze.

Tap on the three dots (menu) in the top right corner.

Go to More > Export chat.

Choose Without Media. (The analyzer currently focuses on text and counts media/links as separate entities, but doesn't process the media itself).

Save the .txt file to your device.

3. Setup the Project
Clone this repository (if applicable) or download the files:

git clone https://github.com/your-username/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer

(Replace your-username with your actual GitHub username or the repository URL)

Install Dependencies:
It's recommended to use a virtual environment.

python -m venv venv
.\venv\Scripts\activate   # On Windows
source venv/bin/activate # On macOS/Linux

Then install the required libraries:

pip install streamlit pandas matplotlib wordcloud emoji nltk

Ensure Helper Files are Present:
Make sure preprocessor.py and helper.py are in the same directory as app.py (your main Streamlit script). These files contain the core logic for data cleaning and analysis.

4. Run the Application
Open your terminal or command prompt.

Navigate to the project directory where app.py is located.

Run the Streamlit application:

streamlit run app.py

Your web browser will automatically open a new tab with the WhatsApp Chat Analyzer application.

5. Analyze Your Chat
Upload File: In the sidebar of the Streamlit app, click on "Choose a file" and upload the .txt file you exported from WhatsApp.

Select User: Once the file is processed, you can choose "overall" or select a specific user from the dropdown menu to see their analysis.

Show Analysis: Click the "Show Analysis" button to display the results!

🛠️ Technologies Used
Python

Streamlit: For building the interactive web application.

Pandas: For data manipulation and analysis.

Matplotlib: For creating static, embeddable plots.

WordCloud: For generating visually appealing word clouds.

Emoji: For handling and counting emojis.

NLTK (Natural Language Toolkit): For text processing (e.g., stopwords).

