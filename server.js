const app = require('./src/app');
const PORT = process.env.PORT ;

app.listen(PORT, ()=>{
    console.log(`Microservice running on port http://localhost:${PORT}\n`)
});

