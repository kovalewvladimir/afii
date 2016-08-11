// Обновить QRcode
function updateImgQrcode(size, img){
  var qrcodeDiv = document.createElement('div');
  $(qrcodeDiv).qrcode({
    text   : location.href,
    width  : size,
    height : size
  });
  var qrcodeCanvas = qrcodeDiv.children[0];
  $(img).attr('src', qrcodeCanvas.toDataURL());
}

$(document).ready(function(){
  
  updateImgQrcode(128, '#qrcodeImg');

  var page = $('#page');
  var print = $('#print');
  
  // onChange изменение ширины страницы
  $('#widthPage').change(function (){
    page.css('width', this.value + 'mm');
  });
  
  // onChange изменение высоты страницы
  $('#heightPage').change(function (){
    page.css('height', this.value + 'mm');
  });
  
  // onChange изменение размера QRcode
  $('#sizeQRcode').change(function (){
    updateImgQrcode(this.value, '#qrcodeImg');
  });
  
  // onClick вкл/выкл рамки QRcode
  $('#isBorderQRcode').click(function (){
      print.css('border', this.checked ? '0.5mm solid #000':'none');
  });
  
  // onClick кнопка открытия модального окна "QR code"
  $('#btnQRcode').click(function (){
    $('#page').print();
  });
});