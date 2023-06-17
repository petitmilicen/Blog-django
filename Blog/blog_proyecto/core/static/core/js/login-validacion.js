$(document).ready(function() {
    $('#form-login').validate({
      rules: {
        nomobre: {
          required: true,
          nomobre: true
        },
        password: {
          required: true,
          minlength: 8
        },
      },
      messages: {
        nomobre: {
          required: "Por favor, ingrese su correo electrónico",
          nomobre: "Por favor, ingrese un correo electrónico válido"
        },
        password: {
          required: "Por favor, ingrese una contraseña",
          minlength: "La contraseña debe tener al menos 8 caracteres"
        },

      }
    });
  });
  