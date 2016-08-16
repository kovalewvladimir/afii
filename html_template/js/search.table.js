/*************************************************************

** Поиск в таблице

*************************************************************/

$(document).ready(function(){

  var searchPrinter = $('#searchPrinter');
  var tblPrintrer   = $('#tblPrinter');
  var td1           = $('#tblPrinter td:nth-child(1)');

  searchPrinter.keyup(function (){
    var searchText = this.value;
    td1.each(function (index, element){
      var $this = $(this);
      if ($this.text().toLowerCase().indexOf(searchText.toLowerCase()) != -1)
        $this.parent().show();
      else
        $this.parent().hide();
    });
  });
});
