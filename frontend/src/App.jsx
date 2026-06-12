import Header from "./components/Header";
import Banner from "./components/Banner";
import Footer from "./components/Footer";

function App() {
  return (
    <>
      <Header />

      <Banner
        title="Welcome to ShopHub"
        description="Your Online Shopping Destination"
      />

      <Footer />
    </>
  );
}

export default App;