// password match function
document.getElementById('id_password2').addEventListener('keyup', checkPassword);
document.getElementById('id_password1').addEventListener('keyup', checkPassword);

function checkPassword() {
    pass1 = document.getElementById('id_password1').value;
    pass2 = document.getElementById('id_password2').value;
    var message = document.getElementById('massage');
    if (pass1 === pass2) {
        message.style.color = 'green';
        message.innerHTML = 'password matched';
        document.getElementById('createButton').disabled = false;
    } else {
        message.style.color = 'red';
        message.innerHTML = 'password not matched';
        document.getElementById('createButton').disabled = true;
    }
}
