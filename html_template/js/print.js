$(document).ready(function(){
  $('#qrcodeCanvas').qrcode({
    text   : location.href,
    width  : 128,
    height : 128
  });
  var canvas = document.querySelector('#qrcodeCanvas canvas');
  $('#qrcodeImg').attr("src", canvas.toDataURL());

  $('#btnQRcode').click(function (){
    $('#page').print();
  });
});

function updateImgQrcode(size){
  
}