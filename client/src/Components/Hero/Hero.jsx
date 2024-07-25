import './Hero.css';
import hero_icon from '../../assets/hero_icon.png';

function Hero() {
  return (
    <div className='hero'>
      <div className="left">
        <h1>Welcome to <span>CodyX</span></h1>
        <p>Level up your coding skills with challenging problems.</p>
        <button><i></i><span>Get Started Now</span></button>
      </div>
      <div className="right">
        <img src={hero_icon} alt="" />
      </div>
    </div>
  )
}

export default Hero