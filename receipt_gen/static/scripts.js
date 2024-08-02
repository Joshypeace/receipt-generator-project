document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('receiptForm');

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        
        if (validateForm()) {
            alert('Form submitted successfully!');
            form.submit();
        }
    });

    function validateForm() {
        const receiptNumber = document.getElementById('receipt_number').value;
        const date = document.getElementById('date').value;
        const receivedFrom = document.getElementById('received_from').value;
        const sumAmount = document.getElementById('sum_amount').value;
        const actualAmount = document.getElementById('actual_amount').value;
        const signature = document.getElementById('signature').value;
        const paymentDetails = document.getElementById('payment_details').value;
        const paymentMethod = document.getElementById('payment_method').value;

        if (!receiptNumber || !date || !receivedFrom || !sumAmount || !actualAmount || !signature || !paymentDetails || !paymentMethod) {
            alert('Please fill in all fields.');
            return false;
        }

        return true;
    }

    const inputs = document.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.style.backgroundColor = '#333';
        });

        input.addEventListener('blur', () => {
            input.style.backgroundColor = 'rgba(255, 255, 255, 0.2)';
        });
    });
});
