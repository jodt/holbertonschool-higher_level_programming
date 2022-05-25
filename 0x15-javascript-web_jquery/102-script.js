window.addEventListener('DOMContentLoaded', (event) => {
  $('#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${language}`, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
