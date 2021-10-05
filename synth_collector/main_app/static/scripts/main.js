$(".navbar-burger").click(function () {
  // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
  $(".navbar-burger").toggleClass("is-active");
  $(".navbar-menu").toggleClass("is-active has-background-dark");
});

$('.modal').click(function () {
  //toggle modal
  $(".modal").toggleClass("is-active");
})