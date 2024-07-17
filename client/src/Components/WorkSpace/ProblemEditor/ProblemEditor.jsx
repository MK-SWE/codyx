import CodeMirror from '@uiw/react-codemirror';
import { javascript } from '@codemirror/lang-javascript';
import { vscodeDark } from '@uiw/codemirror-theme-vscode';
import './ProblemEditor.css';

function ProblemEditor() {
  
  return (
    <div className='codeeditor'>
      <span className='codeType'>javascript</span>
      <CodeMirror value="console.log('hello world!');" theme={vscodeDark} height='83vh'  extensions={[javascript({ jsx: true })]}/>
    </div>
  )
}

export default ProblemEditor