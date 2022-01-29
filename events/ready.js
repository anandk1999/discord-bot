const config = require("../config.json");

module.exports = (client) => {
    console.log(`Logged in as ${client.user.tag}!`);

    /*client.user.setActivity(`Esports | ${config.version}`, {
        type: "PLAYING"
    });*/

    /*client.user.setActivity(`Rutgers Esports`, {
        type: "WATCHING"
    });*/

    /*client.user.setActivity(`to Rutgers Esports`, {
        type: "LISTENING"
    });*/

    client.user.setActivity(`at the Esports Center`, {
        type: "STREAMING",
        url: "https://www.twitch.tv/rutgersesports"
    });
};