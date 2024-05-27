const data = null;

const xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === this.DONE) {
    console.log(this.responseText);
  }
});

xhr.open("GET", "http://127.0.0.1:8000/restaurantes/create/");
xhr.setRequestHeader("Authorization", "CSRFToken ");

xhr.send(data);