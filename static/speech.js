// Create speech recognition object
var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.lang = 'en-US'; // Set language
recognition.interimResults = false; // Only final results
recognition.maxAlternatives = 1;

// Elements
const micBtn = document.getElementById("micBtn");
const userInput = document.getElementById("user_input");
const textInput = document.getElementById("chat");
const enter = document.getElementById("enter");
const form = document.getElementById("speechForm");
const micBtnIcon = document.getElementById("micBtnIcon")

// If speech doesn't work use text input
enter.addEventListener('click', function(){
        const transcript = textInput.value;
        userInput.value = transcript;
        form.submit(); 
    });

// When speech is detected
recognition.onresult = function(event){
    micBtnIcon.src = "/static/mic-icon.png"
    const last = event.results.length - 1;
    const transcript = event.results[last][0].transcript;
    console.log("User said:", transcript);

    // Put transcript in hidden input and submit form
    userInput.value = transcript;
    form.submit();
};

// When recognition ends
recognition.onspeechend = function(){
    recognition.stop();
};

// Start recognition on button click
micBtn.addEventListener("click", function(){
    micBtnIcon.src = "/static/audio-icon.webp"
    recognition.start();
});

recognition.onerror = function(event) {
    console.error("Speech recognition error:", event.error);
};

let map; // store globally so it doesn’t recreate every time

function findNearestHospital(lat, lon) {
  console.log("Finding nearest hospital for:", lat, lon);

  const mapDiv = document.getElementById('map');
  mapDiv.style.display = "block"; // make it visible

  // If map already exists, reset view instead of reinitializing
  if (map) {
    map.setView([lat, lon], 13);
  } else {
    map = L.map('map').setView([lat, lon], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);
  }

  // Fetch hospitals nearby
  const url = `https://nominatim.openstreetmap.org/search?format=json&q=hospital&addressdetails=1&limit=3&viewbox=${lon-0.05},${lat+0.05},${lon+0.05},${lat-0.05}`;

  fetch(url)
    .then(res => res.json())
    .then(data => {
      console.log("Hospital search results:", data);
      if (data.length === 0) {
        alert("No hospitals found nearby!");
        return;
      }

      const hospital = data[0];
      L.marker([lat, lon]).addTo(map).bindPopup("You are here").openPopup();
      L.marker([hospital.lat, hospital.lon]).addTo(map)
        .bindPopup(`Nearest hospital:<br>${hospital.display_name}`).openPopup();
    })
    .catch(err => console.error("Error fetching hospitals:", err));
}

form.addEventListener("submit", function(e) {
  e.preventDefault(); // prevent page reload

  const userText = document.getElementById("user_input").value;

  // send to Flask route
  fetch('/process', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ user_input: userText })
  })
  .then(response => response.json())
  .then(data => {
    // Update your div instead of reloading page
    document.getElementById("responseDiv").textContent = data.response;

    // Optional: also trigger map/hospital logic here
    // findNearestHospital(userLat, userLon);
  })
  .catch(err => console.error(err));
});
