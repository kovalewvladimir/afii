$(document).ready(function(){
  var btnCategory = $('ul#categotyMenu > li');
  var btnSubCategory = btnCategory.filter('.sub-item');
  btnSubCategory.hide();
  var tableTr = $('tr[data-category-id]');
  btnCategory.click(function(){
    var btnCategoryId = Number($(this).attr('data-category-id'));
    if (isNaN(btnCategoryId)) {
      var i = $(this).next();
      while (i.hasClass('sub-item')){
        i.toggle('fast');
        i = i.next();
      }
    } else {
      var filterTableTr = tableTr.filter(function(){
        return (btnCategoryId === 0) || (Number($(this).attr('data-category-id')) === btnCategoryId);
      });
      tableTr.hide();
      filterTableTr.show();

      btnCategory.removeClass('active');
      $(this).addClass('active');
    }
  });
});