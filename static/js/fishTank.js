$( document ).ready(function() {
  const fishTank= document.getElementById("fishtank");
  const bodyEl = document.getElementsByTagName("body");
  fishTank.width = bodyEl[0].clientWidth;
  fishTank.height = bodyEl[0].clientHeight;
});