document.getElementById('add-to-cart').addEventListener('click', function () {

    var pk = this.value;
    $.ajax({
        url: '/user/cart-item/',
        data: {'pk': pk},
        dataType: 'json',
        method: 'GET',
    });

    var values = [];
    var cart_items = localStorage.getItem('cart_item');
    if (cart_items == null) {
        values.push(pk);
        localStorage.setItem('cart_item', values);
    } else {
        values.push(localStorage.getItem('cart_item'));
        values.push(pk);
        localStorage.setItem('cart_item', values);
        console.log(localStorage.getItem('cart_item'))
    }
});


function changeQuantity(id, actionType) {
    $.ajax({
        url: '/user/change-quantity/',
        data: {'pk': id, 'action': actionType},
        dataType: 'json',
        method: 'GET',
        success: function () {
            window.location.reload();
        }
    });
}

function removeCartItem(id) {
    $.ajax({
        url: '/user/remove-cart-item/',
        data: {'pk': id},
        dataType: 'json',
        method: 'GET',
        success: function () {
            window.location.reload();
        }
    });
}