// This assumes that you're using Rouge; if not, update the selector
const codeBlocks = document.querySelectorAll('.code-header + * > .highlighter-rouge, .code-header + .highlighter-rouge');
const copyCodeButtons = document.querySelectorAll('.copy-code-button');

copyCodeButtons.forEach((copyCodeButton, index) => {

  copyCodeButton.addEventListener('click', () => {
    const code = codeBlocks[index].innerText;
    // Copy the code to the user's clipboard
    window.navigator.clipboard.writeText(code);

    // Update the button text visually
    const { innerHTML: originalHTML } = copyCodeButton;
    copyCodeButton.innerHTML = '<i class="fa-solid fa-clone"></i>';

    // (Optional) Toggle a class for styling the button
    copyCodeButton.classList.add('copied');

    // After 2 seconds, reset the button to its initial UI
    setTimeout(() => {
      copyCodeButton.innerHTML = originalHTML;
      copyCodeButton.classList.remove('copied');
    }, 2000);
  });
});
