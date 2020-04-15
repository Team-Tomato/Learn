document.addEventListener("onclick", function(e) {
    if (!e.target.classList.contains("page-choice")) {
        return;
    }
    var chosenPage = "https://" + e.target.textContent;
    chrome.tabs.create({
        url: chosenPage,
    });
});
