// Detect text box
document.addEventListener("focusin", (e) => {
    if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") {
        window.postMessage({ type: "voiceTypingInText" }, "*");
        
    }
});

// Detect when you leve a text box
document.addEventListener("focusout", (e) => {
    if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") {
        window.postMessage({ type: "voiceTypingNotInText" }, "*");
    }
});
