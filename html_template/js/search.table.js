/*************************************************************

** Поиск в таблице

  <!-- Поле для поиска -->
  <!-- <ul data-search-table-id="id связанной таблицы"></u> -->
  <div class="input-group">
    <input type="search" id="!!!!!!!!!!!!!!!!!!!!!!!!!searchPrinter" class="form-control" placeholder="Поиск...">
    <span class="input-group-addon"></span>
    <div class="input-group-btn">
      <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" tabindex="-1"><span class="caret"></span></button>
      <ul class="dropdown-menu pull-right" role="menu" data-search-table-id="idTABLE"></ul>
    </div>
  </div>
  ...
  <table id="idTABLE">
    <thead> <!-- Заголовок таблицы -->
      <tr>
        ...
        <th>...</th>
        ...
      </tr>
    </thead>
    <tbody> <!-- Тело таблицы -->
      ...
      <tr>
        ...
        <td>...</td>
        ...
      </tr>
      ...
    </tbody>
  </table>

*************************************************************/

$(document).ready(function(){

  function setTextSpanAddon(element, text){
    element.parents('div.input-group').children('span.input-group-addon').text(text)
  }

  var functionSearch = function search(eventObj){
    var searchText = this.value;
    eventObj.data.tableTD.each(function (index, element){
      var $this = $(this);
      if ($this.text().toLowerCase().indexOf(searchText.toLowerCase()) != -1)
        $this.parent().show();
      else
        $this.parent().hide();
    });
  }


  var allUlSearch = $('ul[data-search-table-id]');

  allUlSearch.each(function () {
    var $thisUL = $(this);
    var idTable = $thisUL.attr('data-search-table-id');
    var tableTh = $('#' + idTable + ' thead tr th');
    tableTh.each(function (index){
      var $thisTH = $(this);
      var textTH  = 'по ' + $thisTH.text().toLocaleLowerCase();
      $thisUL.append('<li data-table-col="' + (index + 1) + '"><a>' + textTH + '</a></li>');
      if (index == 0) {
        setTextSpanAddon($thisUL, textTH);
      }
    });
    var inputSearch = $thisUL.parents('div.input-group').children('input[type="search"]');
    // TODO:
    inputSearch.click({tableTD: $('#' + idTable + ' td:nth-child(1)')}, functionSearch);
  });



  var allLIULSearch = allUlSearch.children('li[data-table-col]');

  allLIULSearch.click(function (){
    var $thisLI = $(this);
    setTextSpanAddon($thisLI, $thisLI.text());

  });





  var a = function test(eventObj){
    console.log(eventObj.data.a);
    console.log(eventObj.data.b);
  }




  //var searchPrinter = $('#searchPrinter');
  //var tblPrintrer   = $('#tblPrinter');
 // var td1           = $('#tblPrinter td:nth-child(1)');

  //searchPrinter.keyup({a:1,b:'2'},a);

  //searchPrinter.keyup();
});
