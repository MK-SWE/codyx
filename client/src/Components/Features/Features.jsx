import './Features.css';

const featuresData = [
  {
    title: 'Challenging Problems',
    description: 'Solve a wide variety of challenging coding problems that will test your skills and knowledge.'
  },
  {
    title: 'Community Support',
    description: 'Engage with a community of developers to discuss problems, share solutions, and get help.'
  },
  {
    title: 'Detailed Explanations',
    description: 'Access detailed explanations and solutions for each problem to improve your understanding.'
  },
  {
    title: 'Regular Updates',
    description: 'Enjoy regularly updated content with new problems added frequently to keep you engaged.'
  },
  {
    title: 'Personalized Recommendations',
    description: 'Receive personalized problem recommendations based on your interests and skill level.'
  }
];

const Features = () => {
  return (
    <div className="features">
      <h2>Key Features of CodyX</h2>
      <div className="features-cards">
        {featuresData.map((feature, index) => (
          <div className="card" key={index}>
            <h3>{feature.title}</h3>
            <p>{feature.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Features;
