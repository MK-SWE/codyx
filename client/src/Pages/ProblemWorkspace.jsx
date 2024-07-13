import { useParams } from "react-router-dom";
import Split from 'react-split';
import './CSS/ProblemWorkspace.css'
import ProblemDescription from "../Components/WorkSpace/ProblemDescription/ProblemDescription";
import ProblemEditor from "../Components/WorkSpace/ProblemEditor/ProblemEditor";

function ProblemWorkspace() {
  const { problemId } = useParams();

  return (
    <div className="workspace" >
      <Split className="split" minSize={400}>
        <div><ProblemDescription id={problemId}/></div>
        <div><ProblemEditor /></div>   
      </Split>
    </div>
  )
}



export default ProblemWorkspace