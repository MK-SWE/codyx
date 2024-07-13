import './ProblemContent.css';
import problemsList from '../../assets/mockProblems';
import { Link } from "react-router-dom";


function ProblemContent() {
  return (
    <div className='problemcontent'>
      <table>
        <thead>
          <tr>
            <th className='status'>Status</th>
            <th>Title</th>
            <th>Difficulty</th>
            <th>Category</th>
          </tr>
        </thead>
        <tbody>
          {
            problemsList.map((problem) => {
              return (
                <tr key={problem.id}> 
                  <th className='status'>✓</th>
                  <td>
                    <Link to={`/problems/${problem.id}`}>{problem.title}</Link>
                  </td>
                  <td>
                    {problem.difficulty}
                  </td>
                  <td>
                    {problem.category}
                  </td>
                </tr>
              )
            })
          }
        </tbody>
      </table>
    </div>
  )
}

export default ProblemContent