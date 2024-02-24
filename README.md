# Topic Extraction Microservice

A Node.js microservice that utilizes the Hugging Face Inference API with a keyword extraction text2text generation model for extracting topics from a summary of text, and returning the  corresponding Wikipedia links for those topics. The intended purpose is to provide contextual reference to a given summary, allowing for expanded understanding on the topics included. 

**Notes of consideration**:
- Summary should be 200 words minimum to ensure keyword extraction has enough content to pull from.
- It's designed to return the closest match when searching WikiPedia for topics, so if certain terms such as names of individuals, or vague terms like 'managing state', the resulting wiki link is likely to reference an incorrect topic. 
- Future work will be to match topics with wiki-page's topic header to try and capture mismatches.

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

Send a POST request to `/api/context` with a JSON body containing summary text. **Ensure that the summary is 200 words minimum!**:

```bash
{
    "summary: "Your summary text here..."
}
```

The service will return a JSON object with extracted topics as keys and corresponding Wikipedia links as values:

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

## UML Diagram: Communication Contract

![Lucidchart Diagram](https://github.com/LaUrrego/topic-extraction/blob/main/images/cs361%20Microservice%20Communication%20Contract.png?raw=true)


## Structure

- src/controllers/: Contains controller that handles incoming HTTP requests.
- src/services/: Services for interacting with the Hugging Face and Wikipedia APIs.
- src/routes/: Defines API routes.
- src/app.js: Sets up the Express application.
- server.js: Entry point of the application.

## Testing with Visual Studio Code and the REST Client extension

Included is a test file to be used with Visual Studio Code's [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension by Huachao Mao. Before using, make sure you install the extension. 

Input the port number in the provided variable at the top of the page:

```bash
@port = XXXX
```

and use the two samples to test the API's response. To create your own test, simple copy the POST endpoint, protocol, and header to a new line (making sure that the "Content-type" header is immediately following the POST line), and enter your summary into the JSON as a value to the "summary" key. 

Make sure that your summary string is in **double quotes**, and if there are any quotes within the summary itself, make them **escaped double quotes** to ensure it parses correctly. You can copy and past the below template as well:

```bash
### Request X: <Your Title here>
POST http://localhost:{{port}}/api/context HTTP/1.1
Content-Type: application/json

{
    "summary": "<Your summary here...>"
}

```

# Acknowledgments
- Hugging Face for the amazing serverless Inference API with it's specialized running capacity, and [this](https://huggingface.co/transformer3/H2-keywordextractor?text=I+love+AutoTrain+%F0%9F%A4%97.) wonderful community model in paricular
- Wikipedia for providing a wealth of information accessible via [API](https://en.wikipedia.org/w/api.php?action=help&modules=query%2Bsearch)