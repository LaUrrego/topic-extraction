exports.getLinks = async (topics) => {
    // coming as an array   
    const links = {};

    for (const topic of topics) {
        const link = await getWikipediaLink(topic);
        
        // only send back valid topics with links
        if(link) {
            links[topic] = link;
        };
    };
    // console.log(links);
    return links;
};

// Wikipedia API source: # https://en.wikipedia.org/w/api.php?action=help&modules=query%2Bsearch
const getWikipediaLink = async (topic) => {
    const base_url = "https://en.wikipedia.org/w/api.php";
    // convert to URL param formatted object
    const params = new URLSearchParams({
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": topic,
        "srlimit": 1
    });

    try {
        const response = await fetch(`${base_url}?${params.toString()}`);
        const data = await response.json();
        
        if (data.query.search.length > 0) {
            const pageId = data.query.search[0].pageid;
            return `https://en.wikipedia.org/?curid=${pageId}`;
        } else {
            return null;
        }
    } catch(error) {
        console.error("Error fetching Wikipedia link: ", error);
        return null;
    };
};
