from transformers import pipeline
import requests

# Huggingface keyword extractor model 
# https://huggingface.co/transformer3/H2-keywordextractor
pipe = pipeline("summarization", model="transformer3/H2-keywordextractor")

sample = "The Reddit post in question involves a user seeking advice on whether to use Blazor/Razor Pages or Vue for personal projects, given their background in C# and .NET for backend development. The user ultimately decides to learn TypeScript and Vue, aiming to broaden their knowledge base and because they need TypeScript for some Firebase work. Comments vary widely in their recommendations, reflecting personal preferences and experiences with different frameworks. Some argue in favor of Blazor for its convenience in using C# across full-stack development and the growing ecosystem around WebAssembly (Wasm), suggesting it's a more universal approach. Others recommend Vue, pointing out its value in learning front-end development and the potential ease of transitioning to React in the future. React is also mentioned as a popular choice among major companies, including Microsoft. Angular is praised by some for its suitability in large team environments and its comprehensive nature, which could reduce decision fatigue, though it's noted for having a steep learning curve compared to Vue. Svelte is mentioned as an alternative but considered too niche for someone looking to expand their knowledge broadly. The discussion also touches on the importance of familiarizing oneself with concepts like managing state and reactive programming early on. Server-side and WebAssembly versions of Blazor are debated, with some highlighting the practical advantages and scalability of server-side Blazor, whereas others criticize Blazor for not being a mature ecosystem compared to more established JavaScript frameworks. Overall, the thread illustrates the diverse opinions developers have regarding front-end frameworks and emphasizes the importance of choosing a technology not only based on its current popularity or familiarity but also on how it aligns with an individual's learning goals, project requirements, and the broader trends in web development."
sample2 = "The original Reddit post inquiries about the best way to learn Python for free with minimal coding experience. Various members of the Reddit community shared resources, strategies, and personal experiences to assist in learning Python effectively. A popular recommendation is Cory Schafer's YouTube videos for their clarity in explaining basic concepts. Additionally, the book Python Crash Course by Eric Matthes is suggested for beginners. Other users emphasized practical application through project-building after learning the basics, highlighting the value of learning by doing. MOOC by the University of Helsinki is recommended for its University-level course material on Python, which is free and practice-oriented. Harvard's CS50's Python course is another advocated resource, providing structured learning material. Resources like Automate the Boring Stuff with Python are mentioned for offering free access to learning Python through automated tasks. SoloLearn and futurecoder.io are proposed for interactive learning, while services like OpenAI's ChatGPT and Jupyter Notebook are mentioned for practicing code implementation. Some users discourage passive learning through endless tutorials, urging instead to engage in projects to consolidate learning. The consensus is clear: a mix of theoretical understanding and practical application, supported by consistent effort, is key to effectively learning Python for free."

topics = pipe(sample)
topics = list(map(str.strip,topics[0]['summary_text'].split(', ')))


# https://en.wikipedia.org/w/api.php?action=help&modules=query%2Bsearch
def get_wikipedia_link(topic):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": topic,
        "srlimit": 1
    }
    
    response = requests.get(base_url, params=params).json()
    page_id = response['query']['search'][0]['pageid']
    link = f"https://en.wikipedia.org/?curid={page_id}"
    return link

result = {}
for topic in topics:
    result[topic] = get_wikipedia_link(topic)
print(result)

