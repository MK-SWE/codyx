import CodeMirror from '@uiw/react-codemirror';
import { javascript } from '@codemirror/lang-javascript';
import { vscodeDark } from '@uiw/codemirror-theme-vscode';
import './ProblemEditor.css';
import PropTypes from 'prop-types';
import { useState } from 'react';
import { submitProblem } from '../../../redux/reducers/submitSlice';
import { useDispatch, useSelector } from 'react-redux';

function ProblemEditor(props) {
  const { starterCode, id } = props;
  const [code, setCode] = useState(starterCode);
  const language = useState('javascript')[0];

  const dispatch = useDispatch();
  const submitDetails = useSelector((state) => state.submitDetails.submitDetails);
  const loading = useSelector((state) => state.submitDetails.loading);
  const error = useSelector((state) => state.submitDetails.error);

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(submitProblem({ code, problemId: id, language }));

  }
  if (loading){
    console.log("loading");
  }else if (error){
    console.log("error");
  } else{
    console.log(submitDetails);
  }
  
  return (
    <div className='codeeditor'>
      <div className='naveditor'>
        <span className='codeType'>{language}</span>
        <button onClick={(e) => handleSubmit(e)}>Submit</button>
      </div>
      <CodeMirror value={starterCode}  theme={vscodeDark} height='88vh'  extensions={[javascript({ jsx: true })]} style={{ flex: 1 }} onChange={(editor) => {setCode(editor)}}/>
    </div>
  )
}

ProblemEditor.propTypes = {
  starterCode: PropTypes.string.isRequired,
  id: PropTypes.string.isRequired
}

export default ProblemEditor