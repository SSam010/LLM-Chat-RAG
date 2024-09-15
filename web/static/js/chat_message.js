var model;
let controller = null;
var signal = null;
var loadingAnimationLogo = document.getElementById('loading');


function clearScreen() {
    if (controller) controller.abort();
    controller = new AbortController();
    signal = controller.signal;

    var infoContainer = document.getElementById("info-container");
    var chatMessages = document.getElementById("chat-messages");
    infoContainer.innerHTML = '';
    chatMessages.innerHTML = '';
    document.getElementById("user-input").disabled = false;
    document.getElementById("send-button").disabled = false;
    loadingAnimationLogo.style.display = 'none';
}

document.getElementById("send-button").addEventListener("click", function () {
    document.getElementById("user-input").disabled = true;
    this.disabled = true;

    sendMessage();
});

document.getElementById("user-input").addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
        document.getElementById("send-button").disabled = true;
        this.disabled = true;

        sendMessage();
    }
});

function updateInfoWindow(data, message) {
    var infoContainer = document.getElementById("info-container");
    var infoSource = document.createElement("div");
    infoSource.id = "info-source"
    infoContainer.appendChild(infoSource);
    var header = document.createElement("h5");
    var message_short = message
    if (message.length > 25) {
        message_short = message_short.substring(0, 15) + "...";
    }
    header.textContent = "Extra info for: " + message_short;
    infoSource.appendChild(header);

    data.response.sources.forEach(function (source, index) {
        var details = document.createElement("details");
        var summary = document.createElement("summary");
        summary.textContent = "Source " + (index + 1);
        summary.id = "source-list"
        summary.className = "dropdown-focus";
        details.appendChild(summary);

        source.meta.forEach(function (item) {
            var summary = document.createElement("summary");
            summary.textContent = item;
            summary.className = "truncate";
            summary.id = "ext-content"
            summary.addEventListener("click", function () {
                if (this.className === "truncate") {
                    this.className = "truncate-open";
                } else {
                    this.className = "truncate";
                }
            });

            details.appendChild(summary);
        });

        var summaryChunk = document.createElement("summary");
        summaryChunk.textContent = source.chunk;
        summaryChunk.className = "truncate";
        summaryChunk.id = "ext-content"

        summaryChunk.addEventListener("click", function () {
            if (this.className === "truncate") {
                this.className = "truncate-open";
            } else {
                this.className = "truncate";
            }
        });

        details.appendChild(summaryChunk);

        infoSource.appendChild(details);
        if(primarySource) {
            var resource_link = document.createElement("a");
            resource_link.href = primarySource + source.id;
            resource_link.target = "_blank";
            var button = document.createElement("button");
            button.type = "button";
            button.className = "btn btn-outline-info";
            button.id = "ext-button";
            button.textContent = "Read the full article";
            resource_link.appendChild(button);
            details.appendChild(resource_link);
        }
        infoContainer.scrollTop = infoContainer.scrollHeight;
    });
}


function sendMessage() {
    if (controller) controller.abort();
    controller = new AbortController();
    signal = controller.signal;
    
    var userMessage = document.getElementById("user-input").value;
    $('#presets').remove();
    loadingAnimationLogo.style.display = 'block';
    displayMessage(userMessage, "user-message", false);

    fetch(dataset + "/ask/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({text: userMessage}),
        signal: signal
    })
        .then(response => response.json())
        .then(data => {
            var botMessage = data.response.result;
            loadingAnimationLogo.style.display = 'none';
            displayMessage(botMessage, "bot-message", data, userMessage);
        })
        .catch(error => {
            if (error.name === 'AbortError') {
                console.log('Fetch request has been aborted');
            } else {
                console.error('Error:', error);
            }
        });

    document.getElementById("user-input").value = "";
}

function displayMessage(message, className, data, userMessage) {
    var chatMessages = document.getElementById("chat-messages");
    var messageElement = document.createElement("div");
    messageElement.classList.add("message");

    chatMessages.appendChild(messageElement);
    animateMessage(messageElement, message, className, data, userMessage);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}


function animateMessage(messageElement, messageText, className,
                        data, userMessage) {
    messageElement.classList.add(className);

    if (className === "user-message") {
        messageElement.textContent = messageText;
    } else {
        var index = 0;
        var typingInterval = setInterval(function () {
            if (index < messageText.length) {
                messageElement.textContent += messageText.charAt(index);
                index++;
                messageElement.parentElement.scrollTop = messageElement.parentElement.scrollHeight;
            } else {
                clearInterval(typingInterval);
                document.getElementById("user-input").disabled = false;
                document.getElementById("send-button").disabled = false;
                if (data) {
                    updateInfoWindow(data, userMessage);
                }
            }
        }, 2);
    }
}


$(document).ready(function() {
    $('.preset').click(function() {
        var presetText = $(this).text();
        $('#user-input').val(presetText);
        $('#send-button').click();

    });
});