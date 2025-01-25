const studyBuddies = [
  {
    name: "Alice Johnson",
    subject: "Computer Science",
    available_time: "Evening",
    preferred_place: "Library",
  },
  {
    name: "Bob Smith",
    subject: "Math",
    available_time: "Afternoon",
    preferred_place: "Cafe",
  },
  {
    name: "Charlie Brown",
    subject: "Science",
    available_time: "Morning",
    preferred_place: "Online",
  },
  {
    name: "Diana Rodriguez",
    subject: "Computer Science",
    available_time: "Morning",
    preferred_place: "Campus",
  },
  {
    name: "Ethan Kim",
    subject: "Math",
    available_time: "Evening",
    preferred_place: "Library",
  },
  {
    name: "Fiona Lee",
    subject: "Science",
    available_time: "Afternoon",
    preferred_place: "Cafe",
  },
  {
    name: "George Wang",
    subject: "Computer Science",
    available_time: "Afternoon",
    preferred_place: "Online",
  },
];
document
  .getElementById("register-form")
  .addEventListener("submit", async (e) => {
    e.preventDefault();
    const userData = {
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      password: document.getElementById("password").value,
      subject: document.getElementById("subject").value,
      available_time: document.getElementById("available-time").value,
      preferred_place: document.getElementById("preferred-place").value,
      study_style: document.getElementById("study-style").value,
    };

    try {
      const response = await fetch("http://localhost:5000/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      });
      const result = await response.json();
      alert(result.message);
    } catch (error) {
      console.error("Registration error:", error);
    }
  });

document
  .getElementById("buddy-search")
  .addEventListener("submit", async (e) => {
    e.preventDefault();
    const subject = document.getElementById("search-subject").value;
    const time = document.getElementById("search-time").value;
    const place = document.getElementById("search-place").value;

    const params = new URLSearchParams({
      subject,
      available_time: time,
      preferred_place: place,
    });

    try {
      const response = await fetch(
        `http://localhost:5000/find_buddies?${params}`
      );
      const buddies = await response.json();

      const resultsDiv = document.getElementById("buddies-results");
      resultsDiv.innerHTML = "";

      buddies.forEach((buddy) => {
        const buddyCard = document.createElement("div");
        buddyCard.classList.add("buddy-card");
        buddyCard.innerHTML = `
                <h3>${buddy.name}</h3>
                <p>Subject: ${buddy.subject}</p>
                <p>Available Time: ${buddy.available_time}</p>
                <p>Preferred Place: ${buddy.preferred_place}</p>
                <p>Study Style: ${buddy.study_style}</p>
            `;
        resultsDiv.appendChild(buddyCard);
      });
    } catch (error) {
      console.error("Search error:", error);
    }
  });
