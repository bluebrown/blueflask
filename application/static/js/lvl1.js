function toggleSidebar(){

  let toggler = document.getElementById('sidebar-toggler');

  toggler.classList.toggle('is-on');

  if (toggler.classList.contains('is-on')){
    $('#sidebar').show(300);

  } else {
      $('#sidebar').hide(300);
    };

};
