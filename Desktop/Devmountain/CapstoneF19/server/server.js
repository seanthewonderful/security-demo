const express = require('express')
const cors = require('cors')

const app = express()

app.use(express.json())
app.use(cors())



app.listen(9009, () => console.log(`Fussing on port 9009`))