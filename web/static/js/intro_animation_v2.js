window.addEventListener("load", function () {
    var loader = document.getElementById("loader");
    loader.style.animation = "fade-in 1.5s forwards";

    loader.addEventListener("animationend", function () {
        var chatCont = document.getElementById("chat");
        chatCont.style.display = "flex";

        var mainContainer = document.getElementById("main-container");
        mainContainer.style.display = "flex";
        mainContainer.style.justifyContent = "space-between";
        mainContainer.style.width = "100%";

        var userInputContainer = document.getElementById("user-input-container");
        userInputContainer.style.background = "#5e5e5d";

        var asideContainer = document.getElementById("aside-conteiner");
        asideContainer.style.backgroundImage = "url('/static/image/mda.jpg')";

        var chatContainerGeneral = document.getElementById("chat-container-general");
        chatContainerGeneral.style.backgroundImage = "url('/static/image/backstage.png')";
        chatContainerGeneral.style.backgroundImage = dataset === "first_db_rag"
            ? "url('/static/image/first_rag.png')"
            : "url('/static/image/second_rag.png')";


        loader.style.animation = "fade-out 1s forwards";

        loader.addEventListener("animationend", function () {
            loader.style.display = "none";
        });
    });
});
