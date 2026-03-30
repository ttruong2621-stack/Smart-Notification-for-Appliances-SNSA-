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

//call every 2 seconds
setInterval(getLatestEvent, 2000);