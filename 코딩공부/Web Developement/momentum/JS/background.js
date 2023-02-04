const images = ["0.jpg", "1.jpg", "2.jpg"];

const chosenImage = images[Math.floor(Math.random() * images.length)];

const bgp = document.createElement("img");

bgp.src = `img/${chosenImage}`;

document.body.appendChild(bgp);
