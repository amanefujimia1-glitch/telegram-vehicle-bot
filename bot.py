const TelegramBot = require("node-telegram-bot-api")
const fetch = require("node-fetch")

const TOKEN = "8332749106:AAFDlvCKeKGvNZ6uPJLeMQQZN4ASYSBCMrU"
const bot = new TelegramBot(TOKEN, { polling: true })

bot.onText(/\/rc (.+)/, async (msg, match) => {
  const chatId = 1003296016362
  const rc = match[1]

  try {
    const apiUrl = `https://amane.djsouravrooj33.workers.dev/?rc=}`
    const res = await fetch(apiUrl)
    const json = await res.json()

    if (!json.success) {
      bot.sendMessage(chatId, "❌ RC data not found")
      return
    }

    const d = json.data.details

    const message = `
🚗 *Vehicle Details*

🔢 RC: ${json.data.rc}
👤 Owner: ${d["Owner Name"]}
🏍 Model: ${d["Maker Model"]}
⛽ Fuel: ${d["Fuel Type"]}
🏢 RTO: ${d["Registered RTO"]}
📅 Reg Date: ${d["Registration Date"]}

✨ API by @amane_loyal_me
    `

    bot.sendMessage(chatId, message, { parse_mode: "Markdown" })

  } catch (err) {
    bot.sendMessage(chatId, "⚠️ Error fetching data")
  }
})

bot.onText(/\/start/, (msg) => {
  bot.sendMessage(
    msg.chat.id,
    "👋 Welcome!\n\nUse:\n/rc KL43G1669"
  )
})
