import './CSS/About.css';

const developers = [
  {
    name: 'Eslam',
    role: 'Frontend Developer',
    bio: 'Eslam is a passionate frontend developer who loves building beautiful and intuitive user interfaces.',
    image: 'https://avatars.githubusercontent.com/u/114030950?v=4'
  },
  {
    name: 'Tariq',
    role: 'Backend Developer',
    bio: 'Tariq is a Backend Developer who enjoys working on both the frontend and backend.',
   image: 'https://via.placeholder.com/150'
  },
  {
    name: 'Mohamed',
    role: 'Backend Developer',
    bio: 'Mohamed is a Backend Developer who enjoys working on both the frontend and backend.',
    image: 'https://avatars.githubusercontent.com/u/128869362?v=4'
  },
  {
    name: 'Amal',
    role: 'Backend Developer',
    bio: 'Amal is a Backend developer who enjoys working on the backend.',
    image: 'https://avatars.githubusercontent.com/u/129003996?v=4'
  }
]

function About() {
  return (
    <div className="about-container">
      <h1>About CodyX</h1>
      <p>
        Welcome to CodyX, your go-to platform for solving challenging coding problems.
        Our mission is to provide a comprehensive and engaging environment for developers
        to enhance their problem-solving skills and grow their knowledge.
      </p>
      <p>
        At CodyX, we believe that coding is not just about writing code, but about solving
        problems, thinking critically, and continuously learning. Join our community and
        start solving problems today!
      </p>

      <h2>Meet the Developers</h2>
      <div className="developers-container">
        {developers.map((developer, index) => (
          <div key={index} className="developer-card">
            <img src={developer.image} alt={`${developer.name}'s profile`} width="100" />
            <h3>{developer.name}</h3>
            <p className="developer-role">{developer.role}</p>
            <p className="developer-bio">{developer.bio}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default About