const qoutes = [
  {
    qoute: "A good beginning makes a good ending.",
    author: "English Sentence",
  },
  {
    qoute: "For I can raise no money by vile means.",
    author: "William Shakespeare",
  },
  {
    qoute: "You can't blame gravity for falling in love.",
    author: "Albert Einstein",
  },
  {
    qoute: "Apparently three is nothing that cannot happen today.",
    author: "Mark Twain",
  },
  {
    qoute: "Reality is merely an illusion, albeit a very persistent one.",
    author: "Albert Einstein",
  },
  {
    qoute: "Truth is the most valuable thing we have. Let us economize it.",
    author: "Mark Twain",
  },
  {
    qoute:
      "If tou can't explain it simply, you don't understand it well enough.",
    author: "Albert Einstein",
  },
  {
    qoute: "Never do anything against conscience even if the state demands it.",
    author: "Albertinstein",
  },
  {
    qoute: "A clever man commits no minor blunders",
    author: "Johann Wolfgang Von Goethe",
  },
  {
    qoute: "You don't know what you've got until you've lost it.",
    author: "proverb",
  },
];

const qoute = document.querySelector(".first strong:first-child");
const author = document.querySelector(".second strong:first-child");

const TodaysQoute = qoutes[Math.floor(Math.random() * qoutes.length)];
console.log(TodaysQoute);
// TodaysQoute.qoute = q;
// TodaysQoute.author = a;

qoute.innerText = TodaysQoute.qoute;
author.innerText = TodaysQoute.author;

console.log(qoute.innnerText);
