function disableButtons(productID) {
    var specificProductQuantity = parseInt($(`.quantity_of_${productID}`).val());
    var disablePlusButton = specificProductQuantity > 48;
    var disableMinusButton = specificProductQuantity < 2;

    $(`.minus_button_of_${productID}`).prop('disabled', disableMinusButton);
    $(`.plus_button_of_${productID}`).prop('disabled', disablePlusButton);
    
}

var quantityOfProduct = $('.quantity_value');
for(var j = 0; j < quantityOfProduct.length; j++) {
    var productID = $(quantityOfProduct[i]).data('product_id');
    disableButtons(productID);
}

$('.quantity_value').change(function() {
    var productID = $(this).data('product_id');
    disableButtons(productID);
});

$('.add_more').click(function(event) {
    event.preventDefault();
    var productID = $(this).data('product_id');
    var productInput = $(this).closest('.input-group').find('.quantity_value')[0];
    var specificQuantityInput = $(`.input-group-single-${productID} input[name='order_quantity']`);
    var specificProductQuantity = parseInt($(productInput).val());
    
    var newValue = specificProductQuantity + 1;
    $(specificQuantityInput).val(newValue);
    disableButtons(productID);
});

$('.remove_some').click(function(event) {
    event.preventDefault();
    var productID = $(this).data('product_id');
    var productInput = $(this).closest('.input-group').find('.quantity_value')[0];
    var specificQuantityInput = $(`.input-group-single-${productID} input[name='order_quantity']`);
    var specificProductQuantity = parseInt($(productInput).val());

    var newValue = specificProductQuantity - 1;
    $(specificQuantityInput).val(newValue);
    disableButtons(productID);
});