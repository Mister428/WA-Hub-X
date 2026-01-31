// 🔹 Charger dotenv si présent (local)
try {
  require('dotenv').config();
} catch (err) {
  console.log("Pas de fichier .env détecté, utilisation des variables d'environnement de Render.");
}

const { Telegraf } = require('telegraf');

// 🔹 Récupérer le token depuis .env ou Render
const BOT_TOKEN = process.env.BOT_TOKEN;
if (!BOT_TOKEN) {
  console.error("⚠️ Erreur : tu dois définir BOT_TOKEN dans les variables d'environnement !");
  process.exit(1);
}

const bot = new Telegraf(BOT_TOKEN);

// 🔹 Tableau des 10 réactions
const reactions = ['🔥','❤️','👍','😂','😮','😢','👏','💯','🤖','🚀'];

// 🔹 Quand un message est publié dans le canal
bot.on('channel_post', async (ctx) => {
  const messageId = ctx.channelPost.message_id;
  const chatId = ctx.channelPost.chat.id;

  console.log(`Nouveau post détecté : ${messageId} dans le canal ${chatId}`);

  for (const emoji of reactions) {
    try {
      await ctx.telegram.sendMessage(chatId, emoji, {
        reply_to_message_id: messageId
      });
    } catch (err) {
      console.error(`Erreur pour l'emoji ${emoji} :`, err.description || err);
    }
  }
});

// 🔹 Lancer le bot
bot.launch().then(() => console.log('Bot démarré et prêt !'));

// 🔹 Arrêt propre
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));