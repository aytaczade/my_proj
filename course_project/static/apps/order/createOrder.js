// to get selected radio input for wagon type
function getSelected(name) {
    const radioButtons = document.getElementsByName(name);
    let selectedValue = '';
    for (let i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            selectedValue = radioButtons[i].value;
            break;
        }
    }
    return selectedValue;
}


function setChecked(input, name) {
    let radioButtons = document.getElementsByName(name);
    input.setAttribute('checked', 'checked');
    for (let i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].value !== input.value) {
            radioButtons[i].removeAttribute('checked');
        }
    }
}




function createOrder() {
    $.ajax({
      method: "POST",
      url: order_create_url,
      headers: { "X-CSRFToken": csrftoken_ },
      data: {
        product: product_id,
        product_qty: document.getElementById("product-qty").value,
        size: getSelected('size'),
        color: getSelected('color'),
      },
      dataType: "json",
      success: function () {
        window.location.reload();
      },
      error: function(data) {
        console.log('error cixdiiiii', data);
      }
    });
  }


 