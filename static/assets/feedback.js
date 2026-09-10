(function () {
  "use strict";

  document.querySelectorAll(".feedback-form").forEach(function (form) {
    form.addEventListener("submit", function () {
      var message = form.querySelector("textarea[name='body']");
      var pageTitle = form.dataset.pageTitle;
      var pageUrl = window.location.href.split("#")[0];
      var feedback = message.value.trim();

      message.value = [
        feedback,
        "",
        "---",
        "Page: " + pageTitle,
        "URL: " + pageUrl
      ].join("\n");

      window.setTimeout(function () {
        message.value = feedback;
      }, 0);
    });
  });
}());
