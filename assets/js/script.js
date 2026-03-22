function showSection(id){
    document.querySelectorAll('main section').forEach(s => s.classList.remove('active'));
    document.getElementById(id).classList.add('active');
}

async function sendCommand(cmd){
    let url = document.getElementById('url')?.value || '';
    let responseDiv = document.getElementById('response');

    try{
        let res = await fetch(`bot_api.php?cmd=${cmd}&url=${encodeURIComponent(url)}`);
        let data = await res.text();
        responseDiv.innerHTML = data;
    }catch(e){
        responseDiv.innerHTML = "Error sending command!";
    }
}

document.getElementById('musicForm')?.addEventListener('submit', e=>{
    e.preventDefault();
    sendCommand('play');
});
