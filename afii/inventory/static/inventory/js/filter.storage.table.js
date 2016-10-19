$(document).ready(function(){

    // Инициализация переменных
    var btnCategory = $('ul#categotyMenu > li');
    var btnSubCategory = btnCategory.filter('.sub-item');
    var tableTr = $('tr[data-category-id]');

    btnSubCategory.hide();

    // onClick по пункту меню категории
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