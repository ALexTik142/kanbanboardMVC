document.addEventListener('DOMContentLoaded', function() {
    var currentDateElement = document.getElementById('currentDate');
    var currentDate = new Date();
    currentDateElement.textContent = 'Сегодня ' + currentDate.toLocaleDateString('ru-RU');
});