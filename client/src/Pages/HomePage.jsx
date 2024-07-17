import Features from "../Components/Features/Features";
import Footer from "../Components/Footer/Footer";
import Hero from "../Components/Hero/Hero";
import './CSS/HomePage.css';

function HomePage() {
  return (
    <div className="homepage">
      <Hero />
      <Features />
      <Footer />
    </div>
  )
}

export default HomePage;
