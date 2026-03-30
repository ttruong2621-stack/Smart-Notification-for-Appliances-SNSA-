//script to handle UI update

const BACKEND_URL = " https://ancient-wood-c83b.snsa-app.workers.dev";

async function getLatestEvent(){
    try{const response = await fetch(`${BACKEND_URL}/latest-event`);
    const data = await response.json();

    console.log("Received:", data);
    
    //if there's an event, update the UI
    if(data && data.event) {
        const el = document.getElementById("statusText");

        el.textContent = `${data.soundName} detected`;
        el.style.color = "red";
    }
    }
    catch (error) {
        console.error("Error fetching latest event:", error);
    }
}

async function sendTestEvent(){
    const eventMessage = {
        deviceId: "snsa-001",
        event: "sound_detected",
        soundName: "Washer Done",
        timestamp: new Date().toISOString()
    };

    await fetch(`${BACKEND_URL}/event`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(eventMessage)
        
    });
}

//call every 2 seconds
setInterval(getLatestEvent, 2000);