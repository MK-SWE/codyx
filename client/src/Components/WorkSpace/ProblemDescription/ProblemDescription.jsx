import './ProblemDescription.css';
import PropTypes from 'prop-types';
// import Problems from '../../../Utils/Problems';

function ProblemDescription({id}) {
  return (
    <div>
      {/* {Problems[id].problemStatement} */}
      {id}
    </div>
  )
}

ProblemDescription.propTypes = {
  id: PropTypes.string
}

export default ProblemDescription