import React, { useEffect, useState } from "react";
import Logo from "../assets/logo.png";
import { FaEye } from "react-icons/fa6";
import { FaEyeSlash } from "react-icons/fa6";
import "../styles/Register.css";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { toast } from "react-toastify";



const Login = () => {
  const [ showPassword, setShowPassword ] = useState(false);
  const navigate = useNavigate();
  const [ token, setToken ] = useState(JSON.parse(localStorage.getItem("auth")) || "");



  const handleRegisterSubmit = async (e) => {
    e.preventDefault();
    let name = e.target.name.value;
    let lastname = e.target.lastname.value;
    let email = e.target.email.value;
    let password = e.target.password.value;
    // let confirmPassword = e.target.confirmPassword.value;

    // if(name.length > 0 && lastname.length > 0 && email.length > 0 && password.length > 0 && confirmPassword.length > 0){
    if(name.length > 0 && lastname.length > 0 && email.length > 0 && password.length > 0 ){

      // if(password === confirmPassword){
      if(password){
        const formData = {
          username: name + " " + lastname,
          mailid:email,
          password
        };
        console.log(formData);
        try{
        const response = await axios.put("http://0.0.0.0:6999/credentials/create", formData);
        console.log(response.data);
         if(response.data.status == 'success'){
          toast.success("Registration successfull");
          navigate("/login");
         }else{
          toast.error(response.data.message);
          navigate("/register");
          e.target.reset();
         } 
         
       }catch(err){
        console.log(err);
         toast.error("User Already Present");
       }
      }else{
        toast.error("Passwords don't match");
      }
    

    }else{
      toast.error("Please fill all inputs");
    }


  }

  useEffect(() => {
    if(token == "True"){
      toast.success("You already logged in");
      navigate("/dashboard");
    }
  }, []);

  return (
    <div className="register-main">
      <div className="register-right">
        <div className="register-right-container">
          <div className="register-logo">
            <img src={Logo} alt="" />
          </div>
          <div className="register-center">
            {/* <h2>Welcome to our website!</h2>
            <p>Please enter your details</p> */}
            <form onSubmit={handleRegisterSubmit}>
            <input type="text" placeholder="Name" name="name" required={true} />
            <input type="text" placeholder="Lastname" name="lastname" required={true} />
              <input type="email" placeholder="Email" name="email" required={true} />
              <div className="pass-input-div">
                <input type={showPassword ? "text" : "password"} placeholder="Password" name="password" required={true} />
                {showPassword ? <FaEyeSlash onClick={() => {setShowPassword(!showPassword)}} /> : <FaEye onClick={() => {setShowPassword(!showPassword)}} />}
                
              </div>
              {/* <div className="pass-input-div">
                <input type={showPassword ? "text" : "password"} placeholder="Confirm Password" name="confirmPassword" required={true} />
                {showPassword ? <FaEyeSlash onClick={() => {setShowPassword(!showPassword)}} /> : <FaEye onClick={() => {setShowPassword(!showPassword)}} />}
                
              </div> */}
              <div className="register-center-buttons">
                <button type="submit">Sign Up</button>
                {/* <button type="submit">
                  <img src={GoogleSvg} alt="" />
                  Sign Up with Google
                </button> */}
              </div>
            </form>
          </div>

          <p className="login-bottom-p">
            Already have an account? <Link to="/Login">Login</Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;