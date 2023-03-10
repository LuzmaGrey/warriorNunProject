// Fetch the quotes from the JSON file
fetch("quotes.json").then(response => response.json()).then(data => {
    // Get the current date
    const today = new Date().toISOString().slice(0, 10);
  
    // Check if a quote has already been displayed today
    const lastDisplayed = localStorage.getItem("lastDisplayed");
    if (lastDisplayed === today) {
      // If a quote has already been displayed today, use the same one
      const lastQuote = localStorage.getItem("lastQuote");
      document.getElementById("quote").innerHTML = lastQuote;
    } else {
      // If a quote has not been displayed today, pick a random one from the list
      const quoteIndex = Math.floor(Math.random() * data.quotes.length);
      const quote = data.quotes[quoteIndex].text;
      const author = data.quotes[quoteIndex].author;
      const fullQuote = `${quote} - ${author}`;
      document.getElementById("quote").innerHTML = fullQuote;
  
      // Save the current date and displayed quote in local storage
      localStorage.setItem("lastDisplayed", today);
      localStorage.setItem("lastQuote", fullQuote);
    }
  });
  


  /*document.addEventListener( 'DOMContentLoaded', function () {
    new Splide( '#image-carousel', {
      cover      : true,
      heightRatio: 0.5,
    } ).mount();
  } );*/

  let slider = document.querySelector('.slider');
let sliderItems = document.querySelectorAll('.slider-item');
let currentSlide = 0;

function goToSlide(slide) {
  slider.style.transform = 'translateY(-' + (slide * 100) + '%)';
}

function nextSlide() {
  currentSlide++;
  if (currentSlide >= sliderItems.length) {
    currentSlide = 0;
  }
  goToSlide(currentSlide);
}

function prevSlide() {
  currentSlide--;
  if (currentSlide < 0) {
    currentSlide = sliderItems.length - 1;
  }
  goToSlide(currentSlide);
}

let prevButton = document.querySelector('.prev-button');
let nextButton = document.querySelector('.next-button');

prevButton.addEventListener('click', prevSlide);
nextButton.addEventListener('click', nextSlide);


//SOCIAL
