const data = JSON.stringify({
  "nombre": "Restaurante 1",
  "direccion": "Calle 123, 123",
  "tipo_cocina": "Italiana"
});

const xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === this.DONE) {
    console.log(this.responseText);
  }
});

xhr.open("POST", "http://127.0.0.1:8000/restaurantes/create/");
xhr.setRequestHeader("Authorization", "Bearer csrfmiddlewaretoken=nci9wmd6S22dsYVOpIvMZ8oDPbMNhpkx");

xhr.send(data);