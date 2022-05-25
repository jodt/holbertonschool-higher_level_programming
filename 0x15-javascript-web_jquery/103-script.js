window.addEventListener('DOMContentLoaded', (event) => {
  $('#btn_translate').click(function () {
    const language = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${language}`, function (data) {
      $('#hello').text(data.hello);
    });
  });
  $(document).keypress(function (event) {
    if ($('#language_code').is(':focus')) {
      if (event.key === 'Enter') {
        const language = $('#language_code').val();
        $.get(`https://www.fourtonfish.com/hellosalut/?lang=${language}`, function (data) {
          $('#hello').text(data.hello);
        });
      }
    }
  });
});
