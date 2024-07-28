import CodeMirror from '@uiw/react-codemirror';
import { javascript } from '@codemirror/lang-javascript';
import { python } from '@codemirror/lang-python';
import { vscodeDark } from '@uiw/codemirror-theme-vscode';
import './ProblemEditor.css';
import PropTypes from 'prop-types';
import { useState, useEffect } from 'react';
import { submitProblem } from '../../../redux/reducers/submitSlice';
import { useDispatch, useSelector } from 'react-redux';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Confetti from 'react-confetti';

function ProblemEditor(props) {
  const { starterCode, id } = props;
  const [success, setSuccess] = useState(false);
  const [code, setCode] = useState(starterCode);
  const [language, setLanguage] = useState("javascript"); 

  const dispatch = useDispatch();
  
  const data = useSelector((state) => state.submitDetails.data);
  const loading = useSelector((state) => state.submitDetails.loading);
  const error = useSelector((state) => state.submitDetails.error);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (loading === 'pending') return;
    dispatch(submitProblem({ code, problemId: id, language }));
  };

  useEffect(() => {
    if (data.success && !success) {
      setSuccess(true);
      toast.success("submitted successfully", {
        position: "top-center",
        autoClose: 4000,
        closeOnClick: true,
        theme: "dark",
      })}
    else if (data.error && !success) {
        toast.error("submission failed", {
          position: "top-center",
          autoClose: 4000,
          closeOnClick: true,
          theme: "dark",
        })
      }
  }, [error, data, success]);

  const getExtension = () => {
    switch (language){
      case 'python':
        return [python()];
      case 'javascript':
        return [javascript({ jsx: true })];
    }
  }

  const handleLanguage = (value) => {
      setLanguage(value);
      switch (value){
        case 'python':
          setCode(code.replace(/\/\//g, '#')
                       .replace(/function/g, 'def')
                       .replace(/{/g, ':')
                       .replace(/}/g, '')
          );
          break;
        case 'javascript':
          setCode(code.replace(/#/g, '//')
                      .replace(/def/g, 'function')
                      .replace(/:/g, '{')
                      + '}'
          );
      }
  }

  return (
    <div className='codeeditor'>
      <div className='naveditor'>
        <select
          className='codeType'
          value={language}
          onChange={(e) => handleLanguage(e.target.value)}
        >
          <option value='javascript'>JavaScript</option>
          <option value='python'>Python</option>
        </select>
        <button onClick={handleSubmit}>Submit</button>
      </div>
      <CodeMirror
        value={code}
        theme={vscodeDark}
        height='88vh'
        extensions={getExtension()}
        onChange={(value) => setCode(value)}
      />
      {success && (
        <Confetti
          width={window.innerWidth}
          height={window.innerHeight}
          recycle={false}
          numberOfPieces={400}
          gravity={0.3}
        />
      )}
      <ToastContainer />
    </div>
  );
}

ProblemEditor.propTypes = {
  starterCode: PropTypes.string.isRequired,
  id: PropTypes.number.isRequired,
};

export default ProblemEditor;
