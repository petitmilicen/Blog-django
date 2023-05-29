$(document).ready(function() {
  $('#form-registro').validate({
    rules: {
      nombre: {
        required: true,
        minlength: 3
      },
      email: {
        required: true,
        email: true
      },
      password: {
        required: true,
        minlength: 8,
        maxlenght: 20,
        strongPassword: true
      },
      password_2: {
        required: true,
        minlength: 8,
        maxlenght: 20,
        equalTo: "#password"
      }
    },
    messages: {
      nombre: {
        required: "Por favor, ingrese su nombre",
        minlength: "El nombre debe contener al menos 3 caracteres"
      },
      email: {
        required: "Por favor, ingrese su correo electrónico",
        email: "Por favor, ingrese un correo electrónico válido"
      },
      password: {
        required: "Por favor, ingrese una contraseña",
        minlength: "La contraseña debe tener al menos 8 caracteres",
        strongPassword: "La contraseña debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial"
      },
      password_2: {
        required: "Por favor, confirme su contraseña",
        minlength: "La contraseña debe tener al menos 8 caracteres",
        maxlength: "La contraseña debe tener un maximo de 20 caracteres",
        equalTo: "Las contraseñas no coinciden"
      }
    }
  });
});
