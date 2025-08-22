function ABTaddToCart(name, price, image) {
  const cart = JSON.parse(localStorage.getItem("cartItems")) || [];
  cart.push({ name, price: Number(price), image });
  localStorage.setItem("cartItems", JSON.stringify(cart));
}

document.addEventListener("click", (e) => {
  if (e.target.closest(".js-add")) {
    const card = e.target.closest(".ABTproduct");
    const { name, price, image } = card.dataset;
    ABTaddToCart(name, Number(price), image);
    alert(name + " added to cart!");
  }

  if (e.target.closest(".js-buy")) {
    const card = e.target.closest(".ABTproduct");
    const { name, price, image } = card.dataset;
    ABTaddToCart(name, Number(price), image);
    window.location.href = "/cart";  // redirect to Flask cart route
  }
});