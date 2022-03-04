const users = []
const bcryptjs = require("bcryptjs")

module.exports = {
    login: (req, res) => {
      console.log('Logging In User')
      console.log(req.body)
      const { username, password } = req.body

      for (let i = 0; i < users.length; i++) {
        const existingPW = bcryptjs.compareSync(password, users[i].pinHash)
        if (users[i].username === username && (existingPW)) {
          let securedUser = {...users[i]}
          delete securedUser.pinHash
          res.status(200).send(securedUser)
        }else {
          res.status(400).send("User not found.")
        }
      }
    },
    register: (req, res) => {
        console.log('Registering User')
        console.log(req.body)
        const { username, password, email, firstName, lastName } = req.body

        const salt = bcryptjs.genSaltSync(5)
        const pinHash = bcryptjs.hashSync(password, salt)
        
        let userObj = {
          pinHash,
          username,
          email,
          firstName,
          lastName
        }
        users.push(userObj)

        let securedUser = {...userObj}
        delete securedUser.pinHash
        return res.status(200).send(securedUser)
    }
}