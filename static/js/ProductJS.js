function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');


$('input[name=live_checkbox]').change(
    function () {
        if (this.checked) {
            $.ajax({
                url: '/product/product-live/',
                headers: {"X-CSRFToken": csrftoken},
                method: 'POST',
                dataType: 'json',
                data: {'pk': this.value, 'checked': true},
            })
        } else {
            $.ajax({
                url: '/product/product-live/',
                headers: {"X-CSRFToken": csrftoken},
                method: 'POST',
                dataType: 'json',
                data: {'pk': this.value, 'checked': false},
            })
        }
    }
);