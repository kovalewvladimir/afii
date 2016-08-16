/*************************************************************

  ** Сортировка (http://ru.stackoverflow.com/questions/173042)

    <!-- Структура таблицы для сортировки -->
    <table class="..... tableSort">
      <thead> <!-- Заголовок таблицы -->
        <tr>
          ...
          <th><DIV>...</DIV></th>
          ...
        </tr>
      </thead>
      <tbody> <!-- Тело цикла -->
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
  var tableSortTH = $('.tableSort thead tr th');
  var spanCaret = $('<span class="caret"></span>');

  tableSortTH.click(function () {

    // Инициализация переменных
    var thisTH         = this;
    var $thisTH        = $(this);
    var thisTHDiv      = $thisTH.children('div');
    var thisTHDivSpan  = thisTHDiv.children('span');
    var table          = $thisTH.parents('table');
    var tableTH        = table.find('th');
    var tableTHDiv     = tableTH.children('div');
    var tableTHDivSpan = tableTHDiv.children('span');

    var sortingOrder = false;
    var indexSort    = -1;

    // Поиск номера столбца по которому нужно сортировать (indexSort)
    tableTH.each(function (index, element) {
      if (thisTH == element) {
        indexSort = index;
        return false;
      }
    });
    if (indexSort == -1) {
      console.error('Ошибка: не найден столбец сортировки');
      return;
    }
    indexSort++;

    // Добавление значка сортировки (▲ или ▼)
    if (thisTHDivSpan.length == 0){
      tableTHDivSpan.remove();
      tableTHDiv.removeClass('dropup');
      thisTHDiv.append(spanCaret);
      thisTHDiv.addClass('dropup');
    } else {
      if (tableTHDiv.hasClass('dropup')) {
        sortingOrder = true;
        thisTHDiv.removeClass('dropup');
      } else {
        sortingOrder = false;
        thisTHDiv.addClass('dropup');
      }
    }

    // Сортировка элементов table->tbody->tr по столбцу indexSort
    var tbody = table.children('tbody');
    var tr = tbody.children('tr');
    tr.sort(function(a, b) {
      var compA = $(a).children('td:nth-child(' + indexSort + ')').text().toLocaleLowerCase();
      var compB = $(b).children('td:nth-child(' + indexSort + ')').text().toLocaleLowerCase();
      var result = (compA < compB) ? -1 : (compA > compB) ? 1 : 0;
      return (sortingOrder) ?
                            ((compA > compB) ? -1 : (compA < compB) ? 1 : 0) :
                            ((compA < compB) ? -1 : (compA > compB) ? 1 : 0);
    });
    tbody.append(tr);
  });
});
