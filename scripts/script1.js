var swiper = new Swiper(".slide-content", {
    slidesPerView: 3,
    spaceBetween: 50,
    loop: true,
    centerSlide: 'true',
    fade: 'true',
    grabCursor: 'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        520: {
            slidesPerView: 2,
        },
        950: {
            slidesPerView: 3,
        },
    },
  });
  var swiper = new Swiper(".mySwiper", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
  function changeContent () {
    var div1 = document.getElementById('slide-1');
    var div2 = document.getElementById('slide-2');
    var div3 = document.getElementById('slide-3');
    
    div1.style.display = 'none';
    div2.style.display = 'none';
    div3.style.display = 'block';
 }

 function changeContent (num = 1) {
  console.log(num);
  var div1 = document.getElementById('slide-1');
  var div2 = document.getElementById('slide-2');
  var div3 = document.getElementById('slide-3');



     switch(num) {
        case 1:
           div1.style.display = 'block';
           div2.style.display = 'none';
           div3.style.display = 'none';
          break;
        case 2:
           div1.style.display = 'none';
           div2.style.display = 'block';
           div3.style.display = 'none';
          break;
        case 3:
           div1.style.display = 'none';
           div2.style.display = 'none';
           div3.style.display = 'block';
           break;
     }
}