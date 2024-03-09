const huggingFaceService = require('../services/huggingFaceService');
const wikipediaService = require('../services/wikipediaService');

exports.processRequest = async (req, res) => {
    try {
        // obtain summary from body
        
        console.log('Request received ...');
        
        const { summary } = req.body;
        // extract topics from the summary
        const topics = await huggingFaceService.extractTopics(summary);
        // get wikipedia links from topics
        const links = await wikipediaService.getLinks(topics);
        // send

        console.log("Sending response: ");
        console.log({links: links});

        res.status(200).json({links:links});

    } catch(error) {
        console.error(error);
        res.status(500).send('An error processing this summary')
    }
};