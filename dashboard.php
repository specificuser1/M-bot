<?php
// dashboard.php
$bot_status = "Offline";
$token = getenv('DISCORD_TOKEN'); // .env used by Railway
$guild_id = getenv('GUILD_ID');
if($token && $guild_id){
    $bot_status = "Online";
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Music Bot Dashboard</title>
<link rel="stylesheet" href="assets/css/style.css">
<script src="assets/js/script.js" defer></script>
</head>
<body>
<div class="dashboard">
    <header>
        <img src="assets/img/logo.png" alt="Bot Logo" class="logo">
        <h1>Music Bot Dashboard</h1>
        <span class="status <?= $bot_status ?>"><?= $bot_status ?></span>
    </header>
    <nav>
        <ul>
            <li onclick="showSection('home')">Home</li>
            <li onclick="showSection('music')">Music Control</li>
            <li onclick="showSection('about')">About</li>
        </ul>
    </nav>
    <main>
        <section id="home" class="active">
            <h2>Welcome!</h2>
            <p>Manage your private music bot from here.</p>
        </section>
        <section id="music">
            <h2>Music Control</h2>
            <form id="musicForm">
                <input type="text" id="url" placeholder="YouTube URL" required>
                <button type="submit">Play</button>
            </form>
            <button onclick="sendCommand('skip')">Skip</button>
            <button onclick="sendCommand('stop')">Stop</button>
            <button onclick="sendCommand('pause')">Pause</button>
            <button onclick="sendCommand('resume')">Resume</button>
            <div id="response"></div>
        </section>
        <section id="about">
            <h2>About</h2>
            <p>This is a private music bot for your server only.</p>
        </section>
    </main>
</div>
</body>
</html>
