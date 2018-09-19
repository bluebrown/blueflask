function toggleHero(){

  let toggler = document.getElementById('hero-toggler');

  toggler.classList.toggle('is-on');

  if (toggler.classList.contains('is-on')){
    $('.hero').slideDown(500);

  } else {
      $('.hero').slideUp(500);
    };

};
