const Discord = require('discord.js'); // you'll have to convert to discord.js-selfbot-v13, I am inexperienced in that area.
const client = new Discord.Client();

const idleTimeout = 30 * 60 * 1000;
let lastMessageTimestamp = Date.now();

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}`);
});

client.on('message', (message) => {
    if (message.author.bot) return;

    lastMessageTimestamp = Date.now();

    client.user.setPresence({ status: 'online' });
});

function checkIdleStatus() {
    const currentTime = Date.now();
    const elapsedTime = currentTime - lastMessageTimestamp;

    if (elapsedTime >= idleTimeout) {
        client.user.setPresence({ status: 'idle' });
    }
}

setInterval(checkIdleStatus, 60 * 1000);

client.login('TOKEN');