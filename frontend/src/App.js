import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
// import HomeLayout from './components/HomeLayout';
// import Login from './components/Login';
// import Register from './components/Register';
// import Dashboard from './components/Dashboard';
// import Logout from './components/Logout';
import { Dashboard, HomeLayout, Landing, Login, Logout, Register, Contact, Premium } from "./pages";
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  return (
    <>
    <ToastContainer
      position="top-right"
      autoClose={5000}
      hideProgressBar={false}
      newestOnTop={false}
      closeOnClick
      rtl={false}
      pauseOnFocusLoss
      draggable
      pauseOnHover
      theme="light"
      // transition: Bounce,
      />
      {/* Same as */}
      <ToastContainer />

    <Router>
      <Routes>
        <Route path="/" element={<HomeLayout />}>
          <Route path="login" element={<Login />} />
          <Route path="register" element={<Register />} />
          <Route index  element={<Dashboard />} />
          <Route path="logout" element={<Logout />} />
          <Route path="contact" element={<Contact />} />
          <Route path="premium" element={<Premium />} />
          <Route path="*" element={<Navigate replace to="/" />} />
        </Route>
      </Routes>
    </Router>
    </>
  );
}

export default App;
