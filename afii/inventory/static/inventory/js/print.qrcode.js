// Обновить QRcode Img
function updateImgQrcode(size, img){
  var qrcodeDiv = document.createElement('div');
  $(qrcodeDiv).qrcode({
    text   : 'n16.zc.com.ru:16025' + location.pathname,
    width  : size,
    height : size
  });
  var qrcodeCanvas = qrcodeDiv.children[0];
  $(img).attr('src', qrcodeCanvas.toDataURL());
}

$(document).ready(function(){

  var pageQRcode        = $('#pageQRcode');
  var printQRcode       = $('.printQRcode');
  var titleQRcode       = $('.titleQRcode');
  var ipQRcode          = $('.ipQRcode');
  var printQRcodeCount1 = $('#printQRcodeCount1');
  var printQRcodeCount2 = $('#printQRcodeCount2');

  var widthPage          = $('#widthPage');
  var heightPage         = $('#heightPage');
  var sizeQRcode         = $('#sizeQRcode');
  var countQRcode        = $('#countQRcode');
  var isBorderQRcode     = $('#isBorderQRcode');
  var borderTypeQRcode   = $('#borderTypeQRcode');
  var isTitleQRcode      = $('#isTitleQRcode');
  var isIpQRcode         = $('#isIpQRcode');
  var titleSizeQRcode    = $('#titleSizeQRcode');
  var ipSizeQRcode       = $('#ipSizeQRcode');
  var btnQRcodePrint     = $('#btnQRcodePrint');
  var paddingPageQRcode  = $('#paddingPageQRcode');
  var paddingPrintQRcode = $('#paddingPrintQRcode');

  updateImgQrcode(Number(sizeQRcode.val()), '.imgQRcode');

  /***********************************************************

  ** Обработчики событий

  ***********************************************************/

  // onChange изменение ширины страницы
  widthPage.change(function (){
    pageQRcode.css('width', this.value + 'mm');
  });

  // onChange изменение высоты страницы
  heightPage.change(function (){
    pageQRcode.css('height', this.value + 'mm');
  });

  // onChange изменение размера QRcode
  sizeQRcode.change(function (){
    updateImgQrcode(this.value, '.imgQRcode');
  });

  // onChange изменение кол-во QRcode
  countQRcode.change(function (){
    switch (this.value) {
      case '1':
        printQRcodeCount1.show();
        printQRcodeCount2.hide();
        break;
      case '2':
        printQRcodeCount1.hide();
        printQRcodeCount2.show();
        break;
    }
  });

  // onClick вкл/выкл рамки QRcode
  isBorderQRcode.click(function (){
    if (this.checked){
      borderTypeQRcode.change();
      borderTypeQRcode.removeAttr('disabled');
    } else {
      printQRcode.css('border','none');
      borderTypeQRcode.attr('disabled', true);
    }
  });

  // onChange изменение типа рамки QRcode
  borderTypeQRcode.change(function (){
    printQRcode.css('border', '0.5mm ' + this.value + '#000');
  });

  // onClick вкл/выкл заголовок QRcode
  isTitleQRcode.click(function (){
    if (this.checked) {
      titleQRcode.show();
      titleSizeQRcode.removeAttr('disabled');
    } else {
      titleQRcode.hide();
      titleSizeQRcode.attr('disabled', true);
    }
  });

  // onClick вкл/выкл ip QRcode
  isIpQRcode.click(function (){
    if (this.checked) {
      ipQRcode.show();
      ipQRcode.removeAttr('disabled');
    } else {
      ipQRcode.hide();
      ipQRcode.attr('disabled', true);
    }
  });

  // onChange изменение размера заголовка QRcode
  titleSizeQRcode.change(function (){
    titleQRcode.css('font-size', this.value + 'px');
  });

  // onChange изменение размера ip QRcode
  ipSizeQRcode.change(function (){
    ipQRcode.css('font-size', this.value + 'px');
  });

  // onChange изменение отступа снаружи
  paddingPageQRcode.change(function (){
    pageQRcode.css('padding', this.value + 'mm');
  });

  // onChange изменение отступа внутри
  paddingPrintQRcode.change(function (){
    printQRcode.css('padding', this.value + 'mm');
  });

  // onClick кнопка печати QRcode
  btnQRcodePrint.click(function (){
    pageQRcode.print();
  });
});
