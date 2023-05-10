
// get heistform
form = document.querySelector('form.heist_form') as HTMLFormElement!;
imageFields = form.querySelectorAll('p:has(input[accept="image/*"])')

imageFields.forEach(field => {
   anchor = field.querySelector('a')
   image = document.createElement('img')
   image.src = anchor.href
   anchor.child

   console.log(image);
});