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

  $.validator.addMethod("strongPassword", function(value, element) {
    return this.optional(element) || /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/.test(value);
  }, "La contraseña debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial");

  $.validator.addMethod("validEmail", function(value, element) {
    return this.optional(element) || /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(value);
  }, "Por favor, ingrese un correo electrónico válido");

  $.validator.addMethod("noSpace", function(value, element) {
    return value.trim() !== "";
  }, "El campo no puede contener solo espacios en blanco");

  $.validator.addMethod("noSpecialCharacters", function(value, element) {
    return this.optional(element) || /^[a-zA-Z0-9]+$/.test(value);
  }, "El campo no puede contener caracteres especiales");

  $.validator.addMethod("noCommonPasswords", function(value, element) {
    var commonPasswords = ["123456", "password", "qwerty"]; // Agrega más contraseñas comunes aquí
    return !commonPasswords.includes(value.toLowerCase());
  }, "La contraseña no puede ser una contraseña común");
});
