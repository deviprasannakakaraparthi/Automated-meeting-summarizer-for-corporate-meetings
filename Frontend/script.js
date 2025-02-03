document.getElementById('upload-form').onsubmit = async function(event) {
    event.preventDefault();
    let formData = new FormData();
    formData.append('file', document.getElementById('file').files[0]);
    
    let response = await fetch('/summarize', {
        method: 'POST',
        body: formData
    });
    let result = await response.json();
    document.getElementById('summary').innerText = result.summary;
};

