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

    // bootstrap событие show modal ModalAddCategory
    $('#ModalAddCategory').on('show.bs.modal', function (e) {
        var activeItem = $('.list-group-item.sub-item.active');
        var is_base = ! activeItem.hasClass('sub-item');
        var id_is_base = $('#id_is_base');
        var id_base_category = $('#id_base_category');

        if (is_base) {
            id_is_base.prop("checked", true);
        } else {
            id_is_base.removeAttr('checked');
            var data_category_id = $(activeItem.prevAll().not('.sub-item')[0]).attr('data-base-category-id');
            id_base_category.val(data_category_id);
        }
    })

});

// отправка ajax запроса
function sendFormAddCategory() {
    var msg = $('#formAddCategory').serialize();
        $.ajax({
            type: 'POST',
            url: 'add_category',
            data: msg,
            success: function(data) {
                $('#divFormAddCategory').html(data);
            },
            error: function(xhr, str){
                alert(xhr.responseText);
            }
        });
}