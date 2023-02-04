// // function handleh1Click() {
// //   console.log("h1 was clicked");
// //   h1.style.color = "grey";
// //   //h1.style.color = "blue";
// // }
// // function handleMouseEnter() {
//   //   //console.log("mouse is here!");
//   //   h1.innerText = "mouse is here!";
//   // }
//   // function handleMouseLeave() {
//     //   //console.log("mouse is gone!");
//     //   h1.innerText = "mouse is gone!";
//     // }
//     // function handleWindowResize() {
//       //   document.body.style.backgroundColor = "tomato";
//       // }
//       // function handleWindowCopy() {
//         //   alert("copied!");
//         // }
//         // function handleWindowOffline() {
//           //   alert("SOS no WIFI");
//           // }
//           // function handleWindowOnline() {
//             //   alert("All Good!");
// // }

// // // h1.addEventListener("click", handleh1Click);
// // // h1.addEventListener("mouseenter", handleMouseEnter);
// // // h1.addEventListener("mouseleave", handleMouseLeave);

// // // window.addEventListener("resize", handleWindowResize);
// // // window.addEventListener("copy", handleWindowCopy);
// // // window.addEventListener("offline", handleWindowOffline);
// // // window.addEventListener("online", handleWindowOnline);

// const h1 = document.querySelector(".first h1")

// function handleTitleClick() {
//   const clickedClass = "clicked";
//   h1.classList.toggle("clicked");
// }

// h1.addEventListener("click", handleTitleClick);

const loginForm = document.querySelector("#login-form");
const loginInput = loginForm.querySelector("input");
const greeting = document.querySelector("#greeting");
const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";
const savedUsername = localStorage.getItem(USERNAME_KEY);

function paintGreetings(event) {
  greeting.classList.remove(HIDDEN_CLASSNAME);
  greeting.innerText = `Hello, ${event}`;
}

function onLoginSubmit(event) {
  event.preventDefault();
  loginForm.classList.add(HIDDEN_CLASSNAME);
  const username = loginInput.value;
  localStorage.setItem(USERNAME_KEY, username);
  paintGreetings(username);
}

if (savedUsername === null) {
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", onLoginSubmit);
} else {
  paintGreetings(savedUsername);
}
