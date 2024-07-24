import './ProblemDescription.css';
import PropTypes from 'prop-types';
// import Problems from '../../../Utils/Problems';

function ProblemDescription({problem}) {
  return (
    <div className='problemdescription'>
      <h2>{ problem.title }</h2>
      <div dangerouslySetInnerHTML={{ __html: problem.problemStatement }} />
      <div>
        { problem.examples.map((example, index) => (
          <div key={index} className='example-container'>
            <h4>Example {index + 1}:</h4>
            <p><strong>Input:</strong> {example.inputText}</p>
            <p><strong>Output:</strong> {example.outputText}</p>
            {example.explanation && <p><strong>Explanation:</strong> {example.explanation}</p>}
          </div>
        )) }
      </div>
      <div className='Constraints'>
        <h3>Constraints:</h3>
        <ul dangerouslySetInnerHTML={{__html:problem.constraints}}>
        </ul>
      </div>
    </div>
  )
}

ProblemDescription.propTypes = {
  problem: PropTypes.object
}

export default ProblemDescription