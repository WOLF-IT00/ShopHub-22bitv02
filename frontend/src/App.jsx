import Header from "./components/Header";
import Banner from "./components/Banner";
import Footer from "./components/Footer";
import ProductList from "./components/ProductList";

function App() {
  return (
    <>
      <Header />

      <Banner
        title="Welcome to ShopHub"
        description="Your Online Shopping Destination"
      />

      <ProductList />

      <Footer />
    </>
  );
}

export default App;