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
    
  
  // TODO: Как использовать селекторы jQuery для выделения элементов страницы 
  //       http://ruseller.com/lessons.php?id=682
  
  // TODO: Сортировка 
  //       http://ru.stackoverflow.com/questions/173042/%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B5-%D0%B2-%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%BD%D0%BE%D0%BC-%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BA%D0%B5

  $("#sort").click(function () {
    var mylist = $('#menu');
    var listitems = mylist.children('div').get();
    listitems.sort(function(a, b) {
       var compA = $(a).text().toUpperCase();
       var compB = $(b).text().toUpperCase();
       return (compA < compB) ? -1 : (compA > compB) ? 1 : 0;
    })
    $.each(listitems, function(idx, itm) { mylist.append(itm); });
  });
  
  
  
});