import CodeMirror from '@uiw/react-codemirror';
import { javascript } from '@codemirror/lang-javascript';
import { vscodeDark } from '@uiw/codemirror-theme-vscode';
import './ProblemEditor.css';
import PropTypes from 'prop-types';

function ProblemEditor({ starterCode }) {
  
  return (
    <div className='codeeditor'>
      <span className='codeType'>javascript</span>
      <CodeMirror value={starterCode} theme={vscodeDark} height='89vh'  extensions={[javascript({ jsx: true })]} style={{ flex: 1 }}/>
    </div>
  )
}

ProblemEditor.propTypes = {
  starterCode: PropTypes.string.isRequired
}

export default ProblemEditor