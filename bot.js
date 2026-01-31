const { Telegraf } = require('telegraf');

// 🔹 Mets ton token ici directement
const BOT_TOKEN = '8028706978:AAFiOP9Cm3I4mBrraPFk7LPsgN1-MIRJCI0';

if (!BOT_TOKEN) {
  console.error("⚠️ Erreur : tu dois définir BOT_TOKEN !");
  process.exit(1);
}

const bot = new Telegraf(BOT_TOKEN);

// Tableau des 10 réactions
const reactions = ['🔥','❤️','👍','😂','😮','😢','👏','💯','🤖','🚀'];

// Quand un message est publié dans le canal
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

// Lancer le bot
bot.launch().then(() => console.log('Bot démarré et prêt !'));

// Arrêt propre
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));