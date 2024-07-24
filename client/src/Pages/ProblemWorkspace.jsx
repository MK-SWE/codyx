import { useParams } from "react-router-dom";
import Split from 'react-split';
import './CSS/ProblemWorkspace.css'
import ProblemDescription from "../Components/WorkSpace/ProblemDescription/ProblemDescription";
import ProblemEditor from "../Components/WorkSpace/ProblemEditor/ProblemEditor";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { fetchProblemDetails, selectProblemDetails } from "../redux/reducers/problemDetailsSlice";

function ProblemWorkspace() {
  const { problemId } = useParams();
  const dispatch = useDispatch();
  const { problem, loading, error } = useSelector((state) => selectProblemDetails(state) || {});

  useEffect(() => {
    if (problemId) {
      dispatch(fetchProblemDetails(problemId));
    }
  }, [dispatch, problemId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!problem) return <div>No problem details available.</div>;

  return (
    <div className="workspace" >
      <Split className="split" minSize={400}>
        <div><ProblemDescription problem={problem} /></div>
        <div><ProblemEditor starterCode={problem.starterCode} id={problem.id}/></div>   
      </Split>
    </div>
  )
}



export default ProblemWorkspace