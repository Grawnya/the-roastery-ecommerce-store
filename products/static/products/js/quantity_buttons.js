function disableButtons(ProductID) {
    var specificProductQuantity = parseInt($(`.quantity_of_${ProductID}`).val());
    var disablePlusButton = specificProductQuantity > 48;
    var disableMinusButton = specificProductQuantity < 2;

    $(`#minus_button_of_${ProductID}`).prop('disabled', disableMinusButton);
    $(`#plus_button_of_${ProductID}`).prop('disabled', disablePlusButton);
    
}

var quantityOfProduct = $('.quantity_value');
for(var j = 0; j < quantityOfProduct.length; j++) {
    var ProductID = $(quantityOfProduct[i]).data('product_id');
    disableButtons(ProductID);
}

$('.quantity_value').change(function() {
    var ProductID = $(this).data('product_id');
    disableButtons(ProductID);
});