
exports.extractTopics = async (summary) => {
    let data = {
        "inputs": summary
    }
    //console.log(data)
    
    const response = await fetch(
        "https://api-inference.huggingface.co/models/transformer3/H2-keywordextractor",
        {
            headers: {Authorization: `Bearer ${process.env.API_KEY}`},
            method: "POST",
            body: JSON.stringify(data),
        }
    );
    let result = await response.json();
    // response is of type: { "summary_text":"..." }, convert to trimmed array
    result = result[0]["summary_text"].split(", ").map(each => each.trim())
    
    return result
};