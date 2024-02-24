# My Microservice

A Node.js microservice that utilizes the Hugging Face Inference API with a keyword extraction text2text generation model for extracting topics from a summary of text, and returning the  corresponding Wikipedia links for those topics. The intended purpose is to provide contextual reference to a given summary, allowing for expanded understanding on the topics included. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. As the project is not currently deployed, it runs on localhost.

### Prerequisites

- Node.js (v14.x or newer recommended)
- npm (comes with Node.js)

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/LaUrrego/topic-extraction.git
cd topic-extraction
```

Then, install the dependencies: 

```bash
npm install
```

Create a `.env` file at the root of the project and add your Hugging Face API key as API_KEY, and desired port number as PORT:

```bash
API_KEY=your_huggingface_api_key
PORT=port
```

### Running the Application

Start the server with:

```bash
npm start
```

The server will start running on `http://localhost:PORT`

## Usage

Send a POST request to `/api/context` with a JSON body containing summary text:

```bash
{
    "summary: "Your summary text here..."
}
```

The service will return a JSON object with topics as keys and corresponding Wikipedia links as values:

```bash
{
    "links": {

        'Blazor/Razor Pages': 'https://en.wikipedia.org/?curid=58847417',
        'Vue': 'https://en.wikipedia.org/?curid=2253304', 
        'TypeScript': 'https://en.wikipedia.org/?curid=8157205', 
        'Firebase': 'https://en.wikipedia.org/?curid=43030141', 
        'WebAssembly': 'https://en.wikipedia.org/?curid=47013794', 
        'Angular': 'https://en.wikipedia.org/?curid=30688804', 
        'Svelte': 'https://en.wikipedia.org/?curid=13864521', 

        }
}
```

## Structure

- src/controllers/: Contains controller that handles incoming HTTP requests.
- src/services/: Services for interacting with the Hugging Face and Wikipedia APIs.
- src/routes/: Defines API routes.
- src/app.js: Sets up the Express application.
- server.js: Entry point of the application.

# Acknowledgments
- Hugging Face for the amazing serverless Inference API with it's specialized running capacity, and [this](https://huggingface.co/transformer3/H2-keywordextractor?text=I+love+AutoTrain+%F0%9F%A4%97.) wonderful community model in paricular
- Wikipedia for providing a wealth of information accessible via [API](https://en.wikipedia.org/w/api.php?action=help&modules=query%2Bsearch)