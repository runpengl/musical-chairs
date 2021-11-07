for (let i = 0; i < document.getElementsByTagName("input").length - 1; i++) {
    let elem = document.getElementsByTagName("input")[i];
    elem.oninput = function() {
        if ("ABCDEFGHIJKLMNOPQRSTUVWXYZ".indexOf(this.value.toLocaleUpperCase()) === -1) {
            this.value = '';
            return;
        }

        if (this.value.length > 0) {
            try {
                document.getElementsByTagName("input")[i + 1].focus();
            } catch (e) {}
        }
    }
}

document.addEventListener("keydown", (e) => {
    if (e.keyCode === 8 || e.keyCode === 46) {
        let activeIndex = -1;
        for (let i = 0; i < document.getElementsByTagName("input").length; i++) {
            if (document.getElementsByTagName("input")[i] === document.activeElement) {
                activeIndex = i;
            }
        };
        if (activeIndex > -1) {
            document.activeElement.value = '';
            try {
                let prevElement = document.getElementsByTagName("input")[activeIndex - 1];
                prevElement.focus();
            } catch (e) {}
        }
    }
});