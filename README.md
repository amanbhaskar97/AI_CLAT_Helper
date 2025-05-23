# AI_CLAT_Helper

# 🎓 MentorAllocation

**MentorAllocation** is a simple yet effective Python-based recommendation system that helps connect aspirants with the most suitable mentors based on preferences like subjects, target colleges, preparation levels, and learning styles.

## 🚀 Features

- ✅ Matches aspirants with mentors using **cosine similarity** on TF-IDF vectorized data
- 🔍 Considers multiple factors: subject expertise, college background, experience level, and mentoring style
- 📊 Collects user feedback and stores it for future insights
- 📁 Reads and writes data using Excel files (`MentorInfo.xlsx`, `Feedback.xlsx`)

---

## 🛠️ How It Works

1. **User Input**  
   The aspirant enters:
   - Preferred subjects
   - Target college
   - Preparation level (Beginner / Intermediate / Advanced)
   - Learning style (Visual / Auditory / Kinesthetic)

2. **Mentor Matching**  
   The system:
   - Loads mentor data from `MentorInfo.xlsx`
   - Builds a combined textual feature for each mentor
   - Vectorizes both mentor and aspirant data using **TF-IDF**
   - Calculates **cosine similarity** between the aspirant and each mentor
   - Outputs the top 3 mentor matches

3. **Feedback Collection**  
   After showing recommendations, the user is prompted to provide feedback, which is saved in `Feedback.xlsx`.

---

# 🤖 CLAT Legal Exam Chatbot

**CLAT Legal Exam Chatbot** is an AI-powered query chatbot designed to assist students preparing for the CLAT (Common Law Admission Test). Powered by the **Gemini 2.0** generative model, this chatbot answers CLAT-related questions using context-based information loaded from text files.

---

## 🚀 Features

- 🤖 AI-powered chatbot answering CLAT-related queries
- 🧠 Uses **Gemini 2.0** generative model for accurate responses
- 📝 Loads context-based answers from text files located in the `data/` folder
- 🌐 Web app built with **Streamlit** for easy interaction
- 🔑 Requires a **Gemini API key** (to be added in the `.env` file)

---

## 🛠️ How It Works

1. **Initialize the Chatbot**  
   - The chatbot loads the context from text files located in the `data/` folder. These files contain information related to the CLAT exam.
   
2. **User Query**  
   - The user enters a question related to the CLAT exam.

3. **Generate Answer**  
   - The chatbot uses the **Gemini 2.0** model to generate an answer based on the provided context.

4. **Display Result**  
   - The generated answer is displayed in the web interface for the user.

---