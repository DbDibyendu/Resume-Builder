window.onload = function() {
    document.getElementById("download")
        .addEventListener("click", () => {
            const template = this.document.getElementById("w");
            console.log(template);
            console.log(window);
            var opt = {
                margin: [5, 5, 5, 5], //top, left, buttom, right
                filename: this.auth_user,
                image: { type: 'jpeg', quality: 10 },
                html2canvas: {
                    scale: 5,
                },
                pagebreak: { mode: ['css'] },
                jsPDF: {
                    unit: 'mm',
                    orientation: 'portrait'
                }
            };
            html2pdf().from(template).set(opt).save();
        })
}

//! Html to pdf converter