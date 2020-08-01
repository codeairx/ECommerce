document.getElementById('id_product_master_category').addEventListener('click', filterSubCat);


function filterSubCat() {
    let obj = document.getElementById('id_product_sub_category');
    obj.innerHTML = '';

    let pk = document.getElementById('id_product_master_category').value;
    console.log(pk);
    var http = new XMLHttpRequest();
    http.open('GET', '/product/sub-cat-filter/?pk=' + pk, true);
    http.send();
    http.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var value = JSON.parse(http.response);
            for (let item = 0; item < value.subcat.length; item++) {
                obj.innerHTML += `<option value="${value.subcat[item].id}" selected="">${value.subcat[item].subcategory_name}</option>`;
            }
        }
    }
}