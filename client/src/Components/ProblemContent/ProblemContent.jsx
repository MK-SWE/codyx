import './ProblemContent.css';
import { Link } from "react-router-dom";
import { fetchProblems } from '../../redux/reducers/problemSlice';
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from 'react';


function ProblemContent() {
  const dispatch = useDispatch();
  const problems = useSelector((state) => state.problems.problemList);
  const loading = useSelector((state) => state.problems.loading);
  const error = useSelector((state) => state.problems.error);

  useEffect(() => {
    dispatch(fetchProblems());
  }, [dispatch]);

  if (loading === 'pending') {
    return <p>Loading problems...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

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
            problems.map((problem) => {
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