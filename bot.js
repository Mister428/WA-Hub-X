const { Telegraf } = require('telegraf');
const express = require('express');

// 🔹 Mets ton token ici directement
const BOT_TOKEN = '8028706978:AAFiOP9Cm3I4mBrraPFk7LPsgN1-MIRJCI0';

if (!BOT_TOKEN) {
  console.error("⚠️ Erreur : tu dois définir BOT_TOKEN !");
  process.exit(1);
}

const bot = new Telegraf(BOT_TOKEN);
const app = express();

// Middleware pour parser le JSON
app.use(express.json());

// Tableau des 10 réactions
const reactions = ['🔥','❤️','👍','😂','😮','😢','👏','💯','🤖','🚀'];

// Configurer le webhook pour Telegram
const PORT = process.env.PORT || 3000;
const RENDER_EXTERNAL_URL = process.env.RENDER_EXTERNAL_URL;

// Si on est sur Render, on utilise l'URL fournie
if (process.env.RENDER) {
  const webhookPath = `/webhook/${BOT_TOKEN}`;
  const webhookUrl = `${RENDER_EXTERNAL_URL}${webhookPath}`;
  
  // Configurer le webhook
  app.use(await bot.createWebhook({ domain: webhookUrl }));
  
  console.log(`Webhook configuré sur: ${webhookUrl}`);
} else {
  // Mode développement local avec polling
  bot.launch().then(() => console.log('Bot démarré en mode polling !'));
}

// Route pour vérifier que le bot est en ligne
app.get('/', (req, res) => {
  res.send('Bot Telegram en ligne ✅');
});

// Route pour recevoir les webhooks de Telegram
app.post(`/webhook/${BOT_TOKEN}`, (req, res) => {
  bot.handleUpdate(req.body, res);
});

// Gérer les messages du canal
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

// Démarrer le serveur
app.listen(PORT, () => {
  console.log(`Serveur web démarré sur le port ${PORT}`);
});

// Arrêt propre
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));