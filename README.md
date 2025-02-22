<h1>TalentScout - AI Hiring Assistant</h1>

<h2>Overview</h2>
<p><strong>TalentScout</strong> is an AI-powered chatbot designed to help recruiters streamline the initial screening process for job candidates. It collects essential details, generates technical interview questions based on the candidate’s skills, and performs sentiment analysis on their responses. By leveraging <strong>large language models (LLMs)</strong> and <strong>multilingual support</strong>, TalentScout enhances the hiring process, saving recruiters valuable time.</p>

<h2>Key Features</h2>
<ul>
    <li><strong>Candidate Information Collection:</strong> Captures details like name, email, experience, preferred role, and tech stack.</li>
    <li><strong>AI-Generated Interview Questions:</strong> Creates <strong>five</strong> custom technical questions based on the candidate’s skills.</li>
    <li><strong>Multilingual Support:</strong> Supports over <strong>100 languages</strong>, making it accessible to global candidates.</li>
    <li><strong>Sentiment Analysis:</strong> Evaluates candidate feedback to determine their sentiment (<em>positive, negative, or neutral</em>).</li>
    <li><strong>User-Friendly Interface:</strong> Built with <strong>Streamlit</strong>, offering a clean and interactive experience.</li>
    <li><strong>Real-Time Translation:</strong> Uses <strong>Google Translate API</strong> to translate questions and responses instantly.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Python</strong> (Streamlit, Hugging Face API, Google Translate API)</li>
    <li><strong>Hugging Face Falcon-7B</strong> (AI model for question generation)</li>
    <li><strong>Google Translate API</strong> (for multilingual support)</li>
    <li><strong>TextBlob</strong> (for sentiment analysis)</li>
    <li><strong>Streamlit</strong> (to create the chatbot’s web interface)</li>
</ul>

<h2>Project Structure</h2>
<pre>
TalentScout-Chatbot
├── app.py               # Main chatbot application (Streamlit)
├── prompts.py           # Templates for AI-generated questions
├── .env                 # Stores API keys (should not be pushed to GitHub)
├── requirements.txt     # Lists required Python libraries
├── README.md            # Documentation (this file)
└── utils/               # Helper functions for translation & sentiment analysis
</pre>

<h2>Installation Guide</h2>

<h3>1. Clone the Repository</h3>
<pre><code>git clone https://github.com/your-username/TalentScout-Chatbot.git
cd TalentScout-Chatbot</code></pre>

<h3>2. Install Dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>3. Run the Chatbot</h3>
<pre><code>streamlit run app.py</code></pre>
<p>Now, open the provided link in your browser to start using the chatbot!</p>

<h2>How It Works</h2>
<ol>
    <li><strong>Collects candidate details</strong> (name, email, experience, tech stack).</li>
    <li><strong>Generates 5 technical questions</strong> based on the tech stack using Hugging Face Falcon-7B.</li>
    <li><strong>Supports multiple languages</strong> by translating questions using Google Translate API.</li>
    <li><strong>Analyzes candidate sentiment</strong> on feedback responses using TextBlob.</li>
</ol>

<h2>Future Improvements</h2>
<ul>
    <li>Integrate <strong>advanced AI models</strong> for more accurate sentiment analysis.</li>
    <li>Add support for <strong>more languages and dialects</strong>.</li>
    <li>Develop a <strong>candidate dashboard</strong> for recruiters to manage responses.</li>
    <li>Enhance the chatbot's ability to handle <strong>follow-up questions</strong> and maintain context.</li>
    <li>Deploy the chatbot on a <strong>cloud platform</strong> for wider accessibility.</li>
</ul>

<h2>Contributing</h2>
<p>If you would like to contribute to this project, feel free to open issues or submit pull requests. Please follow the contribution guidelines and ensure your changes are well-documented. Contributions to improving the chatbot’s functionality, UI/UX, and multilingual support are highly encouraged!</p>
