import logo from './logo.svg';
import './App.css';
// import Alert from 'react-bootstrap/Alert';


import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <>
      {[
        'primary',
        'secondary',
        'success',
        'danger',
        'warning',
        'info',
        'light',
        'dark',
      ].map((variant) => (
        <div className={`d-flex align-content-center justify-content-center alert alert-${variant}`} key={variant}>
          This is a {variant} alert with{' '}
          <div><a href="#">an example link</a></div>Give it a click if
          you like.
        </div>
      ))}
    </>
  );
}

export default App;
