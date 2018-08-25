$(document).ready(function(){
     function signIn() {
     	console.log(document.getElementByName('username'));
     	console.log(document.getElementByName('pass'));
     }

     $('.login100-form-btn').on('click',signIn);
});